import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import json
import os

CONFIG_FILE = "tools/network_scanner/config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {"scan_range": "10.46.12.0/24", "output_path": "/home/pi/network_scans"}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def start_scan():
    subprocess.Popen(["python3", "tools/network_scanner/scanner.py"])

def view_logs():
    subprocess.Popen(["xdg-open", config.get("output_path", "/home/pi/network_scans")])

def set_scan_range():
    new_range = simpledialog.askstring("Set Scan Range", "Enter scan range (CIDR):", initialvalue=config.get("scan_range", "10.46.12.0/24"))
    if new_range:
        config["scan_range"] = new_range
        save_config(config)
        messagebox.showinfo("Updated", f"Scan range set to: {new_range}")

config = load_config()
root = tk.Tk()
root.title("Network Scanner")
root.geometry("320x240")
root.configure(bg="black")
root.lift()  # Bring the window to the front

tk.Label(root, text="Network Scanner", font=("Helvetica", 14), bg="black", fg="white").pack(pady=10)

tk.Button(root, text="Start Scan", font=("Helvetica", 12), command=start_scan).pack(pady=5)
tk.Button(root, text="Set Scan Range", font=("Helvetica", 12), command=set_scan_range).pack(pady=5)
tk.Button(root, text="View Logs", font=("Helvetica", 12), command=view_logs).pack(pady=5)
tk.Button(root, text="Back", font=("Helvetica", 12), command=root.quit).pack(pady=5)

root.mainloop()