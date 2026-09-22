import json

device = {
    "name": "Lobby Cisco Board",
    "type": "roomdesk",
    "ip": "10.10.10.5",
    "connected": True
}

print(device["name"])
print(json.dumps(device, indent=2))