devices = "DoorProtect DoorProtect MotionProtect MotionProtect FireProtect FireProtectPlus FireProtect DoorProtect"

devices_list = devices.split()
device_dict = {}

for device in devices_list:
     if device not in device_dict:
        device_dict[device] = 1
     else:
        device_dict[device] = device_dict[device] + 1

print(device_dict)

