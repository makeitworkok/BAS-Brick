import tkinter as tk
import subprocess

def launch_network_scanner():
    subprocess.Popen(["python3", "tools/network_scanner/gui.py"])

def shutdown_pi():
    subprocess.call(["sudo", "shutdown", "now"])

root = tk.Tk()
root.title("BAS-Brick Toolbox")
root.geometry("320x240")
root.configure(bg="black")

title = tk.Label(root, text="BAS-Brick", font=("Helvetica", 20, "bold"), fg="white", bg="black")
title.pack(pady=20)

btn1 = tk.Button(root, text="Network Scanner", font=("Helvetica", 14), width=25, height=2, command=launch_network_scanner)
btn1.pack(pady=10)

shutdown_btn = tk.Button(root, text="Shutdown", font=("Helvetica", 12), width=25, height=2, command=shutdown_pi)
shutdown_btn.pack(pady=20)

root.mainloop()