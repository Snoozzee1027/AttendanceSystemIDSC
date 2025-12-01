import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, PhotoImage, scrolledtext, filedialog
import subprocess, threading, os, sys, socket, time, requests, shutil, platform, webbrowser
from pathlib import Path
import psutil

# Config
FLASK_PORT = 5000
server_process = None
server_running = False
log_visible = False
login_successful = False
LOG_LOCK = threading.Lock()
AUTO_RESTART_SERVER = True
THEME = "light"

LOGO_PATH = os.path.join(os.path.abspath("."), "static", "logo.png")
APP_NAME = "Attendance Launcher"

# Utilities
def get_local_and_lan_ip():
    local_ip, lan_ip = "127.0.0.1", "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lan_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass
    return local_ip, lan_ip

def wait_for_server_ready_request(timeout=15):
    url = f"http://127.0.0.1:{FLASK_PORT}/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code < 500:
                return True
        except Exception:
            pass
        time.sleep(0.4)
    return False

def find_app_py_systemwide(limit_roots=None):
    search_roots = []
    home = os.path.expanduser("~")
    for folder in ["Desktop", "Documents", "Downloads"]:
        search_roots.append(os.path.join(home, folder))
    if platform.system() == "Windows":
        search_roots.append("C:\\")
    else:
        search_roots.append(home)
    if limit_roots:
        search_roots = [p for p in search_roots if os.path.exists(p)]
    skip_substrings = ["site-packages", os.path.join("Lib","site-packages"), "__pycache__", ".git", "node_modules"]
    for root in search_roots:
        if not os.path.exists(root): continue
        for dirpath, dirnames, filenames in os.walk(root):
            if any(skip in dirpath for skip in skip_substrings):
                continue
            if "app.py" in filenames:
                candidate = os.path.join(dirpath, "app.py")
                if "site-packages" in candidate or candidate.lower().endswith(os.path.join("flask","app.py")):
                    continue
                return candidate
    return None

def append_log(line):
    with LOG_LOCK:
        try:
            log_text.configure(state="normal")
            log_text.insert(tk.END, line)
            log_text.see(tk.END)
            log_text.configure(state="disabled")
        except Exception:
            pass

# Server
def _stream_process_output(proc):
    global server_running
    try:
        while server_running and proc and proc.stdout:
            line = proc.stdout.readline()
            if not line: break
            append_log(line)
    except Exception:
        pass
    server_running = False
    if AUTO_RESTART_SERVER and login_successful:
        append_log("[launcher] Server crashed. Auto-restarting...\n")
        start_server_action()

def start_server_action():
    global server_process, server_running
    if not login_successful:
        messagebox.showwarning("Access denied", "Please login as admin first.")
        return
    if server_running:
        messagebox.showinfo("Server", "Server is already running.")
        return

    append_log("[launcher] Searching for app.py...\n")
    app_path = find_app_py_systemwide()
    if not app_path:
        append_log("[launcher] ERROR: app.py not found.\n")
        messagebox.showerror("app.py not found", "Could not find app.py in common folders or project root.")
        return

    append_log(f"[launcher] Found app.py: {app_path}\n")
    app_dir = os.path.dirname(app_path)
    venv_py = os.path.join(app_dir, "venv", "Scripts", "python.exe") if platform.system()=="Windows" else os.path.join(app_dir, "venv", "bin", "python")
    python_exec = venv_py if os.path.exists(venv_py) else (shutil.which("python") or sys.executable)
    append_log(f"[launcher] Using Python executable: {python_exec}\n")

    creation_flags = subprocess.CREATE_NO_WINDOW if platform.system()=="Windows" else 0
    try:
        server_process = subprocess.Popen([python_exec, app_path], cwd=app_dir,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                          text=True, creationflags=creation_flags)
    except Exception as e:
        append_log(f"[launcher] Failed to start: {e}\n")
        messagebox.showerror("Failed to start", f"Failed to launch app.py:\n{e}")
        return

    server_running = True
    append_log("[launcher] Server process started — waiting for ready...\n")
    threading.Thread(target=_stream_process_output, args=(server_process,), daemon=True).start()

    def _wait():
        ok = wait_for_server_ready_request(timeout=12)
        if ok:
            status_indicator.config(bg="#27ae60")
            status_label.config(text="Server running", fg="#ffffff")
            start_btn.configure(state="disabled")
            stop_btn.configure(state="normal")
            restart_btn.configure(state="normal")
            append_log(f"[launcher] Server reachable at http://127.0.0.1:{FLASK_PORT}/\n")
        else:
            status_indicator.config(bg="#c0392b")
            status_label.config(text="Server failed to start", fg="#ffffff")
            append_log("[launcher] Server did not respond in time.\n")
    threading.Thread(target=_wait, daemon=True).start()

def stop_server_action():
    global server_process, server_running
    if server_process:
        append_log("[launcher] Terminating server process...\n")
        try:
            server_running = False
            # Terminate first
            server_process.terminate()
            server_process.wait(timeout=3)
        except Exception:
            try:
                # If terminate fails, force kill
                server_process.kill()
            except Exception:
                append_log("[launcher] Failed to terminate server process completely.\n")
        finally:
            server_process = None
            append_log("[launcher] Server stopped.\n")
    # Update UI
    status_indicator.config(bg="#c0392b")
    status_label.config(text="Server stopped", fg="#ffffff")
    start_btn.configure(state="normal")
    stop_btn.configure(state="disabled")
    restart_btn.configure(state="disabled")
    hide_admin_controls()


def restart_server_action():
    stop_server_action()
    time.sleep(0.6)
    start_server_action()

# Admin / QR 
def get_accessible_url(path="/"):
    localhost = f"http://127.0.0.1:{FLASK_PORT}{path}"
    try:
        requests.get(localhost, timeout=1)
        return localhost
    except Exception:
        _, lan = get_local_and_lan_ip()
        return f"http://{lan}:{FLASK_PORT}{path}"

def open_admin_in_browser():
    webbrowser.open(get_accessible_url("/admin"))

def open_qr_in_browser():
    webbrowser.open(get_accessible_url("/"))

# Admin controls
def show_admin_controls():
    admin_frame.pack_configure(fill="x", padx=18, pady=(6,14))
    admin_frame.update()

def hide_admin_controls():
    admin_frame.pack_forget()

def toggle_log_panel():
    global log_visible
    if log_visible:
        log_frame.pack_forget()
        log_visible = False
        log_toggle_btn.config(text="Show Log")
    else:
        log_frame.pack(fill="both", padx=16, pady=(6,16), expand=False)
        log_visible = True
        log_toggle_btn.config(text="Hide Log")

def export_log_action():
    path = filedialog.asksaveasfilename(title="Save Log", defaultextension=".txt", filetypes=[("Text files","*.txt")])
    if path:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(log_text.get("1.0", tk.END))
            messagebox.showinfo("Exported", f"Log saved to {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save log: {e}")

# Credentials
def change_credentials_action():
    creds_file = os.path.join(os.path.abspath("."), "credentials.txt")
    new_user = simpledialog.askstring("New Username", "Enter new admin username:")
    if not new_user: return
    new_pass = simpledialog.askstring("New Password", "Enter new admin password:", show="*")
    if not new_pass: return
    try:
        with open(creds_file, "w", encoding="utf-8") as f:
            f.write(new_user.strip() + "\n")
            f.write(new_pass.strip() + "\n")
        messagebox.showinfo("Saved", "Credentials updated.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save credentials: {e}")

# Login modal
def show_login_modal():
    global login_successful
    login_successful = False
    L = tk.Toplevel(root)
    L.title("Admin Login")
    L.geometry("380x240")
    L.configure(bg="#22313f")
    L.resizable(False, False)
    L.grab_set()
    x = root.winfo_x() + (root.winfo_width() // 2) - 190
    y = root.winfo_y() + (root.winfo_height() // 2) - 120
    try: L.geometry(f"+{x}+{y}")
    except Exception: pass

    tk.Label(L, text="Admin Login", bg="#22313f", fg="white", font=("Segoe UI", 14, "bold")).pack(pady=(14,6))
    tk.Label(L, text="Enter your admin credentials to continue", bg="#22313f", fg="#c5d1d8", font=("Segoe UI",10)).pack()
    frm = tk.Frame(L, bg="#22313f")
    frm.pack(pady=12, padx=16, fill="x")
    tk.Label(frm, text="Username", bg="#22313f", fg="#cfe7ef", anchor="w").pack(fill="x")
    username = tk.Entry(frm, font=("Segoe UI", 11))
    username.pack(fill="x", pady=(2,8))
    tk.Label(frm, text="Password", bg="#22313f", fg="#cfe7ef", anchor="w").pack(fill="x")
    password = tk.Entry(frm, show="*", font=("Segoe UI", 11))
    password.pack(fill="x", pady=(2,8))
    creds_file = os.path.join(os.path.abspath("."), "credentials.txt")
    def read_saved_creds():
        user, pwd = "admin", "password"
        try:
            if os.path.exists(creds_file):
                with open(creds_file, "r", encoding="utf-8") as fh:
                    lines = fh.read().splitlines()
                    if len(lines) >= 2:
                        user = lines[0].strip()
                        pwd = lines[1].strip()
        except Exception: pass
        return user, pwd
    def try_login():
        nonlocal L
        global login_successful
        u = username.get().strip()
        p = password.get().strip()
        saved_user, saved_pass = read_saved_creds()
        if u == saved_user and p == saved_pass:
            login_successful = True
            append_log("[launcher] Admin logged in successfully.\n")
            L.destroy()
            show_admin_controls()
        else:
            messagebox.showerror("Login failed", "Incorrect username or password")
    btn_frame = tk.Frame(L, bg="#22313f")
    btn_frame.pack(pady=(2,12))
    login_btn = tk.Button(btn_frame, text="Login", command=try_login, bg="#2ecc71", fg="#0b1a0b", font=("Segoe UI",11,"bold"), bd=0, padx=12, pady=6)
    login_btn.pack(side="left", padx=8)
    cancel_btn = tk.Button(btn_frame, text="Cancel", command=lambda: L.destroy() if login_successful else root.destroy(), bg="#95a5a6", fg="white", bd=0, padx=12, pady=6)
    cancel_btn.pack(side="left", padx=8)
    def on_close():
        if login_successful: L.destroy()
        else: root.destroy()
    L.protocol("WM_DELETE_WINDOW", on_close)
    username.focus_set()
    root.wait_window(L)

# Theme
def toggle_theme():
    global THEME
    THEME = "dark" if THEME=="light" else "light"
    bg = "#1c1c1c" if THEME=="dark" else "#eafaf1"
    fg = "#f0f0f0" if THEME=="dark" else "#2c3e50"
    main.config(bg=bg)
    status_label.config(bg=bg, fg=fg)
    ip_row.config(bg=bg)
    for lbl in ip_row.winfo_children(): lbl.config(bg=bg, fg=fg)
    statusbar.config(bg=bg)
    for lbl in statusbar.winfo_children(): lbl.config(bg=bg, fg=fg)

# System monitor
def update_system_monitor():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    sysmon_label.config(text=f"CPU: {cpu}%   RAM: {ram}%")
    root.after(1000, update_system_monitor)

# UI Building 
def make_ui(root):
    global main, status_indicator, status_label, ip_row, statusbar, log_frame, log_text
    global start_btn, stop_btn, restart_btn, log_toggle_btn, admin_frame, sysmon_label

    root.title(APP_NAME)
    root.geometry("920x720")
    root.minsize(920, 620)
    try:
        if os.path.exists(LOGO_PATH):
            img = tk.PhotoImage(file=LOGO_PATH)
            root.iconphoto(False, img)
    except Exception as e:
        append_log(f"[launcher] Warning: failed to set icon: {e}\n")

    sidebar = tk.Frame(root, width=240, bg="#0f3d2e")
    sidebar.pack(side="left", fill="y")
    main = tk.Frame(root, bg="#eafaf1")
    main.pack(side="right", expand=True, fill="both")

    # Sidebar buttons
    def make_sidebar_btn(text, command):
        b = tk.Button(sidebar, text=text, command=command, anchor="w", padx=18, bd=0, bg="#0f3d2e", fg="white", activebackground="#145a32", font=("Segoe UI",11))
        b.pack(fill="x", pady=6)
        b.bind("<Enter>", lambda e: b.config(bg="#145a32"))
        b.bind("<Leave>", lambda e: b.config(bg="#0f3d2e"))
        return b

    make_sidebar_btn("Start Server", start_server_action)
    make_sidebar_btn("Stop Server", stop_server_action)
    make_sidebar_btn("Restart Server", restart_server_action)
    make_sidebar_btn("Open Admin Dashboard", open_admin_in_browser)
    make_sidebar_btn("Open QR Attendance", open_qr_in_browser)
    make_sidebar_btn("Change Admin Credentials", change_credentials_action)
    make_sidebar_btn("Toggle Log", toggle_log_panel)
    make_sidebar_btn("Export Log", export_log_action)
    make_sidebar_btn("Toggle Theme", toggle_theme)

    # Header
    header = tk.Frame(main, bg="#eafaf1", pady=12)
    header.pack(fill="x")
    status_indicator = tk.Label(header, bg="#c0392b", width=2, height=1)
    status_indicator.pack(side="left", padx=(10,6))
    status_label = tk.Label(header, text="Server status: Stopped", bg="#eafaf1", fg="#2c3e50", font=("Segoe UI",12,"bold"))
    status_label.pack(side="left")

    # IP row
    local_ip, lan_ip = get_local_and_lan_ip()
    ip_row = tk.Frame(main, bg="#eafaf1")
    ip_row.pack(fill="x", padx=18, pady=(6,0))
    tk.Label(ip_row, text=f"Local: 127.0.0.1    LAN: {lan_ip}", bg="#eafaf1", fg="#576d63", font=("Segoe UI",10)).pack(anchor="w")

    # Server card and admin panel
    left_col = tk.Frame(main, bg="#eafaf1")
    left_col.pack(side="left", fill="both", expand=True)

    # Server Controls Card
    server_card = tk.Frame(left_col, bg="white", bd=0, relief="raised", padx=12, pady=12)
    server_card.pack(fill="x", pady=8)
    tk.Label(server_card, text="Server Controls", bg="white", font=("Segoe UI",12,"bold")).pack(anchor="w")

    sc_buttons = tk.Frame(server_card, bg="white")
    sc_buttons.pack(pady=10, anchor="w")
    start_btn = tk.Button(sc_buttons, text="Start", width=10, command=start_server_action,
                          bg="#2ecc71", fg="#0b2f1a", font=("Segoe UI",11,"bold"), bd=0)
    start_btn.grid(row=0, column=0, padx=6, pady=4)
    stop_btn = tk.Button(sc_buttons, text="Stop", width=10, command=stop_server_action,
                         bg="#e74c3c", fg="white", font=("Segoe UI",11,"bold"), bd=0, state="disabled")
    stop_btn.grid(row=0, column=1, padx=6, pady=4)
    restart_btn = tk.Button(sc_buttons, text="Restart", width=10, command=restart_server_action,
                            bg="#f39c12", fg="white", font=("Segoe UI",11,"bold"), bd=0, state="disabled")
    restart_btn.grid(row=0, column=2, padx=6, pady=4)

    # Admin Panel
    admin_frame = tk.Frame(left_col, bg="white")
    tk.Label(admin_frame, text="Admin Controls", bg="white", font=("Segoe UI",12,"bold")).pack(anchor="w")
    admin_links = tk.Frame(admin_frame, bg="white")
    admin_links.pack(pady=10, anchor="w")
    tk.Button(admin_links, text="Open Admin Dashboard", command=open_admin_in_browser,
              bg="#0f3d2e", fg="white", bd=0, padx=10).pack(side="left", padx=6)
    tk.Button(admin_links, text="Open QR Page", command=open_qr_in_browser,
              bg="#0f3d2e", fg="white", bd=0, padx=10).pack(side="left", padx=6)

    # Right column for log and system monitor
    right_col = tk.Frame(main, bg="#eafaf1", width=320)
    right_col.pack(side="right", fill="y")

    # Log area
    right_top = tk.Frame(right_col, bg="#eafaf1")
    right_top.pack(fill="both", pady=(0,8))
    tk.Label(right_top, text="Activity Log", bg="#eafaf1", font=("Segoe UI",11,"bold")).pack(anchor="w")
    log_frame = tk.Frame(right_top, bg="#ffffff", bd=1, relief="sunken")
    log_frame.pack(fill="both", pady=6)
    log_text = scrolledtext.ScrolledText(log_frame, height=20, width=40, bg="#0b3b2e", fg="#e6f8ee", font=("Consolas",10))
    log_text.pack(fill="both", expand=True)
    log_text.configure(state="disabled")

    log_toggle_btn = tk.Button(right_col, text="Show Log", command=toggle_log_panel, bg="#145a32", fg="white", bd=0, padx=10, pady=6)
    log_toggle_btn.pack(pady=8)

    # System monitor
    sysmon_frame = tk.Frame(right_col, bg="#eafaf1")
    sysmon_frame.pack(pady=12, fill="x")
    tk.Label(sysmon_frame, text="System Monitor", bg="#eafaf1", font=("Segoe UI",11,"bold")).pack(anchor="w")
    sysmon_label = tk.Label(sysmon_frame, text="CPU: 0%   RAM: 0%", bg="#eafaf1", fg="#2c3e50", font=("Segoe UI",10))
    sysmon_label.pack(anchor="w", pady=2)
    update_system_monitor()  # start updating CPU/RAM usage

    # Status bar at bottom
    statusbar = tk.Frame(main, bg="#dfeee7")
    statusbar.pack(fill="x", side="bottom")
    tk.Label(statusbar, text="Ready", bg="#dfeee7", fg="#2f4f45", font=("Segoe UI",9)).pack(side="left", padx=8, pady=6)

    # Initially hide admin controls until login
    hide_admin_controls()

# ----------------- App entrypoint -----------------
if __name__ == "__main__":
    root = tk.Tk()
    make_ui(root)
    # show login modal first; if user cancels or fails, app will quit
    root.after(150, show_login_modal)

    # Define the function to handle app close
    def on_app_close():
        stop_server_action() 
        root.destroy()       

    # Register the close handler
    root.protocol("WM_DELETE_WINDOW", on_app_close)

    root.mainloop()
