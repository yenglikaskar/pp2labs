import json
dict = 'f.json'
with open(dict, 'r') as file:
    info = json.load(file)
info["price"] = 900
print(info)

