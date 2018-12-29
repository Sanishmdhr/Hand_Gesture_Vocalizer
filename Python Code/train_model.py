import pandas as pd
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier 
from sklearn.externals import joblib

#load the dataset ###############################
dataset= pd.read_csv("trainingdataset.csv")
dataset.head()

x=dataset.iloc[:,0:8].values #seperate the features
y= dataset.iloc[:,8].values #seperate the target label

#Split to test and train dataset###################################
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0) 

##scaling the features 
#sc = StandardScaler()
#x_train=sc.fit_transform(x_train)
#x_test=sc.transform(x_test)

#train our random forest algorithm ##############################
RF_classifier_Model = RandomForestClassifier (n_estimators=30, random_state=0)  
RF_classifier_Model.fit(x_train, y_train)  
#y_pred = RF_classifier_Model.predict(x_test)  
#save the model##############################################
filename = 'Hand_gesture_vocalizer_Trained_model.sav'
joblib.dump(RF_classifier_Model , filename)


#
#nfile = open ("newDataset.csv")
#new= pd.read_csv(nfile,sep=",")
#new
#y_pred = RF_classifier_Model.predict(new)           
#y_pred
#new.dtype