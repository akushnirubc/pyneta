# Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring(). 
# Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following: 
# <Element zones-information at 0x7f3271194b48>
# <class 'lxml.etree._Element'>

from __future__ import unicode_literals, print_function
from lxml import etree

# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print("\n\n")
print("Print the XML variable and its type")
print("-" * 20)
print(show_security_zones)
print(type(show_security_zones))