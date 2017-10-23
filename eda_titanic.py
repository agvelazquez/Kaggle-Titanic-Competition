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

data = pd.concat([train, test])
#%% Correlation Matrix

#data = data.fillna(method = 'ffill')
#(train.isnull().sum().sum()/len(train))*100

plt.figure()
plt.title('Spearman Correlation of Features', y=1.05, size=15)
corr = data.corr(method = 'spearman')
sns.heatmap(corr,linewidths=0.1,vmax=1.0, square=True, linecolor='white', annot=True)
plt.xticks(rotation=17)
plt.yticks(rotation=17)

#%% Boxplot: relationnship wit categorical variables 