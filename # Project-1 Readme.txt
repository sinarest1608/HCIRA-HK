PROJECT 1- PART 1: DRAWING ON A CANVAS


* GROUP MEMBERS (Group 18)
   * Kshitij Sinha
   * Hritik Baweja


* PART A: Set up a Development Environment
   * Programming Language Used: For the development of the project we have decided that we’ll be moving forward with Python 3 as our primary programming language due to the large set of compatible languages and a viable community.
   *  Code Editor: We will be using Visual Studio Code offered by Microsoft as our default code editor. VScode comes with a rich set of plugins and has built-in capabilities for git. VSCode also provides us with a clear hierarchy which is easy to navigate.
   * Libraries: We have used the Tkinter library in Python3 for the complete development of the project. Tkinter provides us with a complete set of methods that can be used to create canvas, draw lines, register user interactions from mouse clicks, mouse drags, mouse lifts etc. We import the library on line 1 in our program.
   * Collaboration Tool/Version Control: We will be using github for collaboration throughout our project. GitHub also provides us with a back up of our project code in case we ever need it.
 
* PART B: Instantiating a Canvas
   * Since we’ve successfully imported the library we can now use the methods that come inside it. On line 5, we use the tkinter.Tk() method to create and initialize our app. 
   * On line 8, we set the height and width as our default window size for our canvas the user, when needed can alter the size of the canvas as and when needed by the user. We use the main.geometry() method to do this(main refers to the variable we set while initializing the app). 
   * We then create our canvas (object) by Canvas() method on line 12. This takes a master app (here, we name it main) and the background color as input. We then anchor our canvas to the “north-west” of our app on line 16 which basically means that the north-west of our app is the (0,0) coordinate for our canvas. At the end, we put our app into a loop on line 66 so that it does not terminate unless the user explicitly closes it.




* PART C: Listening for Mouse or Touch Events
   * For this project we are going to move forward with using mouse events to capture the input movements of the user as we don’t have a touch enabled laptop or any other appropriate hardware with us. 
   * The first part of this task is to detect a left mouse button click event by the user which essentially depicts the start of the gesture. We define a function named mouseDown with an event as a parameter on line 23. We get the coordinates of where the user clicked the left mouse button on line 28 and line 29. These coordinates point to the start of the gesture. On line 51, we bind this function to the left mouse click event using the bind method. The parameter “<Button-1>” refers to the left mouse click event. 
   * The second part of the task is to follow through the path or motion the user takes while pressing the left mouse button. We define a function named mouseDrag with an event as a parameter on line 33. In this function we draw a line from the previous point to the current point. We also store the points of the users motion from left mouse button click to left mouse button release. On line 52, we bind the function mouseDrag to the <B1-Motion> event which is an event when the mouse is moved while the left button is being clicked by the user. 
   * The third and final part of the task is to detect when the user releases the left mouse button as this indicates the end of the gesture as we are dealing with unistroke gestures only during the course of the project. On line 41, we define a function named mouseUp with an event as a parameter to the function. This function detects the last point or the ending of the gesture and gives us the coordinates of when the gesture ends. On line 53, we bind this function to the left mouse button release event. The parameter “<ButtonRelease-1>” refers to the left mouse button release event. 


* PART D: Clearing the Canvas
   * In this task we have to provide the user with functionality to be able to clear the canvas as and when needed. Our approach to this task will be to add a button which the user can click when they need to clear the canvas.
   * To create a button we leverage the tkinter.Button method on line 60. For the method we need to pass the master which represents the parent window, in our case our parent window is main. Next we pass the text which we want to display on the button, this helps the user to identify the use for the button. We then fix the border width to 7. And lastly we pass in the command which is the function we desire to call when the button is clicked. 
   * We then place the button on the bottom of our window by using the button.pack method and passing the side as bottom to the method on line 63. 


* References
1. https://www.python.org/doc/
2. https://docs.python.org/3/library/tk.html
3. https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
4. https://pycad.co/how-to-draw-on-an-image/
5. https://depts.washington.edu/acelab/proj/dollar/index.html