import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import os

os.chdir('D:\Programs\Datasets')  #path


data_income = pd.read_csv('income.csv')   #importing data

data = data_income.copy()   # created copy of original data

# Exploratory Data Analysis


# 2.Getting to know the data
print(data.info())
data.isnull().sum()    #Checks the sum of all missing values for corresponding columns

#Summary of numerical variables
summary_num=data.describe()
print(summary_num)

#Summary of Categorical variables
summary_cate=data.describe(include = "O")
print(summary_cate)
 
#Frequencies of important categories
data['JobType'].value_counts()
data['occupation'].value_counts()

#Unique values of important categories
# print(np.unique(data['JobType']).dropna())
# print(np.unique(data['occupation']).dropna())
#commented the above commmands becoz unique values cant include nan values

data = pd.read_csv('income.csv',na_values=[" ?"])


# 2.Data Preprocessing
data.isnull().sum()
missing = data[data.isnull().any(axis=1)]


# 1816 rows have atleast one nan values
# It is evident that 1809 records have both job and occupation as missing values
# Remaining 7 have jobtype as never worked(Which is useless)

data2 = data.dropna(axis=0)

#relationship between correlation values
correlation = data2.corr()
 
# 3. Data Visualization
data2.columns

#gender proportion table
gender = pd.crosstab(index = data2["gender"],
                     columns = 'count',
                     normalize = True )
print(gender)

# Gender vs Salary Status

gender_salstat = pd.crosstab(index = data2["gender"],
                             columns = data2['SalStat'],
                             margins = True,
                             normalize = 'index')
print(gender_salstat)                                          
