# devices = [
#     {"name": "DoorProtect", "price": 20, "centrals": {"hub", "hub+"}},
#     {"name": "MotionProtect", "price": 40, "centrals": {"hub", "hub2+"}},
#     {"name": "FireProtect", "price": 60, "centrals": {"hub+", "hub2", "hub2+"}},
#     {"name": "DoorProtectPlus", "price": 45, "centrals": {"hub", "hub+", "hub2"}},
#     {"name": "Socket", "price": 30, "centrals": {"hub", "hub2"}}
# ]
#
# devices_hub = {}
#
# for device in devices:
#     if device["centrals"] == {"hub+"} and device["price"] >= 40:
#         continue
#
# devices_hub.update(device)
# print(devices_hub)
from typing import Dict

import a as a

# devices = [
#     {"name": "DoorProtect"},
#     {"name": "MotionProtect"},
#     {"name": "FireProtect"},
#     {"name": "DoorProtectPlus"},
#     {"name": "Socket"},
# ]
#
# for device in devices:
#     name = device.values()
# print(name)

#
# name = ['Jon', 'Leonard', 'Vova']
# age = [12, 18, 30]
#
#
# result = dict(zip(name, age))
#
# print(result)

name = ['Jon', 'Leonard', 'Vova']
age = [12, 18, 30]

new_list = {name[i]: age[i] for i in range(len(name))}

print(new_list)