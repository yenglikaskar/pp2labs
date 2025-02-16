import json
jsonfile = 'jsonsample.json'
with open(jsonfile, 'r') as file:
    info = json.load(file)
print("Interface Status")
print("================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-------------------------------------------------- --------------------  ------  ------")
for i in info["imdata"]:
    a = i["l1PhysIf"]["attributes"]
    dn = a["dn"]
    descr = a["descr"]
    if descr:
        descr = descr
    else:
        descr = ""
    sp = a["speed"]
    mtu = a['mtu']
    print(f"{dn :<50} {descr:<20} {sp:<8} {mtu:<6}")