import os
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

os.chdir('D:\Programs\Datasets') #Path
Train_Data = pd.read_csv('CrashTest_TrainData.csv')
Test_Data = pd.read_csv('CrashTest_TestData.csv')


Test_Data.isnull().sum()
Train_Data.isnull().sum()

Train_Data1=Train_Data.copy()
Train_Data1.dropna(inplace = True)
Train_Data1.info()

Train_Data1['CarType'] = Train_Data1['CarType'].map( {'Hatchback':0,'SUV':1})


