import json
file_path = "D:\PP2\lab4\sample-data.json"

with open(file_path) as f:
    data = json.load(f)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for j in data['imdata']:
    l1PhysIf_data = j.get("l1PhysIf") 
    if l1PhysIf_data: 
        attributes_data = l1PhysIf_data.get("attributes")  
        if attributes_data:  
            print(attributes_data.get("dn"), attributes_data.get("descr"), attributes_data.get("speed"), attributes_data.get("mtu"))