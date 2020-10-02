#tips
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir("D:\Programs\Datasets")
Data=pd.read_csv('tips.csv')
df1=Data.loc[:, ['Time', 'TotalBill', 'Tips'] ]
Data1=pd.read_excel('Tips1.xlsx',sheet_name='Sheet1')
Data2 = pd.merge(Data, Data1, how='left')
Data3 = Data2.copy()
