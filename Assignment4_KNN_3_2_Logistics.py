#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing required libraries
import os
import pandas as pd
import numpy as np

os.chdir('D:\Programs\Datasets')
# In[6]:


Train_Data = pd.read_csv("CrashTest_TrainData.csv") # read the train dataset


# In[7]:


Test_Data = pd.read_csv("CrashTest_TestData.csv")  # read the test dataset


# In[8]:


Train_Data.isnull().sum()  # 15Q) missing values in Train_Data


# In[9]:


# third quartile values of the variable ManBI in Train Data
Train_Q3 = np.percentile(Train_Data.ManBI, 75)  # Q3
Train_Q3


# In[10]:


# third quartile values of the variable ManBI in Test Data
Test_Q3 = np.percentile(Test_Data.ManBI, 75)  # Q3
Test_Q3


# In[11]:


# 13Q) difference between third quartile values of the variable ManBI from Train_Data and Test_Data
diff_Train_Test_Q3 = Train_Q3 - Test_Q3
diff_Train_Test_Q3


# In[13]:


Train_Data[Train_Data.isnull().any(axis=1)] # 15Q) missing values are there in Train_Data
Train_Data.shape

# In[14]:


Train_Data2 = Train_Data.dropna()  # Drop the missing values


# In[15]:


Train_Data2.shape


# In[ ]:


Train_Data2.isnull().sum()


# In[3]:


np.unique(Train_Data2['CarType']) #14Q) distinct car types are there in the Train_Data


# In[176]:


Train_Data2['CarType'].value_counts()


# In[177]:


Train_Data2.dtypes  # Map the categorical variables into integers


# In[133]:


# Reindexing the CarType status names to 0,1

Train_Data2['CarType'] = Train_Data2['CarType'].map({'Hatchback': 0, 'SUV':1})



# In[134]:


np.unique(Train_Data2['CarType'])


# In[135]:


# 16Q)  proportion of car types in the Test_Data
prop_cartype = pd.crosstab(index = Test_Data["CarType"],
                  columns = 'count',
                  normalize = True)
prop_cartype


# In[136]:


Test_Data['CarType'] = Test_Data['CarType'].map({'SUV' : 0, 'Hatchback':1})


# In[137]:


Test_Data.dtypes  # to check all column data types


# In[138]:


# target variable (output variable)  - CarType
# seperate the independent (input variables) and target variable on training data and test data
#train_y = Train_Data2['CarType']
#train_x = Train_Data2.drop(['CarType'], axis=1, inplace=True)

#test_y = Test_Data['CarType']
#test_x = Test_Data.drop(['CarType'], axis=1, inplace=True)


# In[139]:


# remove sequence ID value ( CarID) in both train and test data . 
# By removing this will get better accuracy
#train_x = Train_Data2.drop(columns = ['CarID'], axis = 1)
#test_x = Test_Data.drop(columns = ['CarID'], axis = 1)

new_data = pd.get_dummies(Train_Data2,drop_first=True)
columns = list(new_data.columns)
features = list(set(columns)-set(['CarType']))
print(features) 


x=Train_Data2[features].values
y=Train_Data2['CarType']
print(x.shape,y.shape)

data_test = pd.get_dummies(Test_Data,drop_first=True)  # for test data set.
col1 = list(data_test.columns)
features_test = list(set(col1)-set(['CarType']))
print(features_test) 


x_test = Test_Data[features]
y_test = Test_Data['CarType']
print(x_test.shape,y_test.shape)


# In[140]:


x_test.head()


# In[141]:


x_test.dtypes


# In[142]:


#importing the library of KNN
from sklearn.neighbors import KNeighborsClassifier


# In[143]:


# Storing the K nearest neighbors classifier
KNN_classifier_K3 = KNeighborsClassifier(n_neighbors = 3)


# In[144]:


# Fitting the values for x and y
KNN_classifier_K3.fit(x,y)


# In[145]:


# Predicting the test values with model
prediction_k3 = KNN_classifier_K3.predict(x_test)


# In[146]:


from sklearn.metrics import accuracy_score


# In[147]:


# Calculating the accuracy 
accuracy_score_k3 = accuracy_score(y_test, prediction_k3)


# In[148]:


# 17Q) accuracy score of the K-Nearest Neighbor model (model_1) with 3 neighbors using Train_Data and Test_Data
print(accuracy_score_k3)  


# In[152]:


y_test = np.asarray(y_test)
misclassified_y_test = np.where(y_test != KNN_classifier_K3.predict(x_test))


# In[153]:


# 18Q ) list of indices of misclassified samples from the ‘model_1’.
misclassified_y_test


# In[154]:


KNN_classifier_K2 = KNeighborsClassifier(n_neighbors = 2)
KNN_classifier_K2.fit(x,y)
prediction_k2 = KNN_classifier_K2.predict(x_test)
accuracy_score_k2 = accuracy_score(y_test, prediction_k2)
print(accuracy_score_k2) 


# In[157]:


# 19Q) Compare results of the two models (model_1 & model_2).
print(accuracy_score_k2 > accuracy_score_k3) 


# In[158]:


from sklearn.linear_model import LogisticRegression


# In[159]:


logistic = LogisticRegression()


# In[160]:


logistic.fit(x,y)


# In[161]:


logistic.coef_
logistic.intercept_
prediction = logistic.predict(x_test)


# In[162]:


accuracy_score_log = accuracy_score(y_test,prediction)


# In[163]:


print(accuracy_score_log)  # 20Q Logistic Accuracy score

