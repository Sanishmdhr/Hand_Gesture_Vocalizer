from tkinter import *
import serial
import pandas as pd
from sklearn.externals import joblib
from PIL import Image, ImageTk
import pyttsx3

app = Tk()
app.title("Hand Gesture Vocalizer (Let Me Be Your Voice)")

app.geometry("1200x650")
app.configure(background="black")
app.resizable(width=False,height=False)

##for back ground image
image = Image.open('bg.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(app, image = photo_image)
label.pack()
############to open image for gesture###########################################
imgA= Image.open("(Put the path where you have kept the pictures folder)Pictures/Display pictures/A.png");
photoImgA= ImageTk.PhotoImage(imgA);

imgB = Image.open("Pictures/Display pictures/B.png");
photoImgB = ImageTk.PhotoImage(imgB);

imgC = Image.open("Pictures/Display pictures/C.jpg");
photoImgC = ImageTk.PhotoImage(imgC);

imgD = Image.open("Pictures/Display pictures/D.png");
photoImgD = ImageTk.PhotoImage(imgD);

imgE = Image.open("Pictures/Display pictures/E.jpg");
photoImgE = ImageTk.PhotoImage(imgE);

imgokay = Image.open("Pictures/Display pictures/Okay.jpg");
photoImgokay = ImageTk.PhotoImage(imgokay);

imgStop= Image.open("Pictures/Display pictures/Stop.jpg");
photoImgStop = ImageTk.PhotoImage(imgStop);

imgHello= Image.open("Pictures/Display pictures/Hello.png");
photoImgHello = ImageTk.PhotoImage(imgHello);

imgThankYou= Image.open("Pictures/Display pictures/Thank you.png");
photoImgThankYou = ImageTk.PhotoImage(imgThankYou);

imgCan= Image.open("Pictures/Display pictures/Can.png");
photoImgCan = ImageTk.PhotoImage(imgCan);

imgNow= Image.open("Pictures/Display pictures/Now.gif");
photoImgNow = ImageTk.PhotoImage(imgNow);

imgPlease= Image.open("Pictures/Display pictures/Please.png");
photoImgPlease = ImageTk.PhotoImage(imgPlease);

imgHM= Image.open("Pictures/Display pictures/Help me.png");
photoImgHM = ImageTk.PhotoImage(imgHM);

imgBye= Image.open("Pictures/Display pictures/Bye.gif");
photoImgBye = ImageTk.PhotoImage(imgBye);

imgEat= Image.open("Pictures/Display pictures/eat.jpg");
photoImgEat = ImageTk.PhotoImage(imgEat);

imgWR= Image.open("Pictures/Display pictures/I.jpg");
photoImgWR = ImageTk.PhotoImage(imgWR);

imgand= Image.open("Pictures/Display pictures/and.png");
photoImgand = ImageTk.PhotoImage(imgand);

imgNo= Image.open("Pictures/Display pictures/no.png");
photoImgNo = ImageTk.PhotoImage(imgNo);

imgi= Image.open("Pictures/Display pictures/i.png");
photoImgi = ImageTk.PhotoImage(imgi);

imgsit= Image.open("Pictures/Display pictures/sit.png");
photoImgsit = ImageTk.PhotoImage(imgsit);

imgCome= Image.open("Pictures/Display pictures/Come.png");
photoImgCome = ImageTk.PhotoImage(imgCome);
      
#####################################################################################      
def startApp():
    arduinoData=serial;
	## COM4 is the port number of the ****You can change it according to your port number of the arduino ***** 
	arduinoData= serial.Serial("COM4",9600); ## establish serial port connection 
    count=0;
    print("start");
    while arduinoData.isOpen(): ## while serial port is open continue
        myData= arduinoData.readline();
        if len(myData)>0: #check if there is data or not 
            data= myData.decode('utf-8');##do this
            print("Sensing....");
            open('newDataset.csv','w').close();## empty the file if it contains previous data
            nfile=open("newDataset.csv","a+");## add data
            nfile.write(data);
            count= count+1;
            if count == 15:
                nfile.close();##close the file
                arduinoData.close();##close the serial port
    RF_classifier_Model= joblib.load("Hand_gesture_vocalizer_Trained_model.sav");##load the trained model
    nfile=open("newDataset.csv");
    new=pd.read_csv(nfile,sep=",");##save the new unseen data to new variable after separating by comma
    y_pred = RF_classifier_Model.predict(new); ##predict the output
    nfile.close();
    open("newDataset.csv",'w').close();##empty the file
###########################################################
    def mostFrequent(y_pred,n):
        ##sort by array
        y_pred.sort();
        ##find the max frequent o/p using linear traversal
        max_count = 1; res= y_pred[0]; curr_count=1
        
        for i in range(1,n):
            if(y_pred[i] == y_pred[i-1]):
                curr_count +=1;
                
            else :
                if(curr_count > max_count):
                    max_count = curr_count;
                    res = y_pred[i-1];
                
                curr_count=1;
                
        ##if last elemet is most frequent
        if(curr_count > max_count):
            max_count=curr_count;
            res=y_pred[n-1];
            
        return res
    
    n= len(y_pred);
    output = mostFrequent(y_pred,n)
    print(output);
    
    outputImage= Text(app);
    outputImage.place(x=97,y=240);
    outputImage.config(height=13, width =40, state="disabled");
    
    ##for image display as per gesture##########################
    if output == "A":
         outputImage.image_create(INSERT,image=photoImgA);
      
    if output == "B":
         outputImage.image_create(INSERT,image=photoImgB);
         
    if output == "C":
         outputImage.image_create(INSERT,image=photoImgC);
           
    if output == "D":
         outputImage.image_create(INSERT,image=photoImgD);
           
    if output == "E":
         outputImage.image_create(INSERT,image=photoImgE);
         
    if output == "Okay":
         outputImage.image_create(INSERT,image=photoImgokay);
    
    if output == "Stop":
         outputImage.image_create(INSERT,image=photoImgStop);
         
    if output == "Hello":
         outputImage.image_create(INSERT,image=photoImgHello);
         
    if output == "Thank You":
         outputImage.image_create(INSERT,image=photoImgThankYou);
    
    if output == "Can":
         outputImage.image_create(INSERT,image=photoImgCan);
    
    if output == "Now":
         outputImage.image_create(INSERT,image=photoImgNow); 
         
    if output == "Please":
         outputImage.image_create(INSERT,image=photoImgPlease);
         
    if output == "Help Me":
         outputImage.image_create(INSERT,image=photoImgHM);    
        
    if output == "Good Bye":
         outputImage.image_create(INSERT,image=photoImgBye);
         
    if output == "Eat":
         outputImage.image_create(INSERT,image=photoImgEat);
        
    if output == "I need to go to washroom":
         outputImage.image_create(INSERT,image=photoImgWR);
    
    if output == "I":
         outputImage.image_create(INSERT,image=photoImgi);
    
    if output == "No":
         outputImage.image_create(INSERT,image=photoImgNo);
    
    if output == "Sit Here":
         outputImage.image_create(INSERT,image=photoImgsit);     
         
    if output == "Come":
         outputImage.image_create(INSERT,image=photoImgCome);   
         
    if output == "And":
         outputImage.image_create(INSERT,image=photoImgand);   
    ############################################################
    ####for text output as per gesture############
    outputImage.image_create(INSERT,image=photoImgi);     
    outputBox= Text(font=('Times New Roman', 17));
    outputBox.insert(INSERT,output);
    outputBox.place(x=20,y=470);
    outputBox.config(height=2, width =45, state="disabled");  
    ##########for speech conversion#################
    msg= pyttsx3.init()
    newVoiceRate= 200;
    msg.setProperty("rate",newVoiceRate);
    msg.say(output);
    msg.runAndWait();
        
        
def exitApp():
    app.destroy()
    
def speak():
    speech= entry_field.get()
    msg= pyttsx3.init()
    newVoiceRate = 200
    msg.setProperty('rate',newVoiceRate)
    #msg.setProperty('voices', sound[2].id)
    msg.say(speech)
    msg.runAndWait()


#for start button
startButton= Button(app, bg= 'lightslategrey',text= "CLICK TO SPEAK VIA GLOVES",command= startApp)
startButton.place(x=150,y=180)
startButton.config(height=2,width=30)

###Entry field
entry_field = Entry(font=('Times New Roman', 17))
entry_field.place(x=700,y=220)
entry_field.config(width=40)

### Speak via text 
SVTButton= Button(app, bg= 'lightslategrey',text= "CLICK TO TYPE AND TALK",command= speak)
SVTButton.place(x=830,y=290)
SVTButton.config(height=2,width=24)


##exit button
exitButton= Button(app, text= "EXIT", bg= 'lightslategrey',  command= exitApp)
exitButton.place(x=865,y=350)
exitButton.config(height=1,width=15)


## speech to text
#speech_to_text= Button(app, bg= 'lightslategrey',text= "SPEECH TO TEXT",comman=speechtotext)
#speech_to_text.place(x=300,y=330)
#speech_to_text.config(height=2,width=22)



app.mainloop()