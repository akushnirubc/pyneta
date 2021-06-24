# Using your XML variable from exercise 1a, print out the entire XML tree in 
# a readable format  (ensure that the output string is a unicode string).

from __future__ import unicode_literals, print_function
from lxml import etree

# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print("\n\n")
print("Print the XML tree")
print("-" * 20)
print(etree.tostring(show_security_zones).decode())
# Alternate solution
# print(etree.tostring(show_security_zones, encoding="unicode"))