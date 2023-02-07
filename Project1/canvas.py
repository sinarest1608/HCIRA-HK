import tkinter
import math
import template

## Part 1a:
# Create A Tkinter App
main = tkinter.Tk()

# Define size of Window
main.geometry("500x500")

## Part 1b:                       
# Define Canvas Object with a white background
drawCanvas = tkinter.Canvas(main, bg='white')

# Bind the canvas to our app with north-west as (0,0) w.r.t our Window,
# Expand, Fill enables us to use the complete window even if we desire to resize.
drawCanvas.pack(anchor='nw', expand=1, fill='both')

# To store the points while drag (Useful for next part)
points = []

## Part 1c & Part 2a:
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

## Part 1d: 
def clearScreen():
    drawCanvas.delete('all')
    
# Creating a button that calls the clearScreen function
clearScreenButton = tkinter.Button(main, text = 'Clear Canvas', bd = '7', command = clearScreen)

# Placing the button at the very bottom of the window
clearScreenButton.pack(side = 'bottom')

#<------------------------Part 2------------------------>

#point class
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

#rectangle class
class Rectangle:
    def __init__(self, x, y, width, height):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height

#unistroke class
class Unistroke:
    def __init__(self, name, points):
        self.Name = name
        self.Points = resample(points, NumPoints)
        radians = indicativeAngle(self.Points)
        self.Points = rotateBy(self.Points, radians)
        self.Points = scaleTo(self.Points, SquareSize)
        self.Points = translateTo(self.Points, Origin)

#result class
class Result:
    def __init__(self, name, score, ms) -> None:
        self.Name = name
        self.Score = score
        self.Time = ms

NumUnistrokes = 16
NumPoints = 64
SquareSize = 250.0
Origin = Point(0,0)
Diagonal = math.sqrt(SquareSize * SquareSize + SquareSize * SquareSize)
HalfDiagonal = 0.5 * Diagonal
AngleRange = math.Deg2Rad(45.0)
AnglePrecision = math.Deg2Rad(2.0)
Phi = 0.5 * (-1.0 + math.sqrt(5.0))

#dollar recognizer
class DollarRecognizer:
    def __init__(self):
        self.Unistrokes = []
        self.Unistrokes[0] = Unistroke("triangle", [Point(137,139), Point(135,141), Point(133,144), Point(132,146), Point(130,149),
         Point(128,151), Point(126,155), Point(123,160), Point(120,166), Point(116,171), Point(112,177), Point(107,183),
         Point(102,188), Point(100,191), Point(95,195), Point(90,199), Point(86,203), Point(82,206), Point(80,209),
         Point(75,213), Point(73,213), Point(70,216), Point(67,219), Point(64,221), Point(61,223), Point(60,225),
         Point(62,226), Point(65,225), Point(67,226), Point(74,226), Point(77,227), Point(85,229), Point(91,230),
         Point(99,231), Point(108,232), Point(116,233), Point(125,233), Point(134,234), Point(145,233), Point(153,232),
         Point(160,233), Point(170,234), Point(177,235), Point(179,236), Point(186,237), Point(193,238), Point(198,239),
         Point(200,237), Point(202,239), Point(204,238), Point(206,234), Point(205,230), Point(202,222), Point(197,216),
         Point(192,207), Point(186,198), Point(179,189), Point(174,183), Point(170,178), Point(164,171), Point(161,168),
         Point(154,160), Point(148,155), Point(143,150), Point(138,148), Point(136,148)])

         

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
    Points = []
    Points.append(points[0])
    for i in range(1, len(points)):
        d = distance(points[i-1], points[i])
        if((d + D) >= I):
            qx = points[i-1][0] + ((I - D)/d) * (points[i][0] - points[i-1][0])
            qy = points[i-1][1] + ((I - D)/d) * (points[i][1] - points[i-1][1])
            q = [[qx, qy]]
            Points.append(q)
            points = points[:i] + q + points[i:]
            D = 0.0
        else:
            D = D + D

    if(len(Points) == n-1):
        Points.append([points[len(points)-1][0], points[len(points)-1][1]]) 

    return Points


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

def indicativeAngle(points):
    c = Centroid(points)
    theta = math.atan2(c[1] - points[0][1], c[0] - points[0][0])
    return theta

def rotateBy(points, theta):
    c = Centroid(points)
    cos = math.cos(theta)
    sin = math.sin(theta)
    Points = []
    for i in range(0, len(points)):
        qx = (points[i][0] - c[0])*cos - (points[i][1] - c[1])*sin + c[0]
        qy = (points[i][0] - c[0])*sin + (points[i][1] - c[1]) *cos + c[1]
        Points.append([qx, qy])
    return Points


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
    Points = []
    for i in range(0, len(points)):
        qx = points[i][0] * (size/b[2])
        qy = points[i][1] * (size/b[3])
        Points.append([qx, qy]) 
    return Points

def translateTo(points):
    c = Centroid(points)
    Points = []
    for i in range(0, len(points)):
        qx = points[i][0] - c[0]
        qy = points[i][1] - c[1]
        Points.append([qx, qy])
    return Points

def recognize(points, templates, size):
    
    # Represents Infinity
    b = 100000000000000
    
    #TODO: Need to see if Degree to Radians conversion required
    theta = 45
    thetaD = 2
    Tprime = []
    for T in templates:
        d = distanceAtBestAngle(points, T, -1*theta, theta, thetaD)  
        if d < b:
            b = d
            Tprime = T
    sizePrime = math.sqrt(2*size*size)
    score = 1 - (b/(0.5*sizePrime))
    return [Tprime, score]

def distanceAtBestAngle(points, T, thetaA, thetaB, thetaD):
    phi = (math.sqrt(5) - 1)/2
    x1 = phi*thetaA + (1 - phi)*thetaB
    f1 = distanceAtAngle(points, T, x1)
    x2 = (1 - phi)*thetaA + phi*thetaB
    f2 = distanceAtAngle(points, T, x2)
    
    while abs(thetaB - thetaA) > thetaD:
        if f1 < f2:
            thetaB = x2
            x2 = x1
            f2 = f1
            x1 = phi*thetaA + (1 - phi)*thetaB
            f1 = distanceAtAngle(points, T, x1)
        else:
            thetaA = x1
            x1 = x2
            f1 = f2
            x2 = (1 - phi)*thetaA + phi*thetaB 
            f2 = distanceAtAngle(points, T, x2)
    return min(f1, f2)

def distanceAtAngle(points, T, theta):
    Points = rotateBy(points, theta)
    d = pathDistance(Points, T)
    return d

def pathDistance(A, B):
    d = 0
    for i in range(0, len(A)):
        d += distance(A[i], B[i])
    return d/len(A)
# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

