# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:18:36 2022

@author: alexis.chabert
"""
import matplotlib.pyplot as plt
import pandas as pd

#load panda dataframe
df=pd.read_csv('prediction_article_transformer.csv')  

#load columns 'time','target','I' and 'prediction'
t=df['time']
target=df['target']
current=df['I']
pred=df['prediction']

#Plot
#Warning: each array contains around 1 million points
#slicing might be required to reduce memory consumption
#(e.g. plt.plot(t[:50000],current[:50000]))
plt.plot(t,current)
plt.plot(t,pred)
plt.plot(t,target)
