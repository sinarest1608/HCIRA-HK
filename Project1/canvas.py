import tkinter

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

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

