import json

file_path = r"C:\Users\77079\Downloads\sample-data.json"


with open(file_path, "r") as file:
    data = json.load(file)

header = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""

rows = []
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    rows.append(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")

output = header + "\n".join(rows)
print(output)
