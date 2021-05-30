# Expand on exercise3 except use a for-loop to configure five VRFs. 
# Each VRF should have a unique name and a unique route distinguisher. 
# Each VRF should once again have the IPv4 and the IPv6 address families controlled 
# by a conditional-variable passed into the template.

# Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.

from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./ex4_templates")

vrf_vars = [
    {"vrf_name": "blue", "rd_number": "100:1","ipv4_enabled": True,"ipv6_enabled": True},
    {"vrf_name": "blue1", "rd_number": "100:2","ipv4_enabled": True,"ipv6_enabled": True},
    {"vrf_name": "blue2", "rd_number": "100:3","ipv4_enabled": True,"ipv6_enabled": True},
    {"vrf_name": "blue3", "rd_number": "100:4","ipv4_enabled": True,"ipv6_enabled": True},
    {"vrf_name": "blue4", "rd_number": "100:5","ipv4_enabled": True,"ipv6_enabled": True},
]

j2_vars = {"vrf_vars": vrf_vars}
template_file = "vrf_loop_config.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars)
print(cfg)

