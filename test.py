devices = [
    {"name": "DoorProtect"},
    {"name": "MotionProtect"},
    {"name": "FireProtect"},
    {"name": "DoorProtectPlus"},
    {"name": "Socket"},
]

new_list = []
for device in devices:
    new_list.append(device['name'])

print(new_list)

# for device in devices:
#   continue
#
# name  = []
# name.append(device.values())
#
# print(name)