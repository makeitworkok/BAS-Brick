# BAS-Brick

**BAS-Brick** is a modular, field-ready toolkit designed to run on a Raspberry Pi 5 with a touchscreen interface. It is intended for Building Automation System (BAS) professionals who need portable, easy-to-use tools for diagnostics, discovery, and troubleshooting in the field.

This project is designed with non-technical users in mind: large buttons, simple navigation, and automated functions — all accessible via a 3.5" touchscreen display (or HDMI monitor during development).

---

## 🔧 Current Toolset

### 🛠️ Tool 1: Network Scanner
- Scans a known subnet (e.g., `10.46.12.0/24`)
- Records all discovered IP and MAC addresses
- Saves logs to timestamped `.csv` files
- Optional USB copy support (in progress)
- View logs directly on-screen

---

## 📐 Project Structure

```plaintext
BAS-Brick/
├── bas_brick_launcher.py       # Main touchscreen launcher GUI
├── tools/
│   └── network_scanner/
│       ├── gui.py              # GUI for the network scanner
│       ├── scanner.py          # Core scanning logic (currently mocked)
│       └── config.json         # Subnet and IP configuration
├── shared/
│   └── utils.py                # Shared functions for future tools
├── assets/
│   └── bas_brick_logo.png      # (Optional) branding
