## Group 18
## Kshitij Sinha
## Hritik Baweja

import tkinter
import math
from datetime import datetime
import time
from tkinter import messagebox
import recognizer
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
    main, text='Recognize Gesture', bd='7', command=result)

# Placing the button at the very bottom of the window
recognizeScreenButton.pack(side='left')

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()
