# Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". 
# From this routing table data, extract all of the static and connected routes from the default VRF. 
# Print these routes to the screen and indicate whether the route is a connected route or a static route. 
# In the case of a static route, print the next hop address.


import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices
from pprint import pprint

def main():


    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = getpass()
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        # print(output)
        routes = output[0]['result']['vrfs']['default']['routes']
    # pprint(routes)
    
    print()
    for prefix, route_dict in routes.items():
        route_type = route_dict["routeType"]
        print()
        print(prefix)
        print("-" * 12)
        print(route_type)
        print(">" * 6)
        print(route_dict["vias"][0]["interface"])
        if route_type == "static":
            print(route_dict["vias"][0]["nexthopAddr"])
        print("-" * 12)
    print()
if __name__ == "__main__":
    main()