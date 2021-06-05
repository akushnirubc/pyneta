# Create a Python module named 'my_funcs.py'. 
# In this file create two functions: function1 should read the YAML file you created in exercise 2a and return the corresponding data structure; 
# function2 should handle the output printing of the ARP entries 
# (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data). 
# Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.

import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, output_printer

def main():

  
    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = getpass()
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable( "show ip arp")
        arp_list = output[0]['result']['ipV4Neighbors']
        output_printer(arp_list)

if __name__ == "__main__":
    main()