from ast import Set
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict

from numpy import mean
import recognizer
# from random import choices
import random

print(platform)
if(platform == "darwin"):
    cwd = os.getcwd() + "/xml/xml_logs"
else:
    cwd = os.getcwd() + '\Project1' + '\\' + 'xml' + '\\xml_logs'

# class Point:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y

dataset = []



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
            points.append(recognizer.Point(x, y))
      
        # gestureList.append({name : points})
        # gestureList = 
        gestureMap[name] = points
        gestureMap = OrderedDict(sorted(dict.items(gestureMap)))
    dataDict[subject] = gestureMap
    
#------------------------LOOPs---------------------------------------------#

GestureType = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]

# GestureType = ["triangle"]
totalUserAccuracies = []
for U in [list(dataDict.keys())[0], list(dataDict.keys())[1]]:

# for U in dataDict.keys():
    scoreList = []
    # print("U, ---------------", U)
    count=0
    totalCount = 0
    scoreList = []
    for E in range(1, 3):
        # print("E, ---------------", E)
        # Add 1-100 loop
        
        for itr in range(1, 2):
            print("User:", U, "Example Count:", E, "Iteration:", itr)
            recoScore = 0
            
            TemplateSet = []
            TempTest = []
            TempTestLabels = []
            TestSet = []
            TestSetLabels = []
            PickedLabels = []
            for G in GestureType:
                recoScore = 0
                PickGestureList = []
                for key in dataDict[U].keys():
                    if(G in key):
                        # print("G ", G, "key", key)
                        # print(dataDict[U][key][0].X)
                        PickGestureList.append(recognizer.Unistroke(key,dataDict[U][key]))
                        
                        # TempTestPoints.append(dataDict[U][key])
                        
                        # -----TempTest.append(recognizer.Unistroke(key,dataDict[U][key]))----
                        
                        # TempTestLabels.append(G)
                        
                # pick gesture E times from pickgesturelist, pick T 1 time from same.     
                for p in range(1, E+1):
                    # print("p ", p)
                    # Remove the ones choosen here from TempTest
                    randIndexTemplate = random.randint(0, len(PickGestureList)-1)
                    
                    # temporary = choices(PickGestureList, k=1)
                    # print(Test[0].Name)
                    TemplateSet.append(PickGestureList[randIndexTemplate])
                    PickGestureList.pop(randIndexTemplate)
                    # TempTest.remove(TempTest[randIndexTemplate])
                    # for t in TempTest:
                    #     if t.Name == PickGestureList[randIndexTemplate].Name:
                    #         TempTest.remove(t)
                    
                            
           
                randIndexTest = random.randint(0, len(PickGestureList)-1)
                TestSet.append(PickGestureList[randIndexTest])  
                
            for T in TestSet:
                
                resName = recognizer.recognize(points=T.Points, templates=TemplateSet, size=recognizer.SquareSize)
                print("-------------")
                print("Original ", T.Name, "Res ", resName[0].Name, resName[1], resName[2], "Match", resName[0].Name[:-2] == T.Name[:-2])
                print("Nbest, ", resName[3])
                if resName[0].Name[:-2] == T.Name[:-2] :
                    # print("Correct MAtch -------------")
                    # print(resName[0].Name, T.Name)
                    # print(" -------------")
                    recoScore += 1
        scoreList.append(recoScore)

                
            
    # scoreList.append(recoScore/1)
    print("ScoreList", scoreList)
    print("sum",U,":", sum(scoreList))
    print("% Score for User",U,":", (sum(scoreList)*100)/(E*itr*16))
    totalUserAccuracies.append((sum(scoreList)*100)/(E*itr*16))

print("Total Accuracy:", mean(totalUserAccuracies))


#------------------------LOOPs---------------------------------------------#



# Dataset is list of dictionaries
# Dictionary has three keys : User, Gesture and Points 
# Points are stored in the form of class objs and x, y coordinates can be accessed via obj.X and obj.Y
# print(dataDict['5']['arrow01'][0].X)     #### Modified the data as this, give out the first X point of 1st arrow for user 5  