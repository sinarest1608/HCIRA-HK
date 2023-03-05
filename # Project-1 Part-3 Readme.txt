PROJECT 1- PART 3: Offline/Test Recognition with $1


* GROUP MEMBERS (Group 18)
   * Kshitij Sinha - 1416-0481
   * Hritik Baweja - 5667-73397


* Steps to Run
   * Download the .zip file, extract it.
   * Using this command, run the offlineTest.py file:
      * python3 offlineTest.py
        NOTE: You may need to resolve package imports by using pip. 


* PART A: Read in Dataset
   * We begin this part of the project by checking the system operating system to configure our cwd variable to navigate to the xml folders correctly and use the same check further in the code. (Line 20 - 23)
   * We then import the “xml” package and use the “etree.ElementTree” method from the package to access different fields in the XML file.(Line 7)
   * We store the data as dictionary of a dictionary. In the sense, we have the root dictionary with keys as user IDs and the value as another dictionary with key as gestures and value as the list of points. 
for example, 
{
U1 : {"arrow01": [Points]
           "arrow02" : [Points] .....},
U2: {"arrow01": [Points]
           "arrow02" : [Points] .....},
U3: ....
}
So, dataDict['5']['arrow01'][0].X  Gives out the first X point of 1st arrow for user 5
   * To modify our data from XML to the dictionary, we first start by iterating in the XML files present in the directory and selecting the “medium” speed folder. We then create a xml tree and extract name (of the gesture), user, speed, number of points and the X and Y coordinates of each point. We store the coordinates as objects of Point class in a list as defined in the previous part of the project. We then create a dictionary with key as name and value as the points list and order the dictionary by name. Finally we put this as the value for the main dictionary with key as subject (user ID). (Line 30 - 75)


 
* PART B: Connect To Recognizer
   * We first create a list to store all the gesture types so it can be used further in part c to pick and recognize gestures. (Line 93) 
   * Every gesture picked is stored in a list as an object for Unistroke class. The Unistroke class preprocesses the list of points as soon as the object is initlialized so we don’t have to explicitly call the functions. (Line 139)
   * After selecting random gestures from the data for a particular gesture type, we select one random gesture from the data for that particular gesture type and call the recognize function that is defined in the recognizer.py file and explained in the last part of the project. (Line 159-161)
   * We preprocess our data when we call the recognizer.Unistroke() method on line 139 and append it to the pickGestureList variable. This method internally preprocesses the gesture using resample(), rotateBy(), scaleTo(), translateTo() methods defined in the recognizer.py file. 




* PART C: Loop Over Dataset 
   * We start this part by iterating over the keys, which are our users, in the main dictionary using the dataDict.keys() function. This gives us a list of all the keys to be iterated. To run the program for single user, we use list(dataDict.keys())[0]. (Line 102)
   * Next, we maintain a scoreList  to store average scores of each user, and start the example count (E) loop and start the 10 iteration loop. Here, we print the user, example count and the iteration number per example just to keep track of the program running. We then maintain some lists for storing template and test sets for each iteration.  (Line 103 - 125)
   * Next, we start iterating through the GestureType  list and maintain recoScore to store the accuracy score per gesture  and PickGestureList to store the required gestures as Unistroke object along with the label. (Line 128 - 139)
   * Then for each gesture G, we randomly pick E*16 template samples from the PickGestureList and simultaneously remove the picked ones from the list. We do this as we want to eliminate the chances of the same gesture being picked up randomly for both the template and the test set. We next pick 16 gestures, one of each type G, for the test set from PickGestureList. (Line 144 - 161)
   * The testing procedure starts. We iterate through the test set and call our recognizer() function which takes the current test set of points, the templates and square size. Note that we don’t preprocess the test set as we already did that while extracting gestures in PickGestureList when we created the 
Unistroke object. We store the result from recognizer() in resName variable and match if the test name and result name is correct and increment the score for the gesture. We also append the sum of score in the scoreList to calculate mean score for a particular user. (Line 164 - 180)


* PART D: Output The Result
   *  We start the logFile by defining a path and columns to be written. An initial row is being written that contains our details and the logfile title. These have been directly picked up from the sample logFile provided in the project description. We then open the file, create an object for multiple access, and write the above rows using File I/O methods in Python3. 
(Line 78 - 87)
   * After every iteration in the TestSet, we write to the file user, gesture, iteration number, number of examples(E), template set length (E*16), the template set, the test set, what gesture was recognized, correct recognition or not (1 for correct and 0 for incorrect), recognition confidence, best match from the N-best list and the N-best list. (Line 177-179)
   * Finally, we calculate the average accuracy and write that to the file too. (Line 195-196)




* References
1. https://www.python.org/doc/
2. https://docs.python.org/3/library/tk.html
3. https://www.datacamp.com/community/tutorials/python-xml-elementtree
4. https://realpython.com/working-with-files-in-python/
5. http://depts.washington.edu/acelab/proj/dollar/index.html