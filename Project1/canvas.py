import tkinter
import math

## Part a:
# Create A Tkinter App
main = tkinter.Tk()

# Define size of Window
main.geometry("500x500")

## Part b:                       
# Define Canvas Object with a white background
drawCanvas = tkinter.Canvas(main, bg='white')

# Bind the canvas to our app with north-west as (0,0) w.r.t our Window,
# Expand, Fill enables us to use the complete window even if we desire to resize.
drawCanvas.pack(anchor='nw', expand=1, fill='both')

# To store the points while drag (Useful for next part)
points = []

## Part c:
# This helps us register the mouse click and store the pointer co-ordinates. We use event here as a parameter.
def mouseDown(event):
    clearScreen()
    print("mouseDown")
    print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    
    
# This helps us draw a line betweem current and previous point. We use event here as a parameter.
def mouseDrag(event):
    global x, y
    drawCanvas.create_line((x, y, event.x, event.y), fill="black")
    x = event.x
    y = event.y
    points.append([x, y])

# This helps us register the mouse release and store the pointer co-ordinates. We use event here as a parameter.
def mouseUp(event):
    print("mouse up")
    print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    print(points)
    

# We bind the above functions to events and triggers provided by Tkinter library
drawCanvas.bind("<Button-1>", mouseDown)
drawCanvas.bind("<B1-Motion>", mouseDrag)
drawCanvas.bind("<ButtonRelease-1>", mouseUp)

## Part d: 
def clearScreen():
    drawCanvas.delete('all')
    
# Creating a button that calls the clearScreen function
clearScreenButton = tkinter.Button(main, text = 'Clear Canvas', bd = '7', command = clearScreen)

# Placing the button at the very bottom of the window
clearScreenButton.pack(side = 'bottom')

#resampling
def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dx = pow(dx, 2)
    dy = pow(dy, 2)
    return math.sqrt(dx + dy)


def path_length(A):
    d = 0.0
    for i in range(1, len(A)):
        d = d + distance(A[i-1], A[i])
    return d


def resample(points, n):
    I = path_length(points)/n
    D = 0.0
    newPoints = []
    newPoints.append(points[0])
    for i in range(1, len(points)):
        d = distance(points[i-1], points[i])
        if((d + D) >= I):
            qx = points[i-1][0] + ((I - D)/d) * (points[i][0] - points[i-1][0])
            qy = points[i-1][1] + ((I - D)/d) * (points[i][1] - points[i-1][1])
            q = [[qx, qy]]
            newPoints.append(q)
            points = points[:i] + q + points[i:]
            D = 0.0
        else:
            D = D + D

    if(len(newPoints) == n-1):
        newPoints.append([points[len(points)-1][0], points[len(points)-1][1]]) 

    return newPoints


#rotation
def Centroid(points):
    x = 0.0
    y = 0.0
    for i in range(0, len(points)):
        x = x + points[i][0]
        y = y + points[i][1]
    
    x = x/len(points)
    y = y/len(points)

    return [x, y]

def rotate_to_zero(points):
    c = Centroid(points)
    theta = math.atan2(c[1] - points[0][1], c[0] - points[0][0])
    return theta

def rotateBy(points, theta):
    c = Centroid(points)
    cos = math.cos(theta)
    sin = math.sin(theta)
    newPoints = []
    for i in range(0, len(points)):
        qx = (points[i][0] - c[0])*cos - (points[i][1] - c[1])*sin + c[0]
        qy = (points[i][0] - c[0])*sin + (points[i][1] - c[1]) *cos + c[1]
        newPoints.append([qx, qy])
    return newPoints


#Scale
# def Reactangle(self, x, y, width, height):
#     self.X = x
#     self.Y = y
#     self.Width = width
#     self.Height = height

def boundingBox(points):
    minX = math.inf
    maxX = -math.inf
    minY = math.inf
    minX = -math.inf
    for i in range(0, len(points)):
        minX = min(minX, points[i][0])
        maxX = max(maxX, points[i][0])
        minY = min(minY, points[i][1])
        maxY = max(maxY, points[i][1])
    return [minX, minY, maxX-minX, maxY-minY]

# for reactangle
# [0] = x
# [1] = y
# [2] = width
# [3] = height

def scaleTo(points, size):
    b = boundingBox(points)
    newPoints = []
    for i in range(0, len(points)):
        qx = points[i][0] * (size/b[2])
        qy = points[i][1] * (size/b[3])
        newPoints.append([qx, qy]) 
    return newPoints

def translateTo(points):
    c = Centroid(points)
    newPoints = []
    for i in range(0, len(points)):
        qx = points[i][0] - c[0]
        qy = points[i][1] - c[1]
        newPoints.append([qx, qy])
    return newPoints

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

