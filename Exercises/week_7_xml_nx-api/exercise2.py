# Using xmltodict, load the show_security_zones.xml file as a Python dictionary. 
# Print out this new variable and its type. 
# Note, the newly created object is an OrderedDict; not a traditional dictionary

from __future__ import unicode_literals, print_function
import xmltodict
from pprint import pprint 

with open("show_security_zones.xml") as infile:
    show_security_zones = xmltodict.parse(infile.read())

print("\n\n")
print("Print the new variable and it's type")
print("-" * 20)
pprint(show_security_zones)
pprint(type(show_security_zones))

# Print the names and an index number of each security zone in the XML data from Exercise 2a. 
# Your output should look similar to the following (tip, enumerate will probably help): 


print ("\n\n")
print("Print out index and name of the security zones")
print("-" * 20)
zones = show_security_zones["zones-information"]["zones-security"]
for index, zone in enumerate(zones):
    print(f"Security zone #{index + 1}: {zone['zones-security-zonename']}")
print("\n\n")