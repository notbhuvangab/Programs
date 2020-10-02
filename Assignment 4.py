# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:44:42 2020

@author: Admin
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

Train_Data= pd.read_csv('CrashTest_TrainData.csv')
Test_Data=pd.read_csv('CrashTest_TestData.csv')
Train_Data.describe()

###Q13 What is the difference between third quartile values of the
# variable ManBI from Train_Data and Test_Data?
Train_Data['ManBI'].describe()
Test_Data['ManBI'].describe()
#75%       3.417500
#75%       2.50000
# ans=(3.417500-2.50000=0.9175)
###################################################
##Q14 How many distinct car types are there in the Train_Data?
pd.crosstab(Train_Data['CarType'],columns= 'count')
#col_0      count
#CarType         
#Hatchback     50
#SUV           30
#Ans=2
############################################
#Q15 How many missing values are there in Train_Data?
Train_Data.isnull().sum()
Test_Data.isnull().sum()
#Ans=3
##############################################
#Q16What is the proportion of car types in the Test_Data?
pd.crosstab(Test_Data['CarType'],columns= 'count')
#Ans=50-50
#########################################

train_data=Train_Data.dropna(axis=0)
train_x1=train_data.drop(['CarID','CarType'],axis=1,inplace=False)
train_y1=train_data['CarType']
train_y1=train_y1.map({'Hatchback':0,'SUV':1})

test_data=Test_Data.dropna(axis=0)
test_x1=test_data.drop(['CarID','CarType'],axis=1,inplace=False)
test_y1=test_data['CarType']
test_y1=test_y1.map({'Hatchback':0,'SUV':1})

model1=KNeighborsClassifier(n_neighbors=3)
model1_KNN=model1.fit(train_x1,train_y1)
prediction_model1=model1.predict(test_x1)
accuracy_score_model1=accuracy_score(test_y1,prediction_model1)
misclassified_sample=np.where(prediction_model1 != test_y1)

print("misclassified sample: %d" %(prediction_model1!=test_y1).sum())

######################33
model2=KNeighborsClassifier(n_neighbors=2)
model2_KNN=model2.fit(train_x1,train_y1)
prediction_model2=model2.predict(test_x1)
accuracy_score_model2=accuracy_score(test_y1,prediction_model2)


#################################3
from sklearn.linear_model import LogisticRegression
lgr=LogisticRegression()
lgr.fit(train_x1,train_y1)
predict_lgr=lgr.predict(test_x1)
accuracy_lgr=accuracy_score(test_y1,predict_lgr)
