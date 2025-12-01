from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify, send_file, flash
import sqlite3
from datetime import datetime, timedelta
import uuid
import os
from functools import wraps
from utils import init_db, DB_FILE, make_qr_base64, create_excel, get_local_ip

# Added for logging + restart
import subprocess
import threading
import sys
import time

# --- Initialize database ---
init_db()

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_string"

# --- QR / attendance settings ---
QR_VALID_HOURS = 2
QR_AUTO_REFRESH_SECONDS = 30

# --- PyInstaller safe base path ---
if getattr(sys, "_MEIPASS", None):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.abspath(".")

# --- Database helper ---
def db_conn():
    return sqlite3.connect(DB_FILE)

# --- Admin login decorator ---
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated

# --- Token helpers ---
def create_token(hours=QR_VALID_HOURS):
    token = str(uuid.uuid4())
    expiry = (datetime.now() + timedelta(hours=hours)).isoformat()
    conn = db_conn(); c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO tokens (token, expiry) VALUES (?, ?)", (token, expiry))
    conn.commit(); conn.close()
    return token, expiry

def token_valid(token):
    conn = db_conn(); c = conn.cursor()
    c.execute("SELECT expiry FROM tokens WHERE token=?", (token,))
    row = c.fetchone(); conn.close()
    if not row: return False
    expiry = datetime.fromisoformat(row[0])
    return datetime.now() <= expiry

# --- QR page ---
@app.route("/")
def index():
    token, expiry = create_token()
    ip = get_local_ip()
    port = 5000  # fixed port
    qr_url = f"http://{ip}:{port}/attend?token={token}"
    qr_base64 = make_qr_base64(qr_url)
    return render_template("index.html", qr_base64=qr_base64, qr_value=qr_url,
                           token=token, expiry=expiry, refresh_seconds=QR_AUTO_REFRESH_SECONDS)

@app.route("/qr")
def qr_endpoint():
    token, expiry = create_token()
    ip = get_local_ip()
    port = 5000  # fixed port
    qr_url = f"http://{ip}:{port}/attend?token={token}"
    qr_base64 = make_qr_base64(qr_url)
    return jsonify({"token": token, "qr_value": qr_url, "qr_base64": qr_base64, "expiry": expiry})

# --- Attend / Register ---
@app.route("/attend", methods=["GET","POST"])
def attend():
    token = request.args.get("token") or request.form.get("token")
    if not token or not token_valid(token):
        return render_template("thankyou.html", name="", message="This QR has expired. Please refresh the main page.")
    
    device_id = request.cookies.get("device_id")
    conn = db_conn(); c = conn.cursor()

    if request.method == "POST":
        name = request.form.get("name")
        student_number = request.form.get("student_number")
        if not device_id:
            device_id = str(uuid.uuid4())
        c.execute("INSERT OR REPLACE INTO devices (device_id, name, student_number) VALUES (?,?,?)",
                  (device_id, name, student_number))
        
        today = datetime.now().strftime("%Y-%m-%d")
        c.execute("SELECT id FROM attendance WHERE device_id=? AND date=?", (device_id, today))
        if c.fetchone():
            conn.commit(); conn.close()
            resp = make_response(render_template("thankyou.html", name=name, message="Already timed in today."))
            resp.set_cookie("device_id", device_id, max_age=60*60*24*365)
            return resp
        
        now = datetime.now()
        c.execute("INSERT INTO attendance (name, student_number, device_id, date, time) VALUES (?,?,?,?,?)",
                  (name, student_number, device_id, today, now.strftime("%H:%M:%S")))
        conn.commit(); conn.close()
        resp = make_response(render_template("thankyou.html", name=name, message="Attendance recorded. Thank you!"))
        resp.set_cookie("device_id", device_id, max_age=60*60*24*365)
        return resp

    # GET flow
    c.execute("SELECT name, student_number FROM devices WHERE device_id=?", (device_id,))
    dev = c.fetchone()
    if not dev:
        conn.close()
        return render_template("register.html", token=token)
    
    # Auto-check-in
    name, student_number = dev
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT id FROM attendance WHERE device_id=? AND date=?", (device_id, today))
    if c.fetchone():
        conn.close()
        return render_template("thankyou.html", name=name, message="Attendance already recorded today.")
    
    now = datetime.now()
    c.execute("INSERT INTO attendance (name, student_number, device_id, date, time) VALUES (?,?,?,?,?)",
              (name, student_number, device_id, today, now.strftime("%H:%M:%S")))
    conn.commit(); conn.close()
    resp = make_response(render_template("thankyou.html", name=name, message="Attendance recorded. Thank you!"))
    if not request.cookies.get("device_id"):
        resp.set_cookie("device_id", device_id, max_age=60*60*24*365)
    return resp

# --- Admin ---
@app.route("/admin", methods=["GET","POST"])
def admin_login():
    error = None
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = db_conn(); c = conn.cursor()
        c.execute("SELECT id FROM admin WHERE username=? AND password=?", (username,password))
        if c.fetchone():
            session["admin_logged_in"] = True
            conn.close()
            return redirect(url_for("admin_dashboard"))
        conn.close()
        error = "Invalid credentials"
    return render_template("admin_login.html", error=error)

@app.route("/admin/dashboard")
@admin_required
def admin_dashboard():
    conn = db_conn(); c = conn.cursor()
    c.execute("SELECT * FROM attendance ORDER BY date DESC, time DESC")
    records = c.fetchall()
    c.execute("SELECT * FROM devices ORDER BY id DESC")
    devices = c.fetchall(); conn.close()
    return render_template("admin_dashboard.html", records=records, devices=devices)

@app.route("/admin/export")
@admin_required
def admin_export():
    start = request.args.get("start")
    end = request.args.get("end")
    out = create_excel(start, end)
    return send_file(out, as_attachment=True)

@app.route("/admin/clear")
@admin_required
def admin_clear():
    conn = db_conn(); c = conn.cursor()
    c.execute("DELETE FROM attendance")
    conn.commit(); conn.close()
    flash("Attendance cleared.")
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/change_credentials", methods=["GET","POST"])
@admin_required
def change_credentials():
    msg = None
    if request.method=="POST":
        new_user = request.form.get("username")
        new_pass = request.form.get("password")
        conn = db_conn(); c = conn.cursor()
        c.execute("UPDATE admin SET username=?, password=? WHERE id=1", (new_user,new_pass))
        conn.commit(); conn.close()
        msg = "Credentials updated"
    return render_template("change_credentials.html", message=msg)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin_login"))

@app.route("/admin/remove_device/<device_id>", methods=["POST"])
@admin_required
def admin_remove_device(device_id):
    conn = db_conn(); c = conn.cursor()
    c.execute("DELETE FROM devices WHERE device_id=?", (device_id,))
    c.execute("DELETE FROM attendance WHERE device_id=?", (device_id,))
    conn.commit(); conn.close()
    flash(f"Device {device_id} removed.")
    return redirect(url_for("admin_dashboard"))

#--- Added files and features ---

LOG_FILE = "server.log"

# --- Real-time log writing ---
def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
        f.flush()
    print(text, flush=True)

# --- Global server status ---
SERVER_STATUS = {"running": True}

@app.route("/server/status")
def server_status():
    return jsonify(SERVER_STATUS)

@app.route("/server/logs")
def server_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"logs": ""})
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    return jsonify({"logs": content})

@app.route("/server/restart")
def server_restart():
    SERVER_STATUS["running"] = False
    write_log("Server restart requested via panel.")
    threading.Thread(target=_delayed_restart, daemon=True).start()
    return jsonify({"status": "restarting"})

def _delayed_restart():
    time.sleep(1)
    python = sys.executable
    os.execv(python, [python] + sys.argv)


# Run Command
if __name__=="__main__":
    os.makedirs("static", exist_ok=True)

    write_log("Starting Flask attendance server...")
    write_log("Running on: " + get_local_ip())

    app.run(host="0.0.0.0", port=5000, debug=True)
