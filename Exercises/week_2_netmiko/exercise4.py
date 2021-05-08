# Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

# ip name-server 1.1.1.1
# ip name-server 1.0.0.1
# ip domain-lookup

# Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

start_time = datetime.now()
device = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    "session_log": 'my_session.txt',
    "fast_cli": True,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
print()

cfg = ["ip name-server 1.1.1.1",
       "ip name-server 1.0.0.1",
       "ip domain-lookup",
]

cfg_change = net_connect.send_config_set(cfg)
print("Config changes:")
print(cfg_change)
print("*" * 80)

ping_output = net_connect.send_command("ping google.com")
# print(ping_output)
print("*" * 80)
if "!!" in ping_output:
    print("ping was successful!")
    print("\n\nPing Output {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))

end_time = datetime.now()
print("Total time {}".format(end_time - start_time))
# cmds = ["show version", "show lldp neighbors"]
# for cmd in cmds:
#     output = net_connect.send_command(cmd, use_textfsm=True)
#     print("*" *80)
#     print(cmd)
#     print("*" * 80)
#     print(output)
#     print("*" * 80)

#     if cmd == "show lldp neighbors":
#         print("LLDP Data structure type {}".format(type(output)))
#         print("test {}".format(output[0]))
#         print("HPE Switch connection port{}".format(output[0]["neighbor_interface"]))
