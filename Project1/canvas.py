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
gestureCount = 0

gestureList = ["triangle", "x", "rectangle", "circle", "check", "caret",
                 "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]

def part4(_):
    messagebox.showinfo("Gesture","Welcome!")
    global countNumberOfGestures
    global gestureCount
    global gestureList
    global count
    
    cwd = os.getcwd()
    print("cwd ", cwd)
    dir = "usersamples"
    path = ""
    count = 0

    if(os.path.exists(cwd + '\\' + dir) == False):
        path = os.path.join(cwd, dir)
        os.mkdir(path)
        print("path ", path)
        new_path = os.path.join(cwd+'\\'+dir, "Subject"+str(count+1))
        os.mkdir(new_path)
        count = 1
    else:
        count = len(os.listdir(cwd + '\\' + dir))
        new_path = os.path.join(cwd+'\\'+dir, "Subject"+str(count+1))
        # newLen = len(os.listdir(new_path))
        os.mkdir(new_path)
    submit()

def end():
    global countNumberOfGestures
    global gestureCount
    cwd = os.getcwd()
    print(type(cwd))
    dir = "usersamples"
    path = ""

    if(os.path.exists(cwd + '\\' + dir)):
        count = len(os.listdir(cwd + '\\' + dir))
    else:
        path = os.path.join(cwd, dir)
        os.mkdir(path)
        print(type(path))
    print(path)
    new_path = os.path.join(cwd+'\\'+dir, "Subject"+str(count+1))
    os.mkdir(new_path)
    countNumberOfGestures = 1
    gestureCount = 1

def insertXML(gestureList, gestureCount, points, cwd, count, dir):
    global countNumberOfGestures
    root = ET.Element('Gesture')

    print("count ", countNumberOfGestures)

    root.set("Name", gestureList[gestureCount])
    root.set("Subject", str(count))

    for p in points:
        element = ET.SubElement(root, "Point")
        element.set("X", str(p.X))
        element.set("Y", str(p.Y))
        print("X ", p.X)
        print("Y ", p.Y)

    root_xml = ET.tostring(root)

    new_path = os.path.join(cwd+"\\"+dir, "Subject"+str(count))

    # if(os.path.exists(new_path) == False):
    #     print("inside")
    #     os.mkdir(new_path)

    with open(new_path + '\\' + gestureList[gestureCount] + str(countNumberOfGestures) +".xml", "wb") as f:
        f.write(root_xml)

    countNumberOfGestures += 1

def submit():
    global countNumberOfGestures
    global gestureCount
    global gestureList
    global points
    global count
    cwd = os.getcwd()
    print(type(cwd))
    dir = "usersamples"
    path = ""

    print("gesture count inside submit ",gestureCount)
    print("countNumber inside submit", countNumberOfGestures)

    count = len(os.listdir(cwd + '\\' + dir))
    print("c inside submit", count)

    if(countNumberOfGestures == 2 and gestureCount < len(gestureList)):
        countNumberOfGestures = 1
        messagebox.showinfo("Gesture","Gesture " + gestureList[gestureCount] + str(countNumberOfGestures))
        insertXML(gestureList, gestureCount, points, cwd, count, dir)
        gestureCount += 1
        
    elif(gestureCount == len(gestureList)):
        messagebox.showinfo("Thank you", "Thank you participating in data collection!")
        # end()
    else:
        messagebox.showinfo("Gesture","Gesture " + gestureList[gestureCount] + str(countNumberOfGestures))
        insertXML(gestureList, gestureCount, points, cwd, count, dir)

    print("points inside submit", points)

def mouseDown(event):
    global points
    points = []
    clearScreen()
    obj1 = recognizer.DollarRecognizer()
    # print("mouseDown")
    # print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
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
    global x, y
    x = event.x
    y = event.y
    points.append(recognizer.Point(x, y))
    # Unistroke(points=points, name="")
    # print(points)


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
    print("points ",len(Points))
    r = recognizer.indicativeAngle(Points)
    Points = recognizer.rotateBy(Points, r)
    Points = recognizer.scaleTo(Points, recognizer.SquareSize)
    Points = recognizer.translateTo(Points, recognizer.Origin)
    print("points ",len(Points))
    resName = recognizer.recognize(points=Points, templates=recognizer.DollarRecognizer().Unistrokes, size=recognizer.SquareSize)
    print("line 386 ", resName[0].Name, resName[1], resName[2])
    displayResult(resName[0].Name, resName[1], resName[2])

# Defining a recognize button for the window
recognizeScreenButton = tkinter.Button(
    main, text='Recognize Gesture', bd='7', command=submit)

# Placing the button at the very bottom of the window
recognizeScreenButton.pack(side='left')

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

