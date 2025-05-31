import tkinter as tk
import subprocess

def launch_network_scanner():
    subprocess.Popen(["python3", "tools/network_scanner/gui.py"])

def launch_ip_config():
    subprocess.Popen(["python3", "tools/ip_config/ip_config_gui.py"])

root = tk.Tk()
root.title("BAS-Brick Launcher")
root.geometry("320x240")
root.configure(bg="black")

tk.Label(root, text="BAS-Brick Tools", font=("Helvetica", 16), bg="black", fg="white").pack(pady=10)

tk.Button(root, text="Network Scanner", font=("Helvetica", 12), width=20, height=2, command=launch_network_scanner).pack(pady=5)
tk.Button(root, text="Set Static IP", font=("Helvetica", 12), width=20, height=2, command=launch_ip_config).pack(pady=5)
tk.Button(root, text="Exit", font=("Helvetica", 12), width=20, height=2, command=root.quit).pack(pady=5)

root.mainloop()
