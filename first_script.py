# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:12:15 2017

@author: Usr
"""
#Data Handling
import pandas as pd
import numpy as np
import os

#Visualization
import matplotlib.pyplot as plt
import seaborn as sns


#%% Data import 
gender_submission = pd.read_csv('gender_submission.csv')
train =pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train_description = train.describe()
test_description  = test.describe()

#%% Data Missing
train = train.fillna(method = 'ffill')
#%% Exploratory data analysis

train_numeric = train[['Pclass','Age','SibSp','Parch','Fare']]

plt.figure()
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(train.corr(),linewidths=0.1,vmax=1.0, square=True, linecolor='white', annot=True)
