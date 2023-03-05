PROJECT 1- PART 4: Collecting Data from People


* GROUP MEMBERS (Group 18)
   * Kshitij Sinha
   * Hritik Baweja


* Note: All line number mentioned for the code refer to line numbers in canvas.py file in the directory unless otherwise mentioned


* PART A: Write Gesture Files
   * Our part 4 of the project begins from Line 48 in the canvas.py file by defining the part4() function. This is function is called by our program on start. As soon as the program is run, we show the user a prompt message saying “Welcome!” which indicates the user that experimentation has started (Line50, canvas.py). Next, from lines 51-54(canvas.py), we initialize our global variables to keep track and access the data and count of gesture and users. 
   * Next we get the current working directory, create a new directory named usersamples and prompt the user to draw our first gesture, Triangle along with the number of gesture. For example, “Draw Gesture: Triangle #1” and increment the gesture count globally. (Lines 56-79, canvas.py).
   * Next we define the insertXML() function that takes the dataset list as input and writes everything to the xml files upon being called in the submit function (described next). It creates a new file directory with subject ID. It then starts iterating the dataset and first checks for the last gesture. It then creates an ElementTree and gets the root. Different indices of the dataset are mapped to different names in the XML file such as Name, Subject, Speed, Number, NumPts, Milliseconds, AppName, AppVersion (set to 1.0.0 by default), Date, TimeOfDay and Points. Finally it opens the file on the path and writes the xml to it. (Lines 81-145, canvas.py).
   * From line 153 in canvas.py we start our submit() function which is called by clicking the Submit button (talked about in the later part). We start this by declaring the global variable to access their last value. We check if the current length of gestures drawn is less than the actual gestures to be collected and appends the required fields to the dataset (Line 177-178, canvas.py). It then checks if the user has finished with all the 16x10 gestures and appends that to dataset and shows the prompt “Thank you” to the user and ends the program. (Lines 180-195, canvas.py)
If all these fail, we continue to ask user to draw next gestures and increment the count by 1 on every gesture drawn. (Lines 197-209, canvas.py).
   * We change the calling function for the Submit button from recognize to submit. We also bind the part4 function to our module so that it runs upon starting the program. (Lines 258, 305, canvas.py).


 
* PART B: Prompt for Specific Samples
   * After each gesture is drawn, user receives a message box asking the user to draw next gesture along with the gesture number (Lines 77, 198, 205, canvas.py). The user can resume drawing by clicking the “OK” button on the box. At the end of all the 16x10 gestures, user is prompted by the message “Thank you for participating!” which indicates to the user that data collection is completed. (Line 194, canvas.py). User is also given the freedom to clear screen incase they are not satisfied by the gesture.
   * We do not perform any sort of recognition or preprocessing of the points and store the raw points itself. In our earlier parts, we had a dedicated recognize button to start the recognition process but we have commented the code for that in this part of the project. 








* PART C: Recruit 6 People
   * For our data collection, we asked 6 of our friends who are not in our HCIRA course to specifically eliminate any biases possible. Every candidate was asked to sign the consent form prior to the start of the data creation.
   * Once the program is started, the user receives prompts based on what gesture to draw and the number of gesture to be drawn. The GUI also has a clear screen button in case use draws something wrong and want to correct his gesture.
   * Once the user records 16x10, they are prompted by a thank you message which indicates that the data collection is finished. 
   * Every user data set is saved in usersamples by the name “Subject” with an ID.
   * We have tried to keep the user data as confidential as possible with no mention of the user details anywhere except in the consent forms.




* PART D: Submit Full Dataset
   * The final dataset can be found in the usersamples folder in the root folder. It further has 6 folders each named as “Subject1”, “Subject2”, “Subject3” …. “Subject6”. Each folder contains 16x10 gestures with each 16 the same as presented on the “$1 Unistroke Recognizer” webpage. Each file also follows the same structure as provided to us in the dataset used in project 1 part 3.
















* References
1. https://www.python.org/doc/
2. https://docs.python.org/3/library/tk.html
3. https://www.datacamp.com/community/tutorials/python-xml-elementtree
4. https://realpython.com/working-with-files-in-python/
5. http://depts.washington.edu/acelab/proj/dollar/index.html