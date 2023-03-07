## Project #1 - Part #3 - Offline/Test Recognition with $1
## KSHITIJ SINHA (1416-0481) / HRITIK BAWEJA (5667-7397)

# Importing all the packages
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict
from statistics import mean
import recognizer
import random
import csv

# Setting current working directory
current_directory = os.getcwd() 
# print("curr ", current_directory)

# print(platform)
# Changing file path representations aaccording to the OS (MacOS/Win)
# if(platform == "darwin"):
#     cwd = os.getcwd() + "/xml/xml_logs"
# else:
#     cwd = os.getcwd() + '\Project1' + '\\' + 'xml' + '\\xml_logs'

if(platform == "darwin"):
    cwd = os.getcwd() + "/usersamples"
else:
    cwd = os.getcwd() + '\Project1' + '\\' + 'usersamples'
# Initializing data dictionary
dataDict = {}
gestureList = []

# Iterating in the working directory to access data folders
for fileName in os.listdir(cwd):
    if fileName == ".DS_Store":
        continue
    # print("cwd ", cwd +'\\' + fileName)
    if(platform == "darwin"):
       userFolder = cwd + '/' + fileName 
    else:
        userFolder = cwd + '\\' + fileName
    
    print(userFolder)
    # Choosing the medium speed folder 
    # speedFolder = userFolder+'/medium' if (platform == "darwin") else userFolder+'\\medium'
    speedFolder = userFolder
    gestureList = []
    gestureMap = {}
    for xml in os.listdir(speedFolder):
       
        # print("xml, ", xml, "usr, ", fileName)
        xml = speedFolder+'/'+xml if (platform == "darwin") else speedFolder+'\\'+xml
        
        # Creating XML tree 
        
        tree = ET.parse(xml)
        root = tree.getroot()
        
        # Getting details from XML for every file
        name = root.attrib.get('Name')
        subject = root.attrib.get('Subject')
        speed = root.attrib.get('Speed')
        number = root.attrib.get('Number')
        numpts = root.attrib.get('NumPts')
        points = []
        # print("sbj, ", subject)
        # Saving points as objects of recognizer.Point class
        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            points.append(recognizer.Point(x, y))
        
        # Maping label to points
        gestureMap[name] = points
        
        # Sorting by label name
        gestureMap = OrderedDict(sorted(dict.items(gestureMap)))
    
    # Mapping gesture map to User ID
    dataDict[subject] = gestureMap

# Sortig data based on User ID
dataDict = dict(sorted(dataDict.items(), key=lambda x: int(x[0])))


# Creating logFile instance and writing column names
fileName = "logfile_usersamples.csv"
fields = ["User[all-users]"	,"GestureType[all-gestures-types]" ,"RandomIteration[1to100]", "#ofTrainingExamples[E]", "TotalSizeOfTrainingSet[count]", "TrainingSetContents[specific-gesture-instances]", "Candidate[specific-instance]", "RecoResultGestureType[what-was-recognized]", "CorrectIncorrect[1or0]", "RecoResultScore", "RecoResultBestMatch[specific-instance]", "RecoResultNBestSorted[instance-and-score]"]

row = ["Recognition Log: Kshitij Sinha(1416-0481) Hritik Baweja(5667-7397) // [$1 RECOGNITION ALGORITHM] // [Unistroke Gesture Logs] // USER-DEPENDENT RANDOM-100"]

file = open(fileName, 'w')
csvwriter = csv.writer(file)
csvwriter.writerow(row)
csvwriter.writerow(fields)
    
#------------------------LOOPs---------------------------------------------#


# Creating a list of all Gesture Types
# GestureType = ["triangle", "x", "rectangle", "circle", "check", "caret",
#                  "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]

GestureType = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "zig zag"]

# GestureType = ["triangle"]
# print(dataDict.keys())
totalUserAccuracies = []

# Iterating in users
# for U in list(dataDict.keys())[0]:
for U in dataDict.keys():
    scoreList = []
    # print("U, ---------------", U)
    count=0
    totalCount = 0
    scoreList = []
    
    # Iterating for different number of examples
    for E in range(1, 10):
        # print("E, ---------------", E)
        
        # Iterating for 10 iterations
        for itr in range(1, 11):
            print("User:", U, "Example Count:", E, "Iteration:", itr)
            recoScore = 0
            
            TemplateSet = []
            TempTest = []
            TempTestLabels = []
            TestSet = []
            TestSetLabels = []
            PickedLabels = []
            TemplateSetList = []
            TestSetList = []
            
            # Iterating for different gesture types
            for G in GestureType:
                recoScore = 0
                PickGestureList = []
                
                # Picking the right gestures from complete data
                for key in dataDict[U].keys():
                    if(G in key):
                        # print("G ", G, "key", key)
                        # print(dataDict[U][key][0].X)
                        
                        # Appending Unistroke object ( preprocessing automatically done here)
                        PickGestureList.append(recognizer.Unistroke(key,dataDict[U][key]))
                        
                    
                        
                # pick gesture E times from pickgesturelist, pick T 1 time from same.     
                for p in range(1, E+1):
                    # print("p ", p)
                    
                    randIndexTemplate = random.randint(0, len(PickGestureList)-1)
                    
                    # temporary = choices(PickGestureList, k=1)
                    # print(Test[0].Name)
                    TemplateSet.append(PickGestureList[randIndexTemplate])
                    
                    TemplateSetList.append(PickGestureList[randIndexTemplate].Name)
                    
                    # Remove the ones choosen here from TempTest
                    PickGestureList.pop(randIndexTemplate)
                    
                # Randomly picking one of each gesture type for testing
                randIndexTest = random.randint(0, len(PickGestureList)-1)
                TestSet.append(PickGestureList[randIndexTest]) 
                TestSetList.append(PickGestureList[randIndexTest].Name) 
                
            # Testing
            for T in TestSet:
                resName = recognizer.recognize(points=T.Points, templates=TemplateSet, size=recognizer.SquareSize)
                # print("-------------")
                # print("Original ", T.Name, "Res ", resName[0].Name, resName[1], resName[2], "Match", resName[0].Name[:-2] == T.Name[:-2])
                # print("Nbest, ", resName[3])
                
                # If correct match, increment score.
                if resName[0].Name[:-2] == T.Name[:-2] :
                    # print("Correct MAtch -------------")
                    # print(resName[0].Name, T.Name)
                    # print(" -------------")
                    recoScore += 1
                # else:
                #     print("InCorrect MAtch -------------")
                #     print(resName[0].Name, T.Name)
                #     print(" -------------")       
                # Write result to logfile
                row1 = [U, T.Name[0:-2], itr, E, len(TemplateSet), TemplateSetList, T.Name, resName[0].Name, 1 if (resName[0].Name[:-2] == T.Name[:-2]) else 0, resName[1], resName[0].Name, resName[3]]
                csvwriter.writerow(row1)
            scoreList.append(recoScore)
            



                
            
    # scoreList.append(recoScore/1)
    # print("ScoreList", scoreList)
    # print("sum",U,":", sum(scoreList))
    # print("% Score for User",U,":", (sum(scoreList)*100)/(E*itr*16))
    

    totalUserAccuracies.append((sum(scoreList)*100)/(E*itr*16))

print("Total Accuracy:", mean(totalUserAccuracies))
csvwriter.writerow(["TotalAvgAccuracy", mean(totalUserAccuracies)])


#------------------------LOOPs---------------------------------------------#



# Dataset is list of dictionaries
# Dictionary has three keys : User, Gesture and Points 
# Points are stored in the form of class objs and x, y coordinates can be accessed via obj.X and obj.Y
# print(dataDict['5']['arrow01'][0].X)     #### Modified the data as this, give out the first X point of 1st arrow for user 5  