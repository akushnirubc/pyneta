# Print out the root element tag name (this tag should have a value of 
# "zones-information"). Print the number of child elements of the root element 
# (you can retrieve this using the len() function).

from __future__ import unicode_literals, print_function
from lxml import etree
# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print("\n\n")
print("Print the root name (tag) of the root element")
print("-" * 20)
print(show_security_zones.tag)
print()
print("Print the number of direct children of the root")
print("-" * 20)
print(len(show_security_zones))