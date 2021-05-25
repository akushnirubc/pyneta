# Expand your Jinja2 template such that both the following interface and BGP configurations 
# are generated for nxos1 and nxos2. The interface name, IP address, netmask, local_as, and peer_ip 
# should all be variables in the template. 
# This is iBGP so the remote_as will be the same as the local_as. 

# nxos1

# interface Ethernet1/1
#   ip address 10.1.100.1/24

# router bgp 22
#   neighbor 10.1.100.2 remote-as 22
#     address-family ipv4 unicast


# nxos2

# interface Ethernet1/1
#   ip address 10.1.100.2/24

# router bgp 22
#   neighbor 10.1.100.1 remote-as 22
#     address-family ipv4 unicast

from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader([".", "./ex2_templates"])

interface = "Ethernet1/1"

nxos1 = {
    "device_name": "nxos1",
    "local_as": 22,
    "interface": interface,
    "ip_addr": "10.1.100.1",
    "mask": "24",
}
nxos2 = {
    "device_name": "nxos2",
    "local_as": 22,
    "interface": interface,
    "ip_addr": "10.1.100.2",
    "mask": "24",
}

nxos1["peer_ip"] = nxos2["ip_addr"]
nxos2["peer_ip"] = nxos1["ip_addr"]

print()
for device in (nxos1, nxos2):
  print(f" {device['device_name']} ".center(80, "#"))
  template_file = "intf_bgp_config.j2"
  template = env.get_template(template_file)
  output = template.render(**device)
  print(output)
  print()
