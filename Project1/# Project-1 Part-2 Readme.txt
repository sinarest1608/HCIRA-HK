PROJECT 1- PART 2: Online/Live Recognition


* GROUP MEMBERS (Group 18)
   * Kshitij Sinha
   * Hritik Baweja


* PART A: Store the Points
   * For the ease of storing points we’ve defined a class Point( line 33) as this helps us standardize points for capturing, processing and result. 
   * The first task tasks us with capturing the points the user makes the gesture through. Building on part 1 of the project we tweak our mouseDown(), mouseDrag() and mouseUp() methods. 
   * On line 38, we’ve our mouseDown() method, we define a global variable called points as we will be accessing these points throughout our implementation. We define points as an empty list initially. We capture the point at which the user clicks the left mouse button on and append it to the list of points (Line 45 - 48).
   * On line 52, we’ve our mouseDrag() method, in this method we capture the points the user drags through and append it to the list of points (Line 55 - 57). 
   * On line 62, we’ve our mouseDrag() method, in this method we capture the points the user drags through and append it to the list of points (Line 65 - 68). 


 
* PART B: Store Some Templates
   * We define a class called UniStroke on line 103 to help us efficiently organize a unistroke template. In this class we store the name of the unistroke, and perform preprocessing on the points. Unistroke.name gives use the name of the unistroke and Unistroke.Points gives us the Points list associated with that unistroke (Line 103 - 119).
   *  We use another class named DollarRecognizer() as a template class to store the list of all the unistrokes as object of the Unistroke class. First we initialize a list of length 16 and then place each unistroke in the length in order. In total we have 16 unistrokes. (Line 149 - 196)




* PART C: Implement $1 Algorithm 
   * Our implementation of the algorithm starts from Line 92. We first define a Rectangle class which takes input the coordinates, the height and the width for the rectangle. This is further used in the boundingBox function. (described further)
   * On line 123, we create a Result class by which we return the result from the recognise function. The object of the Result class has a name, score and time taken for the result (in ms).
   * Line 136 - 144 we define the required constants to be used further in the helper functions.
   * Our Step 1, Resampling begins from line 198. We create a helper function to calculate Euclidean distance between two coordinates on line 201. A path_length function is created on line 209 to calculate the perimeter of the gesture. The actual resample function begins from line 216 and returns the new list of points on line 243. Apart from the pseudocode given in the paper, we add an additional check outside the loop to check if the last point is added to the new list or not. 
   * Next for Step 2, we create four helper functions, Centroid on line 249(that calculates the centroid for the gesture), indicativeAngle on line 266, rotateToZero on line 275 (that rotates the gesture about origin) and rotateBy on line 282 (that rotates the gesture by the provided angle). This completes our Rotation part.
   * Step 3, Scaling and Translating begins from line 295. We create a boundingBox function that returns a rectangle based on the calculated height and width. We define the scaleTo function on line 308 that scales the gesture according to the boundingBox and appends the news points to the list. On line 318, translateTo function is defined that uses Centroid function to translate the gesture and returns the new set of points. 
   * For Step 4, Recognize, we create distanceAtBestAngle on line 330 take takes input three angles (thetaA, thetaB and thetaD) and calculates the best distance, distanceAtAngle on line 353 that calculates distance at a particular angle, pathDistance on line 361 and the final recognize function on 368 that uses angles of 45 and 2 degrees, loops over the templates and calculates the best fit and it’s score according to the pseudocode. We here calculate the time for execution using the time.time() functions provided by Python3. (Line 368 - 391)




* PART D: Output The Result
   * In the final part of the project, we need to display the result to the user who has made the gesture. We approach this task by giving the user a button to recognize the gesture, this also tells us that the user has made the gesture. 
   * On line 398, we define a function result() which we use to perform processing on the set of input points. On the set of input points we first perform resampling by calling the resample() method (Line 399). 
   * Then we find the indicative angle by calling the indicativeAngle() method (Line 401).
   * Then we rotate the gesture by calling the rotateBy() method (Line 402).
   * We then perform scaling by calling the scaleTo() method (Line 403).
   * We call the translateTo method to perform translation on the set of input points by calling translateTo(Line 404).
   * After performing all the processing steps and updating the points as we perform each step, we then call the recognize() method which performs the matching process and sends the template closest match with ,the score and the time taken to perform the process. We store this in the resName variable on line 406.
   * At the end, we call the displayResult() method which pops up a dialog box with the name of the template and the score on line 395. displayResult() function is implemented from line 394 - line 395. We use the messagebox method to pop a dialogue box using showinfo.
   * On line 411, we initialize a new button called recognizeScreenButton which we pressed on calls the result function we’ve discussed. On line 415, we pack this function to the left side of our Window.  
* References
1. https://www.python.org/doc/
2. https://docs.python.org/3/library/tk.html
3. https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
4. https://pycad.co/how-to-draw-on-an-image/
5. https://depts.washington.edu/acelab/proj/dollar/index.html
6. https://www.geeksforgeeks.org/how-to-create-a-pop-up-message-when-a-button-is-pressed-in-python-tkinter/
7. https://docs.python.org/3/library/tkinter.messagebox.html
8. https://www.w3schools.com/python/ref_math_dist.asp
9. https://www.activestate.com/resources/quick-reads/how-to-position-buttons-in-tkinter-with-pack/