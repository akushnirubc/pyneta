# Use the find() method to retrieve the first "zones-security" element. 
# Print out the tag of this element and of all its children elements. Your output should be similar to the following:

# Find tag of the first zones-security element
# --------------------
# zones-security

# Find tag of all child elements of the first zones-security element
# --------------------
# zones-security-zonename
# zones-security-send-reset
# zones-security-policy-configurable
# zones-security-interfaces-bound
# zones-security-interfaces
# Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).
# Use the findall() method to find all occurrences of "zones-security". For each of these security zones, 
# print out the security zone name ("zones-security-zonename", the text of that element).


from __future__ import unicode_literals, print_function
from lxml import etree


def read_xml(filename):
    with open(filename) as infile:
        return etree.fromstring(infile.read())

if __name__ == "__main__":
    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)

    print("\n\n")
    print("Find tag of the first zones-security element")
    print("-" * 20)
    first_zone = show_security_zones.find("./zones-security")
    print(first_zone.tag)

    print()
    print("Find the tag of all the child elements of the first security-zone")
    print("-" * 20)
    children = first_zone.getchildren()
    for child in children:
        print(child.tag)

    print("\n\n")
    print("Use the find() method to find the first 'zones-security-zonename' element")
    print("-" * 20)
    print(show_security_zones.find(".//zones-security-zonename").text)

    security_zones = show_security_zones.findall(".//zones-security")
    for zone in security_zones:
        print(zone.find("./zones-security-zonename").text)
    print("\n\n")