# Use Python and Jinja2 to generate the below NX-OS interface configuration. 
# You should use an external template file and a Jinja2 environment to accomplish this. 
# The interface, ip_address, and netmask should all be variables in the Jinja2 template.

# nxos1
# interface Ethernet1/1
#   ip address 10.1.100.1/24

# nxos2
# interface Ethernet1/1
#   ip address 10.1.100.2/24

from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader([".", "./ex2_templates"])

interface = "Ethernet1/1"

nxos1 = {
    "interface": interface,
    "ip_addr": "10.1.100.1",
    "mask": "24"
}
nxos2 = {
    "interface": interface,
    "ip_addr": "10.1.100.2",
    "mask": "24"
}

for j2_vars in (nxos1, nxos2):
  template_file = "intf_config.j2"
  template = env.get_template(template_file)
  output = template.render(**j2_vars)
  print(output)