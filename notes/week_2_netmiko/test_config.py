from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco1.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    #"session_log": 'my_session.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

# cfg = [
#     'logging buffered 20000',
#     'no logging console',
#     'clock timezone EST -5 0',
# ]
output = net_connect.send_config_from_file(config_file='my_changes.txt')
print(output)

net_connect.disconnect()