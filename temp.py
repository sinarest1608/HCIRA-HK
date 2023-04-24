import xml.etree.ElementTree as ET
import os
import recognizer

current_directory = os.getcwd() + '\\Project2\\usersamples'
dataDict = {}
gestureList = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

for fileName in os.listdir(current_directory):
    gestureMap = {}
    print(fileName)
    xml_path = current_directory + '\\' + "Subject2"
    xml_pathn = current_directory + '\\' + "s02"
    # os.mkdir(xml_pathn)
    for xml in os.listdir(xml_path):
        tree = ET.parse(xml_path + '\\' + xml)
        root = tree.getroot()
        points = []
        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            points.append(recognizer.Point(x, y))

        newroot = ET.Element('Gesture')

        newroot.set("Name", gestureList[int(xml[0])] + "0" + xml[1])
        newroot.set("Subject", "2")
        newroot.set("Speed", "Medium")
        newroot.set("Number", root.attrib.get('Number'))
        newroot.set("NumPts", root.attrib.get('NumPts'))
        newroot.set("Milliseconds", "1024")
        newroot.set("AppName", "Gestures")
        newroot.set("AppVersion", "1.0.0.0")
        newroot.set("Date", root.attrib.get('Date'))
        newroot.set("TimeOfDay", root.attrib.get('TimeOfDay'))

        for p in points:
            element = ET.SubElement(newroot, "Point")
            element.set("X", str(p.X))
            element.set("Y", str(p.Y))
            element.set("T", str(1))
            element.tail = "\n \t"
        
        root_xml = ET.tostring(newroot, encoding="utf8")
        # print(xml[:-5])
        # print(xml[:-5] + "0" + xml[-5:])

        
        # os.mkdir(xml_pathn + '\\' + xml)
        with open(xml_pathn + '\\' + gestureList[int(xml[0])]+"0"+xml[1] + ".xml", "wb") as f:
            f.write(root_xml)
            print("xml ", xml)