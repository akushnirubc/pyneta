# Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows: 

# password = getpass()
# device = {
#     "host": "cisco4.lasthop.io",
#     "username": "pyclass",
#     "password": password,
#     "secret": password,
#     "device_type": "cisco_ios",
#     "session_log": "my_output.tls -olaxt",
# }
# Execute the following sequence of events using Netmiko:
# After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import time
import os


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

print("\nEnter Config mode")
net_connect.config_mode()
print ("\n>>>>>>>")
print("Checking if it's in config mode")
print("Config mode check: {}".format(net_connect.check_config_mode()))
print("Current Prompt: {}".format(net_connect.find_prompt()))


print("\nExit Config mode")
net_connect.exit_config_mode()
print ("\n>>>>>>>")
# print("Config mode check: {}".format(net_connect.exit_config_mode())
print("Current Prompt: {}".format(net_connect.find_prompt()))


net_connect = ConnectHandler(**device)
print("\nExit priviledged exec (disable), Current prompt")
net_connect.write_channel("disable\n")
time.sleep(2)
print ("\n>>>>>>>")
output = net_connect.read_channel()
print(output)

net_connect = ConnectHandler(**device)
print("\nExecute enable() method, Current prompt")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()