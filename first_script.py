# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:12:15 2017

@author: Usr
"""
import pandas as pd
import numpy as np
import os

#%% Data import 
gender_submission = pd.read_csv('gender_submission.csv')
train =pd.read_csv('train.csv')