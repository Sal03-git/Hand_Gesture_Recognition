import asyncio
from bleak import BleakScanner, BleakClient

async def discover_devices():
    # Discover nearby BLE devices
    devices = await BleakScanner.discover()

    print("Discovered devices:")
    for device in devices:
        print(f"Device name: {device.name}, Address: {device.address}")

    return devices

async def connect_to_device(device_address):
    async with BleakClient(device_address) as client:
        print(f"Connecting to {device_address}...")

        # Check if connected
        if client.is_connected:
            print(f"Successfully connected to {device_address}")
            
            # Replace with the actual UUID you provided
            characteristic_uuid = "000000ff-0000-1000-8000-00805f9b34fb"  # This is your UUID
            data = bytearray([0x01, 0x02, 0x03])  # Replace with actual data

            # Example: Writing data to the characteristic
            await client.write_gatt_char(characteristic_uuid, data)
            print(f"Sent data: {data}")
            
            # Optionally, you can also read from the characteristic
            # data_received = await client.read_gatt_char(characteristic_uuid)
            # print(f"Received data: {data_received}")

        else:
            print(f"Failed to connect to {device_address}")

# Main function to run discovery and connect
async def main():
    # Discover devices
    devices = await discover_devices()

    # Find the device you want to connect to by address
    device_address = None
    for device in devices:
        if device.address == "9C:9E:6E:85:C7:5A":
            device_address = device.address
            break
    
    # Connect to the device if found
    if device_address:
        await connect_to_device(device_address)
    else:
        print("Device not found!")

# Run the main function
asyncio.run(main())