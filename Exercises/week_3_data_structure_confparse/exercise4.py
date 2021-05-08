# You have the following JSON ARP data from an Arista switch:
# arp_data = {

#     "dynamicEntries": 2,
#     "ipV4Neighbors": [
#         {
#             "hwAddress": "dc38.e111.97cf",
#             "address": "172.17.17.1",
#             "interface": "Ethernet45",
#             "age": 0
#         },
#         {
#             "hwAddress": "90e2.ba5c.25fd",
#             "address": "172.17.16.1",
#             "interface": "Ethernet36",
#             "age": 0
#         }
#     ],
#     "notLearnedEntries": 0,
#     "totalEntries": 2,
#     "staticEntries": 0
# }

# From a file, read this JSON data into your Python program. 
# Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. 
# Print this dictionary to standard output.

import json
from pprint import pprint

with open("arista_ip.json") as f:
    data =json.load(f)

pprint(data)

arp_dict = {}
arp_entries = data["ipV4Neighbors"]

pprint(arp_entries)

for entry in arp_entries:
    print(entry["hwAddress"])
    print(entry["address"])
    mac_addr = entry["hwAddress"]
    ip_addr = entry["address"]
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()