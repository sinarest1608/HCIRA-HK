## Group 18
## Kshitij Sinha
## Hritik Baweja

import tkinter
import math
from datetime import datetime
import time
from tkinter import messagebox
import recognizer
import xml.etree.ElementTree as ET
import os
from sys import platform
# Part 1a:
# Create A Tkinter App
main = tkinter.Tk()

# Define size of Window
main.geometry("500x500")

# Part 1b:
# Define Canvas Object with a white background
drawCanvas = tkinter.Canvas(main, bg='white')

# Bind the canvas to our app with north-west as (0,0) w.r.t our Window,
# Expand, Fill enables us to use the complete window even if we desire to resize.
drawCanvas.pack(anchor='nw', expand=1, fill='both')

# To store the points while drag (Useful for next part)
points = []

# Part 1c & Part 2a:
# This helps us register the mouse click and store the pointer co-ordinates. We use event here as a parameter.

# Point class to standardize points capturing, processing and result output
# class Point:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y

countNumberOfGestures = 1
gestureCount = 15

gestureList = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "zig zag"]

def part4(_):
    # Shows the welcome message to user, indicates the application start
    messagebox.showinfo("Gesture","Welcome!")
    global countNumberOfGestures
    global gestureCount
    global gestureList
    global count

    # Get the current working directory 
    cwd = os.getcwd()
    # print("cwd ", cwd)
    
    # Storing directory name
    dir = "usersamples"
    path = ""
    count = 0
    # pathCheck = cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir
    
    # Check if path of directory does not exists
    if(os.path.exists(cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir) == False):
        # Create new directory
        path = os.path.join(cwd, dir)
        os.mkdir(path)
        print("path ", path)
        # new_path = os.path.join(cwd+'\\'+dir, "Subject"+str(count+1))
        # os.mkdir(new_path)
        # count = 1
    
    # Show Prompt asking user to draw the gesture with sample number
    messagebox.showinfo("Draw Gesture", "Gesture To Be Made: " + gestureList[gestureCount] + str(countNumberOfGestures))
    # Increment count of gesture
    countNumberOfGestures += 1

# Write data to XML file
def insertXML(dataset):
    cwd = os.getcwd()
    # print("cwd ", cwd)
    dir = "usersamples"
    # tempPath = cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir
    
    # Get the count of current directories present
    count = len(os.listdir(cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir))
    # Create new directory path for next subject
    new_path = os.path.join(cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir, "Subject"+str("1_itr"))
    # Create the new directory
    os.mkdir(new_path)

    lastGesture = dataset[0][0]
    counter = 0
    
    # Write the gesture to the XML File
    for i in range(0, len(dataset)):
        if(dataset[i][0] != lastGesture):
            lastGesture = dataset[i][0]
            counter = 1
        else:
            counter += 1

        root = ET.Element('Gesture')

        print(dataset[i][0], counter)
        root.set("Name", dataset[i][0] + str(counter))
        root.set("Subject", str(count+1))
        root.set("Speed", "Medium")
        root.set("Number", str(counter))
        root.set("NumPts", str(len(dataset[i][1])))
        root.set("AppName", "Gestures")
        root.set("AppVersion", "1.0.0.0")

        currentDate = datetime.now()
        root.set("Date", currentDate.strftime("%A, %B %d, %Y"))
        currentTime = datetime.now()
        root.set("TimeOfDay", currentTime.strftime("%X %p"))
    

        # Extract X and Y co-ordinates from Point Object and store in XML file
        for p in dataset[i][1]:
            element = ET.SubElement(root, "Point")
            element.set("X", str(p.X))
            element.set("Y", str(p.Y))
            element.tail = "\n \t"
            # print("X ", p.X)
            # print("Y ", p.Y)        

        # Set the encoding as utf-8
        root_xml = ET.tostring(root, encoding="utf8")

        new_path = os.path.join(cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir, "Subject"+str("1_itr"))

    # if(os.path.exists(new_path) == False):
    #     print("inside")
    #     os.mkdir(new_path)
        # Save the file
        xmlPath = new_path + '/' + dataset[i][0] + str(counter) +".xml" if (platform == "darwin") else new_path + '\\' + dataset[i][0] + str(counter) +".xml"
        with open(xmlPath, "wb") as f:
            f.write(root_xml)
            print("xml ", xmlPath)

    # print("count ", countNumberOfGestures)

# Create dataset list to store all the points
dataset = []
datasetTally = []

# The submit button calls this
def submit():
    # Define global variables to access and store data
    global countNumberOfGestures
    global gestureCount
    global gestureList
    global points
    global count
    global datasetTally
    
    cwd = os.getcwd()
    # print(type(cwd))
    dir = "usersamples"
    path = ""

    # Clear Screen when user clicks Submit gesture
    clearScreen()
    # print("gesture count inside submit ",gestureCount)
    # print("countNumber inside submit", countNumberOfGestures)

    count = len(os.listdir(cwd+ '/'+ dir if (platform == "darwin") else cwd + '\\' + dir))
    # print("c inside submit", count)

    # To calculate user time
    
    if(gestureCount < len(gestureList)-1):
        dataset.append([gestureList[gestureCount], points])
    
    # If last gesture
    elif(gestureCount == len(gestureList)-1):
        if(countNumberOfGestures < 2):
            dataset.append([gestureList[gestureCount],points])
        else:
        # print("first ", dataset[0])
        # print("first T ", datasetTally[0])
            dataset.append([gestureList[gestureCount],points])
            # Put everything in XML
            insertXML(dataset)
            # Reset data list
            dataset.clear()

            # Display Thank you message
            messagebox.showinfo("Thank you", "Thank you for participating!")
            main.destroy()

    if(countNumberOfGestures <2 and gestureCount < len(gestureList)) :
        messagebox.showinfo("Draw Gesture", "Gesture To Be Made: " + gestureList[gestureCount] + str(countNumberOfGestures))
        print("Gesture: " + gestureList[gestureCount] + str(countNumberOfGestures))
        countNumberOfGestures += 1
    elif(gestureCount < len(gestureList)):
        gestureCount += 1
        countNumberOfGestures = 1
        if(gestureCount < len(gestureList)):
            messagebox.showinfo("Draw Gesture", "Gesture To Be Made: " + gestureList[gestureCount] + str(countNumberOfGestures))
            print("Gesture: " + gestureList[gestureCount] + str(countNumberOfGestures))
        countNumberOfGestures += 1
    else:
        gestureCount += 1

    print("gC ", gestureCount)


    # countNumberOfGestures += 1
    # print("points inside submit", points)
    # print("countNUmber 2 inside submit ", countNumberOfGestures)


def mouseDown(event):
    global points, s
    points = []
    clearScreen()
    obj1 = recognizer.DollarRecognizer()
    # print("mouseDown")
    # print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    s = datetime.now().microsecond
    points.append(recognizer.Point(x, y))


# This helps us draw a line betweem current and previous point. We use event here as a parameter.
def mouseDrag(event):
    global x, y
    drawCanvas.create_line((x, y, event.x, event.y), fill="black")
    x = event.x
    y = event.y
    points.append(recognizer.Point(x, y))

# This helps us register the mouse release and store the pointer co-ordinates. We use event here as a parameter.


def mouseUp(event):
    # print("mouse up")
    # print(event.x, event.y)
    global x, y, datasetTally, s, e
    x = event.x
    y = event.y
    points.append(recognizer.Point(x, y))
    # Unistroke(points=points, name="")
    # print("points when mouse up ", points)
    e = datetime.now().microsecond
    datasetTally.append(points)


# We bind the above functions to events and triggers provided by Tkinter library
drawCanvas.bind("<Visibility>", part4)
drawCanvas.bind("<Button-1>", mouseDown)
drawCanvas.bind("<B1-Motion>", mouseDrag)
drawCanvas.bind("<ButtonRelease-1>", mouseUp)

# Part 1d:


def clearScreen():
    drawCanvas.delete('all')


# Creating a button that calls the clearScreen function
clearScreenButton = tkinter.Button(
    main, text='Clear Canvas', bd='7', command=clearScreen)

# Placing the button at the very bottom of the window
clearScreenButton.pack(side='left')

# <------------------------Part 2------------------------>

# Displaying the result on button click using an information box
def displayResult(template, score, timeTaken):
    messagebox.showinfo("Result", "Result: " + template + " \nScore: " + str(round(score*100)) + "\n Time take: "+str(round(timeTaken)) + "ms")

# Calcualting the result and identifying gesture. This function is called on the "Recognize" function and returns the result to the displayResult function
def result():
    Points = recognizer.resample(points=points, n=64)
    # print("points ",len(Points))
    r = recognizer.indicativeAngle(Points)
    Points = recognizer.rotateBy(Points, r)
    Points = recognizer.scaleTo(Points, recognizer.SquareSize)
    Points = recognizer.translateTo(Points, recognizer.Origin)
    # print("points ",len(Points))
    resName = recognizer.recognize(points=Points, templates=recognizer.DollarRecognizer().Unistrokes, size=recognizer.SquareSize)
    # print("line 386 ", resName[0].Name, resName[1], resName[2])
    displayResult(resName[0].Name, resName[1], resName[2])


# Defining a recognize button for the window
# recognizeScreenButton = tkinter.Button(
#     main, text='Recognize Gesture', bd='7', command=result)

# # Placing the button at the very bottom of the window
# recognizeScreenButton.pack(side='left')


submitButton = tkinter.Button(main, text='Submit Gesture', bd='7', command=submit)
submitButton.pack(side='left')

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

