from pprint import pprint
import textfsm

template_file = "show_ip_int_brief.template"
template = open(template_file)

with open("show_ip_int_brief.txt") as f:
    raw_text_data = f.read()

# import ipdb
# ipdb.set_trace()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()





# (py3_venv) (py3_venv) [akushnir@pylab25b week_4_textfsm_reuse_code]$ python textfsm_simple.py 
# > /home/akushnir/notes/week_4_textfsm_reuse_code/textfsm_simple.py(14)<module>()
#      13 # The argument 'template' is a file handle and 'raw_text_data' is a string.
# ---> 14 re_table = textfsm.TextFSM(template)
#      15 data = re_table.ParseText(raw_text_data)

# ipdb> n
# > /home/akushnir/notes/week_4_textfsm_reuse_code/textfsm_simple.py(15)<module>()
#      14 re_table = textfsm.TextFSM(template)
# ---> 15 data = re_table.ParseText(raw_text_data)
#      16 template.close()

# /home/akushnir/notes/week_4_textfsm_reuse_code/textfsm_simple.py(15)<module>()
#      14 re_table = textfsm.TextFSM(template)
# ---> 15 data = re_table.ParseText(raw_text_data)
#      16 template.close()

# ipdb> n
# State Transition > : ShowIPIntBrief

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet0', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet1', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet2', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet3', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet4', '10.220.88.20', 'up', 'up']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['Vlan1', 'unassigned', 'down', 'down']

# > /home/akushnir/notes/week_4_textfsm_reuse_code/textfsm_simple.py(16)<module>()
#      15 data = re_table.ParseText(raw_text_data)
# ---> 16 template.close()
#      17 

# State Transition > : ShowIPIntBrief

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet0', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet1', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet2', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet3', 'unassigned', 'down', 'down']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['FastEthernet4', '10.220.88.20', 'up', 'up']

# Assign Var > : INTERFACE

# Assign Var > : IP_ADDR

# Assign Var > : LINE_STATUS

# Assign Var > : LINE_PROTOCOL

# RECORD > : ['Vlan1', 'unassigned', 'down', 'down']

# > /home/akushnir/notes/week_4_textfsm_reuse_code/textfsm_simple.py(16)<module>()
#      15 data = re_table.ParseText(raw_text_data)
# ---> 16 template.close()
#      17 

# ipdb> pp data
# [['FastEthernet0', 'unassigned', 'down', 'down'],
#  ['FastEthernet1', 'unassigned', 'down', 'down'],
#  ['FastEthernet2', 'unassigned', 'down', 'down'],
#  ['FastEthernet3', 'unassigned', 'down', 'down'],
#  ['FastEthernet4', '10.220.88.20', 'up', 'up'],
#  ['Vlan1', 'unassigned', 'down', 'down']]
# ['FastEthernet0', 'unassigned', 'down', 'down'],
#  ['FastEthernet1', 'unassigned', 'down', 'down'],
#  ['FastEthernet2', 'unassigned', 'down', 'down'],
#  ['FastEthernet3', 'unassigned', 'down', 'down'],
#  ['FastEthernet4', '10.220.88.20', 'up', 'up'],
#  ['Vlan1', 'unassigned', 'down', 'down']]
# ipdb> p type(data)
# <class 'list'>
# ipdb> p data[0]
# ['FastEthernet0', 'unassigned', 'down', 'down']
# 'FastEthernet0', 'unassigned', 'down', 'down']
# ipdb> p data[4]
# ['FastEthernet4', '10.220.88.20', 'up', 'up']
# 'FastEthernet4', '10.220.88.20', 'up', 'up']
# ipdb> p data[4][0]
# 'FastEthernet4'
# astEthernet4'
# ipdb> p data[4][1]
# '10.220.88.20'