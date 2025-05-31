import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import time
import threading

CONFIG_FILE = "tools/network_scanner/config.json"

DEFAULT_IP = [10, 46, 12, 2]

class IPConfigurator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Set Static IP (eth0)")
        self.geometry("320x240")
        self.octets = DEFAULT_IP.copy()
        self.buttons = []
        self.hold_thread = None
        self.holding = False
        self.hold_delay = 0.5

        self.build_gui()

    def build_gui(self):
        tk.Label(self, text="Static IP for eth0:", font=("Arial", 12)).pack(pady=5)

        frame = tk.Frame(self)
        frame.pack()

        self.labels = []
        for i in range(4):
            octet_frame = tk.Frame(frame)
            octet_frame.pack(side=tk.LEFT, padx=5)

            btn_up = tk.Button(octet_frame, text="▲", repeatdelay=200, repeatinterval=100)
            btn_up.pack()
            btn_up.bind("<ButtonPress-1>", lambda e, i=i: self.start_hold(i, 1))
            btn_up.bind("<ButtonRelease-1>", lambda e: self.stop_hold())

            lbl = tk.Label(octet_frame, text=str(self.octets[i]), font=("Arial", 14))
            lbl.pack()
            self.labels.append(lbl)

            btn_down = tk.Button(octet_frame, text="▼")
            btn_down.pack()
            btn_down.bind("<ButtonPress-1>", lambda e, i=i: self.start_hold(i, -1))
            btn_down.bind("<ButtonRelease-1>", lambda e: self.stop_hold())

        tk.Button(self, text="Apply", command=self.apply_ip).pack(pady=10)

    def update_octet(self, index, delta):
        self.octets[index] = (self.octets[index] + delta) % 256
        self.labels[index].config(text=str(self.octets[index]))

    def start_hold(self, index, delta):
        self.holding = True
        def hold():
            delay = self.hold_delay
            while self.holding:
                self.update_octet(index, delta)
                time.sleep(delay)
                delay = max(0.05, delay * 0.75)  # Accelerate
        self.hold_thread = threading.Thread(target=hold)
        self.hold_thread.start()

    def stop_hold(self):
        self.holding = False
        if self.hold_thread:
            self.hold_thread.join()
            self.hold_thread = None

    def apply_ip(self):
        ip = ".".join(str(o) for o in self.octets)
        gateway = ".".join(str(o) for o in self.octets[:3] + [1])
        try:
            subprocess.run(["nmcli", "connection", "modify", "eth0-static",
                            "ipv4.addresses", f"{ip}/24",
                            "ipv4.gateway", gateway,
                            "ipv4.method", "manual"], check=True)
            subprocess.run(["nmcli", "connection", "up", "eth0-static"], check=True)
            self.update_config(ip)
            messagebox.showinfo("Success", f"IP set to {ip}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to apply IP")

    def update_config(self, ip):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        config["ip_address"] = ip
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)

if __name__ == "__main__":
    app = IPConfigurator()
    app.mainloop()
