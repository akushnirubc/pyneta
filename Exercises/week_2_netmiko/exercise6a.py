# Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows: 

# password = getpass()
# device = {
#     "host": "cisco4.lasthop.io",
#     "username": "pyclass",
#     "password": password,
#     "secret": password,
#     "device_type": "cisco_ios",
#     "session_log": "my_output.txt",
# }
# Execute the following sequence of events using Netmiko:
# a. Print the current prompt using find_prompt()

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
print("Current prompt: ")
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
print()

net_connect.disconnect()