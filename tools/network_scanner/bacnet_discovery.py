import BAC0

# Start a BACnet stack on your Pi's default interface
# You may change the IP here to match your wired interface if needed
bacnet = BAC0.lite()

# Perform a Who-Is to discover devices
devices = bacnet.whois()

# Print discovered devices
print("\nDiscovered BACnet Devices:")
for device in devices:
    print(f" - Address: {device.address}, ID: {device.device_id}, Name: {device.name}")