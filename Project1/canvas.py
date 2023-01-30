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
def markPoints(event):
    print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    
    
# To draw line between points
def drawLine(event):
    global x, y
    drawCanvas.create_line((x, y, event.x, event.y), fill="black")
    x = event.x
    y = event.y

drawCanvas.bind("<Button-1>", markPoints)
drawCanvas.bind("<B1-Motion>", drawLine)
# print(points)
# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

