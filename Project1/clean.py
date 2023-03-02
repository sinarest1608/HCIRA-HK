from ast import Set
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict

# from numpy import mean
from statistics import mean
import recognizer
# from random import choices
import random
import re

print(platform)
if(platform == "darwin"):
    cwd = os.getcwd() + "/xml/xml_logs"
else:
    cwd = os.getcwd() + '\Project1' + '\\' + 'xml' + '\\xml_logs'

# class Point:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y

dataDict = {}

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
        points = []
        # print("sbj, ", subject)
        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            points.append(recognizer.Point(x, y))
      
        # gestureList.append({name : points})
        # gestureList = 
        gestureMap[name] = points
        gestureMap = OrderedDict(sorted(dict.items(gestureMap))) #why this?
    dataDict[subject] = gestureMap

# print("user keys ", dataDict.keys())
# print("gesture name ", dataDict.get('1').keys())

preProcessedDataDict = {}
preProcessedGestureMap = {}

for u in dataDict.keys():
    for g in dataDict.get(u).keys():
        points = dataDict.get(u).get(g)
        Points = recognizer.resample(points=points, n=64)
        # print(u + " " + g + " " + str(len(Points)))
        r = recognizer.indicativeAngle(Points)
        Points = recognizer.rotateBy(Points, r)
        Points = recognizer.scaleTo(Points, recognizer.SquareSize)
        Points = recognizer.translateTo(Points, recognizer.Origin)
        preProcessedGestureMap[g] = Points
        preProcessedDataDict[u] = preProcessedGestureMap

        # print("points ",len(Points))
     
# print("user keys 2", preProcessedDataDict.keys())
# print("gesture name ", preProcessedDataDict.get('1').keys())

# for each user U = 1 to 10 
#   for each example E = 1 to 9 
#     for i = 1 to 100 
#       for each gesture type G 
#         choose E templates from U,G set 
#         choose 1 candidate from U,G set 
#       for each candidate T from 1 to G 
#         recognize T w/ E,G chosen templates 
#         if reco correct 
#           reco score for each U,G += 1 
#     reco score for each U,G /= 100 
# report final average per-user accuracy

gestureList = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]
count = 0
total = 0
totalUserAccuracies = []
# tempDict = {}
# tempDict['1'] = preProcessedDataDict.get('1')

for u in preProcessedDataDict.keys():
    print("U -------> ", u)
    scoreList = []
    for e in range(1, 10):
        print("e ------ ", e)
        for i in range(1, 5):
            templatesList = []
            candidatesList = []
            recScore = 0
            for gestureType in gestureList:
                UG = []
                for g in preProcessedDataDict.get(u).keys():
                    if(gestureType == g[0:len(g)-2]):
                        UG.append(recognizer.Unistroke(g, preProcessedDataDict.get(u).get(g)))
                    # print("gesture " + str(type(g)) + " " + g)
                numberOfTemplates = 1
                # print("len before " , len(UG))
                lengthUG = len(UG)
                while numberOfTemplates < e+1:
                    randomIdx = random.randint(0, lengthUG-1)
                    templatesList.append(UG[randomIdx])
                    UG.remove(UG[randomIdx])
                    numberOfTemplates += 1
                    lengthUG =len(UG)
                randomIdx = random.randint(0, len(UG)-1)
                candidatesList.append(UG[randomIdx])

                # print("len after ", len(UG))
            # print("temp len ", len(templatesList))
            # print("candidate len ", len(candidatesList))
            for T in candidatesList:
                # print(type(T))
                # points = recognizer.resample(T.Points, 64)
                # r = recognizer.indicativeAngle(points)
                # points = recognizer.rotateBy(points, r)
                # points = recognizer.scaleTo(Points, recognizer.SquareSize)
                # points = recognizer.translateTo(Points, recognizer.Origin)

                # print("len resample ", len(T.Points))
                resName = recognizer.recognize(points=T.Points, templates=templatesList, size=recognizer.SquareSize)
                if(resName[0].Name[:-2] == T.Name[:-2]): 
                    count += 1
                    recScore += 1
                total += 1
                
                # print("Match", resName[0].Name[:-2] == T.Name[:-2])
                # print("inside gesture ", type(dataDict.get(u).get(g)))
                # print("list of points ", len(preProcessedDataDict.get(u).get(g)))
        scoreList.append(recScore)

    print("Score List: ", scoreList)     
    print("sum ",u,":", sum(scoreList))
    print("% Score for User ",u,":", (sum(scoreList)*100)/(e*i*16))
    totalUserAccuracies.append((sum(scoreList)*100)/(e*i*16))

print("positive ", count)
print("Total ", total)