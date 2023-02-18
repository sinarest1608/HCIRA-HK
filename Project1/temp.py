import os
import xml.etree.ElementTree as ET
cwd = os.getcwd() + '\\' + 'xml' + '\\xml_logs'

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


for fileName in os.listdir(cwd):
    print("cwd ", cwd +'\\' + fileName)
    userFolder = cwd + '\\' + fileName
    for user in os.listdir(userFolder):
        print("user ", user)
        speedFolder = userFolder + '\\' + user
        for speed in os.listdir(speedFolder):
            print("speed ", speed )
            xmlFile = speedFolder + '\\' + speed
            tree = ET.parse(xmlFile)
            root = tree.getroot()
            name = root.attrib.get('Name')
            subject = root.attrib.get('Subject')
            speed = root.attrib.get('Speed')
            number = root.attrib.get('Number')
            numpts = root.attrib.get('NumPts')
            points = []

            for i in range(0, len(root)):
                x = root[i].attrib.get('X')
                y = root[i].attrib.get('Y')
                points.append(Point(x, y))

            print("root " ,root)
            print("attrib ", len(root))
            print("find ", root.attrib.get('Name'))
            print(len(points))
            print(numpts)
    

