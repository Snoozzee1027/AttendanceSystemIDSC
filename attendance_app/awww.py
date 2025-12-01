# this is wala na
import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage, ttk
import subprocess, threading, os, sys, socket, time, requests, shutil
import platform

# ----------------- Configuration -----------------
FLASK_PORT = 5000
server_process = None
server_running = False
log_visible = False

# ----------------- Utility Functions -----------------
def get_ips():
    """Return local and network IP"""
    local_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        network_ip = s.getsockname()[0]
        s.close()
    except:
        network_ip = "Unavailable"
    return local_ip, network_ip

def wait_for_server(timeout=15):
    url = f"http://127.0.0.1:{FLASK_PORT}/"
    start_time = time.time()
    while True:
        try:
            requests.get(url)
            return True
        except:
            if time.time() - start_time > timeout:
                return False
            time.sleep(0.5)

# ----------------- Server Functions -----------------
def stream_logs():
    global server_process, server_running
    while server_running and server_process and server_process.stdout:
        line = server_process.stdout.readline()
        if not line:
            break
        log_text.insert(tk.END, line)
        log_text.see(tk.END)
    server_running = False

# ----------------- Find app.py Systemwide -----------------
def find_app_py_systemwide():
    """Search common user folders and C:\ for app.py, skipping system folders"""
    search_roots = []
    home = os.path.expanduser("~")
    for folder in ["Desktop", "Documents", "Downloads"]:
        search_roots.append(os.path.join(home, folder))
    search_roots.append("C:\\")
    if platform.system() != "Windows":
        search_roots.append(home)

    for root in search_roots:
        for dirpath, dirnames, filenames in os.walk(root):
            skip_dirs = ["venv", "Lib", "site-packages", "__pycache__", ".git", "node_modules"]
            if any(sd in dirpath for sd in skip_dirs):
                continue
            if "app.py" in filenames:
                return os.path.join(dirpath, "app.py")
    return None

# ----------------- Start / Stop Server -----------------
def start_server():
    global server_process, server_running
    if server_running:
        messagebox.showinfo("Server", "Server is already running.")
        return

    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, "[INFO] Searching for app.py on your system...\n")

    app_path = find_app_py_systemwide()
    if not app_path:
        messagebox.showerror("Error", "Could not find app.py anywhere on your system!")
        return

    log_text.insert(tk.END, f"[INFO] Found app.py at: {app_path}\n")
    app_dir = os.path.dirname(app_path)
    venv_python = os.path.join(app_dir, "venv", "Scripts", "python.exe")
    python_exec = venv_python if os.path.exists(venv_python) else shutil.which("python") or sys.executable
    log_text.insert(tk.END, f"[INFO] Using Python executable: {python_exec}\n")

    try:
        creation_flags = 0
        if os.name == "nt":
            creation_flags = subprocess.CREATE_NO_WINDOW

        server_process = subprocess.Popen(
            [python_exec, app_path],
            cwd=app_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            creationflags=creation_flags
        )
        server_running = True
        threading.Thread(target=stream_logs, daemon=True).start()
        threading.Thread(target=wait_for_server_ready, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start server:\n{e}")

def wait_for_server_ready():
    if wait_for_server():
        status_label.config(text="Server is running!")
        start_btn.config(state="disabled")
        stop_btn.config(state="normal")
        restart_btn.config(state="normal")
        show_admin_controls()
    else:
        status_label.config(text="Server failed to start.")

def stop_server():
    global server_process, server_running
    if server_process:
        server_running = False
        server_process.terminate()
        server_process = None
        log_text.insert(tk.END, "\n[INFO] Server stopped.\n")
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")
    restart_btn.config(state="disabled")
    hide_admin_controls()

def restart_server():
    stop_server()
    time.sleep(1)
    start_server()

# ----------------- Admin / QR -----------------
def get_accessible_url(path):
    """Try localhost first, fallback to LAN IP"""
    localhost_url = f"http://127.0.0.1:{FLASK_PORT}{path}"
    try:
        requests.get(localhost_url, timeout=1)
        return localhost_url
    except:
        _, lan_ip = get_ips()
        return f"http://{lan_ip}:{FLASK_PORT}{path}"

def open_admin():
    url = get_accessible_url("/admin")
    os.startfile(url)

def open_qr():
    url = get_accessible_url("/")
    os.startfile(url)

def show_admin_controls():
    admin_btn.pack(pady=5, fill="x")
    qr_btn.pack(pady=5, fill="x")
    creds_btn.pack(pady=5, fill="x")

def hide_admin_controls():
    admin_btn.pack_forget()
    qr_btn.pack_forget()
    creds_btn.pack_forget()

def toggle_log():
    global log_visible
    if log_visible:
        log_frame.pack_forget()
        log_visible = False
        log_btn.config(text="View Log")
    else:
        log_frame.pack(fill="both", expand=True, pady=5)
        log_visible = True
        log_btn.config(text="Hide Log")

def change_credentials():
    new_user = simpledialog.askstring("Change Username", "Enter new admin username:")
    if not new_user: return
    new_pass = simpledialog.askstring("Change Password", "Enter new admin password:", show="*")
    if not new_pass: return
    creds_path = "credentials.txt"
    try:
        with open(creds_path, "w") as f:
            f.write(f"{new_user}\n{new_pass}")
        messagebox.showinfo("Success", "Credentials updated successfully!")
    except:
        messagebox.showerror("Error", "Failed to write credentials file.")

# ----------------- Login -----------------
def prompt_login():
    login_win = tk.Toplevel(root)
    login_win.title("Admin Login")
    login_win.geometry("300x180")
    login_win.resizable(False, False)
    login_win.grab_set()

    tk.Label(login_win, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_win)
    username_entry.pack(pady=5)
    tk.Label(login_win, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack(pady=5)

    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        saved_user, saved_pass = "admin", "password"
        creds_path = "credentials.txt"
        if os.path.exists(creds_path):
            with open(creds_path) as f:
                saved_user = f.readline().strip()
                saved_pass = f.readline().strip()
        if username == saved_user and password == saved_pass:
            messagebox.showinfo("Login", "Login successful!")
            login_win.destroy()
            show_admin_controls()
            return
        messagebox.showerror("Login Failed", "Incorrect username or password")

    tk.Button(login_win, text="Login", command=check_login, width=15).pack(pady=10)

# ----------------- Main GUI (Modern) -----------------
root = tk.Tk()
root.title("Attendance System Launcher")
root.geometry("550x700")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# ----------------- Modern Logo -----------------
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(BASE_DIR, "static", "logo.png")
if os.path.exists(logo_path):
    logo_img = PhotoImage(file=logo_path)
    tk.Label(root, image=logo_img, bg="#1e1e2f").pack(pady=20)

# Status
status_label = tk.Label(root, text="Server status: Stopped", font=("Segoe UI", 12), bg="#1e1e2f", fg="white")
status_label.pack(pady=5)

# IP Info
local_ip, network_ip = get_ips()
ip_label = tk.Label(root, text=f"Local IP: {local_ip} | Network IP: {network_ip}", font=("Segoe UI", 10), bg="#1e1e2f", fg="white")
ip_label.pack(pady=5)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

btn_style = {"font": ("Segoe UI", 10), "bg": "#4b4b6b", "fg": "white", "activebackground": "#6c6c8f", "width": 18, "bd": 0}

start_btn = tk.Button(frame, text="Start Server", command=start_server, **btn_style)
start_btn.grid(row=0, column=0, padx=5, pady=5)
stop_btn = tk.Button(frame, text="Stop Server", command=stop_server, state="disabled", **btn_style)
stop_btn.grid(row=0, column=1, padx=5, pady=5)
restart_btn = tk.Button(frame, text="Restart Server", command=restart_server, state="disabled", **btn_style)
restart_btn.grid(row=0, column=2, padx=5, pady=5)

# Hidden admin controls
admin_btn = tk.Button(root, text="Open Admin Dashboard", command=open_admin, **btn_style)
qr_btn = tk.Button(root, text="Open QR Attendance", command=open_qr, **btn_style)
creds_btn = tk.Button(root, text="Change Admin Credentials", command=change_credentials, **btn_style)

# Log frame
log_frame = tk.Frame(root, bg="#2c2c44")
log_text = tk.Text(log_frame, height=15, width=65, bg="#2c2c44", fg="white")
log_text.pack(fill="both", expand=True)
log_btn = tk.Button(root, text="View Log", command=toggle_log, **btn_style)
log_btn.pack(pady=5)

# Show login at start
root.after(100, prompt_login)
root.protocol("WM_DELETE_WINDOW", lambda: [stop_server(), root.destroy()])
root.mainloop()
