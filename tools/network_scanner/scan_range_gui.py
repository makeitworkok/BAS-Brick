import tkinter as tk
from tkinter import messagebox
import json
import threading
import time

CONFIG_FILE = "tools/network_scanner/config.json"

DEFAULT_SCAN_RANGE = [10, 46, 12, 0]

class ScanRangeConfigurator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Set Scan Range")
        self.geometry("320x240")
        self.octets = DEFAULT_SCAN_RANGE.copy()
        self.labels = []
        self.holding = False
        self.hold_thread = None
        self.hold_delay = 0.5
        self.build_gui()

    def build_gui(self):
        tk.Label(self, text="Scan Range Base (e.g., 10.46.12.0/24):", font=("Arial", 10)).pack(pady=5)

        frame = tk.Frame(self)
        frame.pack()

        for i in range(4):
            octet_frame = tk.Frame(frame)
            octet_frame.pack(side=tk.LEFT, padx=5)

            btn_up = tk.Button(octet_frame, text="▲")
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

        tk.Button(self, text="Apply", command=self.apply_range).pack(pady=10)

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
                delay = max(0.05, delay * 0.75)
        self.hold_thread = threading.Thread(target=hold)
        self.hold_thread.start()

    def stop_hold(self):
        self.holding = False
        if self.hold_thread:
            self.hold_thread.join()
            self.hold_thread = None

    def apply_range(self):
        scan_range = ".".join(str(o) for o in self.octets) + "/24"
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            config["scan_range"] = scan_range
            with open(CONFIG_FILE, "w") as f:
                json.dump(config, f, indent=2)
            messagebox.showinfo("Success", f"Scan range set to {scan_range}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ScanRangeConfigurator()
    app.mainloop()
