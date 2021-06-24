# Using both direct indices and the getchildren() method, 
# obtain the first child element and print its tag name. 

from __future__ import unicode_literals, print_function
from lxml import etree

# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print("\n\n")
print("Print the child tag using list indices")
print("-" * 20)
print(show_security_zones[0].tag)

print()
print("Print the child tag using getchildren()")
print("-" * 20)
print(show_security_zones.getchildren()[0].tag)