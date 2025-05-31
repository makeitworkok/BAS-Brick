from bacpypes3.core import run, stop
from bacpypes3.app import BIPSimpleApplication
from bacpypes3.local.device import DeviceObject
from bacpypes3.primitivedata import Unsigned, ObjectIdentifier, CharacterString
from bacpypes3.apdu import WhoIsRequest, ReadPropertyRequest
from bacpypes3.pdu import Address
from bacpypes3.service.device import WhoIsIAmServices
import csv
from datetime import datetime
import os

SCAN_PATH = "/home/pi/network_scans"

class BACnetScanner(BIPSimpleApplication, WhoIsIAmServices):
    def __init__(self, device, address):
        super().__init__(device, address)
        self.devices = {}

    def indication(self, apdu):
        super().indication(apdu)

    def confirmation(self, apdu):
        if hasattr(apdu, 'apduType') and apdu.apduType == "IAm":
            self.devices[apdu.iAmDeviceIdentifier[1]] = {
                "device_id": apdu.iAmDeviceIdentifier[1],
                "address": str(apdu.pduSource)
            }

def scan_bacnet():
    this_device = DeviceObject(
        objectIdentifier=('device', 599),
        objectName='BAS-Brick',
        maxApduLengthAccepted=1024,
        segmentationSupported='noSegmentation',
        vendorIdentifier=15
    )

    scanner = BACnetScanner(this_device, "0.0.0.0")

    # Send Who-Is broadcast
    request = WhoIsRequest()
    request.pduDestination = Address("255.255.255.255")
    scanner.request(request)

    run(timeout=5)  # Listen for 5 seconds
    stop()

    results = []
    for device_id, info in scanner.devices.items():
        results.append((device_id, info["address"]))

    return results

def write_csv(results):
    os.makedirs(SCAN_PATH, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(SCAN_PATH, f"bacnet_discovery_{ts}.csv")
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Device ID", "IP Address"])
        for device_id, ip in results:
            writer.writerow([device_id, ip])
    print(f"[+] Results saved to {file_path}")

if __name__ == "__main__":
    devices = scan_bacnet()
    write_csv(devices)
    print(f"[+] {len(devices)} BACnet device(s) discovered.")
