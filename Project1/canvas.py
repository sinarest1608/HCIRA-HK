import tkinter

# Create A Tkinter App
main = tkinter.Tk()

# Define size of Window
main.geometry("500x500")
                          
# Define Canvas Object with a white background
drawCanvas = tkinter.Canvas(main, bg='white')

# Bind the canvas to our app with north-west as (0,0) w.r.t our Window,
# Expand, Fill enables us to use the complete window even if we desire to resize.
drawCanvas.pack(anchor='nw', expand=1, fill='both')


points = []
# To store the points while drag (Useful for next part)
def mouseDown(event):
    clearScreen()
    print("mouseDown")
    print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    
    
# To draw line between points
def mouseDrag(event):
    global x, y
    drawCanvas.create_line((x, y, event.x, event.y), fill="black")
    x = event.x
    y = event.y
    points.append([x, y])

def mouseUp(event):
    print("mouse up")
    print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    print(points)

drawCanvas.bind("<Button-1>", mouseDown)
drawCanvas.bind("<B1-Motion>", mouseDrag)
drawCanvas.bind("<ButtonRelease-1>", mouseUp)

# part d: clearing the canvas
def clearScreen():
    drawCanvas.delete('all')
    
clearScreenButton = tkinter.Button(main, text = 'Clear Canvas', bd = '7', command = clearScreen)

clearScreenButton.pack(side = 'bottom')

# print(points)
# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

