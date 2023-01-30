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
def markPoints(array, event):
    print(event, end="")
    points.append(event.x, event.y)
    print(array)
    return

# To draw line between points
def drawLine():
    
    return

drawCanvas.bind('<Button-1>', markPoints, points)
# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()

