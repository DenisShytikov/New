devices = [
    {"name": "DoorProtect", "price": 20, "centrals": {"hub", "hub+"}},
    {"name": "MotionProtect", "price": 40, "centrals": {"hub", "hub2+"}},
    {"name": "FireProtect", "price": 60, "centrals": {"hub+", "hub2", "hub2+"}},
    {"name": "DoorProtectPlus", "price": 45, "centrals": {"hub", "hub+", "hub2"}},
    {"name": "Socket", "price": 30, "centrals": {"hub", "hub2"}}
]

for device in devices:
    if device['centrals'] == {'hub+'} and device['price'] > 40:
        print(device)
