import xml.etree.ElementTree as ET

root = ET.Element('Gesture')

root.set("Name", "arrow01")
root.set("Subject", "1")

element = ET.SubElement(root, "Point")
element.set("X", "1")
element.set("Y", "2")

root_xml = ET.tostring(root)

with open("temp.xml", "wb") as f:
    f.write(root_xml)