1. Upload the arduino code to your arduino board
2. The pictures folder contains the photos essentials for the python GUI
3. Put all the python files in the python code folder in the same folder or the project 
will not work.(Run the train_model.py first in order to train the model)

****** Description of the project *******
This project is design to assist the mute people to interact with other normal people via 
sign languages where the normal people may or maynot know the sign languages.
As everybody is not familiar with sign languages this project is designed to allow the 
mute people to interact with normal people who do not know the meanings of sign languages.
****************************************************************************************
In this project we have used 5 flex sensors, accelerometer and an Arduino Mega 2560 to take in
the hand gesture data from the user and all the data are processed in laptop.
****************************************************************************************
We have used Machine learning to predict the gestures done by the user.
An algorithm named Random Forest Classifier is used which is a supervised machine learning 
algorithm.
*****************************************************************************************
When an user makes a gesture the arduino takes in the flex sensor data that shows the bending 
of the fingers and the accelerometer shows the datas for hand movement of the user.
The datas are sent to the laptop via arduino via USB connection. 
The datas are then stored in a temporary dataset from which the trained model predicts the 
outcome of the hand gesture made by the user.
******************************************************************************************* 

