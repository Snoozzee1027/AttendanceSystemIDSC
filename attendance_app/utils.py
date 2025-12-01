import sqlite3
from datetime import datetime
import qrcode
import base64
from io import BytesIO
import os
import pandas as pd

# Requires qr
try:
    from PIL import Image
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image

# For QR fix
from qrcode.image.pil import PilImage  

DB_FILE = "attendance.db"

# Initialize DB and tables
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Add id as PRIMARY KEY for devices to match admin queries
    c.execute('''CREATE TABLE IF NOT EXISTS devices (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     device_id TEXT UNIQUE,
                     name TEXT,
                     student_number TEXT
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     student_number TEXT,
                     device_id TEXT,
                     date TEXT,
                     time TEXT
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS tokens (
                     token TEXT PRIMARY KEY,
                     expiry TEXT
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS admin (
                     id INTEGER PRIMARY KEY,
                     username TEXT,
                     password TEXT
                 )''')
    
    # Default admin credentials
    c.execute("INSERT OR IGNORE INTO admin (id, username, password) VALUES (1, 'admin', 'password')")
    
    conn.commit()
    conn.close()


# Generate QR as base64
def make_qr_base64(url):
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=PilImage)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_b64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_b64}"


# Export attendance to Excel (optional date filter)
def create_excel(start=None, end=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    query = "SELECT name, student_number, device_id, date, time FROM attendance"
    params = ()
    if start and end:
        query += " WHERE date BETWEEN ? AND ?"
        params = (start, end)
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    df = pd.DataFrame(rows, columns=["Name", "Student Number", "Device ID", "Date", "Time"])
    out_file = "attendance_export.xlsx"
    df.to_excel(out_file, index=False)
    return out_file


# Get local IP for QR generation
def get_local_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip
