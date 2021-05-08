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
# Execute the exit_config_mode() method and print the new prompt using find_prompt()

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

net_connect = ConnectHandler(**device)
print("\nExit Config mode")
net_connect.exit_config_mode()
print ("\n>>>>>>>")
# print("Config mode check: {}".format(net_connect.exit_config_mode())
print("Current Prompt: {}".format(net_connect.find_prompt()))
print()

net_connect.disconnect()