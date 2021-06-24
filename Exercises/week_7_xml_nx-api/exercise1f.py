# Iterate through all of the child elements of the "trust_zone" variable. 
# Print out the tag name for each child element.

from __future__ import unicode_literals, print_function
from lxml import etree

# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

trust_zone = show_security_zones[0]
print("\n\n")
print("All children of the 'trust_zone'")
print("-" * 20)
for child in trust_zone:
    print(child.tag)
print("\n\n")