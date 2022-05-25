# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:18:36 2022

@author: alexis.chabert
"""
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('prediction_article_transformer.csv')  

t=df['time']
target=df['target']
current=df['I']
pred=df['prediction']

plt.plot(current)
plt.plot(pred)
plt.plot(target)
