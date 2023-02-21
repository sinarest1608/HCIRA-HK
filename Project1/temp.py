from ast import Set
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict
import recognizer
from random import choices

print(platform)
if(platform == "darwin"):
    cwd = os.getcwd() + "/xml/xml_logs"
else:
    cwd = os.getcwd() + '\Project1' + '\\' + 'xml' + '\\xml_logs'

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

dataset = []


# for fileName in os.listdir(cwd):
#     # print("cwd ", cwd +'\\' + fileName)
#     if(platform == "darwin"):
#        userFolder = cwd + '/' + fileName 
#     else:
#         userFolder = cwd + '\\' + fileName
#     for user in os.listdir(userFolder):
#         # print("user ", user)
#         speedFolder = userFolder + '/' + user if(platform == "darwin")  else userFolder + '\\' + user
#         for speed in os.listdir(speedFolder):
#             # print("speed ", speed )
#             xmlFile = speedFolder + '/' + speed if(platform == "darwin")  else speedFolder + '\\' + speed
#             tree = ET.parse(xmlFile)
#             root = tree.getroot()
#             name = root.attrib.get('Name')
#             subject = root.attrib.get('Subject')
#             speed = root.attrib.get('Speed')
#             number = root.attrib.get('Number')
#             numpts = root.attrib.get('NumPts')
#             points = []
#             # print("sbj, ", subject)
#             for i in range(0, len(root)):
#                 x = root[i].attrib.get('X')
#                 y = root[i].attrib.get('Y')
#                 points.append(Point(x, y))

#             currSubject = {
#                 "User" : subject,
#                 "Gesture" : name[0:len(name)-2],
#                 "Points" : points
#             }

#             dataset.append(currSubject)
#             # print("root " ,root)
#             # print("attrib ", len(root))
#             # print("find ", root.attrib.get('Name'))
#             # print(len(points))
#             # print(numpts)
dataDict = {}
gestureList = []
for fileName in os.listdir(cwd):
    # print("cwd ", cwd +'\\' + fileName)
    if(platform == "darwin"):
       userFolder = cwd + '/' + fileName 
    else:
        userFolder = cwd + '\\' + fileName 
    speedFolder = userFolder+'/medium' if (platform == "darwin") else userFolder+'\\medium'
    gestureList = []
    gestureMap = {}
    for xml in os.listdir(speedFolder):
        
        # print("xml, ", xml, "usr, ", fileName)
        xml = speedFolder+'/'+xml if (platform == "darwin") else speedFolder+'\\'+xml
        tree = ET.parse(xml)
        root = tree.getroot()
        name = root.attrib.get('Name')
        subject = root.attrib.get('Subject')
        speed = root.attrib.get('Speed')
        number = root.attrib.get('Number')
        numpts = root.attrib.get('NumPts')
        points = []
        # print("sbj, ", subject)
        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            points.append(Point(x, y))
      
        # gestureList.append({name : points})
        # gestureList = 
        gestureMap[name] = points
        gestureMap = OrderedDict(sorted(dict.items(gestureMap)))
    dataDict[subject] = gestureMap
    
#------------------------LOOPs---------------------------------------------#

GestureType = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]

# GestureType = ["triangle"]

for U in list(dataDict.keys())[0]:
    print("U, ---------------", U)
    for E in range(1, 10):
        print("E, ---------------", E)
        # Add 1-100 loop
        TemplateSet = []
        TempTestPoints = []
        TempTestLabels = []
        TestSetPoints = []
        TestSetLabels = []
        for G in GestureType:
            PickGestureList = []
            for key in dataDict[U].keys():
                if(G in key):
                    # print(dataDict[U][key][0].X)
                    PickGestureList.append(recognizer.Unistroke(G,dataDict[U][key]))
                    
                    TempTestPoints.append(dataDict[U][key])
                    TempTestLabels.append(G)
               
            # pick gesture E times from pickgesturelist, pick T 1 time from same.     
            for p in range(1, E+1):
                # print("p ", p)
                # Remove the ones choosen here from TempTest
                temporary = choices(PickGestureList, k=1)
                # print(Test[0].Name)
                TemplateSet.append(temporary[0])
            # print(TemplateSet[0][0].Name)
            # TestSet.append(choices(PickGestureList, k=1))
            temporary1 = choices(TempTestPoints, k=1)
            # TestSetLabels.append(TemplateSet)
            TestSetPoints.append(temporary1)    
            
        for T in TestSetPoints:
            # print("To be tested ",T[0])
            Points = recognizer.resample(points=T[0], n=64)
            # print("points ",len(Points))
            r = recognizer.indicativeAngle(Points)
            Points = recognizer.rotateBy(Points, r)
            Points = recognizer.scaleTo(Points, recognizer.SquareSize)
            Points = recognizer.translateTo(Points, recognizer.Origin)
            # print("points ",len(Points))
            resName = recognizer.recognize(points=Points, templates=TemplateSet, size=recognizer.SquareSize)
            print("line 132 ", resName[0].Name, resName[1], resName[2])
            # displayResult(resName[0].Name, resName[1], resName[2])
        # print(len(TestSet), len(TemplateSet))
        
                # else:
                #     print(key)
            # if(dataDict[U].keys().contains(G)):
            #     print(dataDict[U].value())
            
            # print("User, ",U," Example, ", E, " Gesture ", str(G)+"0"+str(E), "Points ",dataDict[U][str(G)+"0"+str(E)][0].X)


#------------------------LOOPs---------------------------------------------#
# with open("myfile.txt", 'w') as f: 
#     for key, value in dataDict.items(): 
#         f.write('%s:%s\n' % (key, value))

        # print(name, subject, speed, number, numpts) 
    # print("user ", user)
    # speedFolder = userFolder + '/' + user if(platform == "darwin")  else userFolder + '\\' + user
    # for speed in os.listdir(speedFolder):
    #     # print("speed ", speed )
    #     xmlFile = speedFolder + '/' + speed if(platform == "darwin")  else speedFolder + '\\' + speed
        # tree = ET.parse(xmlFile)
        # root = tree.getroot()
        # name = root.attrib.get('Name')
        # subject = root.attrib.get('Subject')
        # speed = root.attrib.get('Speed')
        # number = root.attrib.get('Number')
        # numpts = root.attrib.get('NumPts')
        # points = []
        # # print("sbj, ", subject)
        # for i in range(0, len(root)):
        #     x = root[i].attrib.get('X')
        #     y = root[i].attrib.get('Y')
        #     points.append(Point(x, y))

    #     currSubject = {
    #         "User" : subject,
    #         "Gesture" : name[0:len(name)-2],
    #         "Points" : points
    #     }

    #     dataset.append(currSubject)
    #     # print("root " ,root)
    #     # print("attrib ", len(root))
    #     # print("find ", root.attrib.get('Name'))
    #     # print(len(points))
    #     # print(numpts)
    
    
# print(*dataset, sep="\n")
# print(dataset[0])
# s = set()
# for d in dataset:
#     for u in d["User"]:
        

# print(s)


# Dataset is list of dictionaries
# Dictionary has three keys : User, Gesture and Points 
# Points are stored in the form of class objs and x, y coordinates can be accessed via obj.X and obj.Y
# print(dataDict['5']['arrow01'][0].X)     #### Modified the data as this, give out the first X point of 1st arrow for user 5  