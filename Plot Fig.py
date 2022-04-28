# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:18:36 2022

@author: alexis.chabert
"""
import pickle
import matplotlib.pyplot as plt
import numpy as np
path=r'M:\ae\dcade\Python_IA\IA/'.replace('\\','/')
file='prediction_probability.p'
I = pickle.load( open(path+file, "rb" ) )


#I.show()
#I.axes[0].get_children()

t=I.axes[0].lines[0].get_xdata()
current=I.axes[0].lines[0].get_ydata()
target=I.axes[0].lines[1].get_ydata()
pred=I.axes[0].lines[2].get_ydata()

plt.Figure()
plt.plot(current,color='tab:green')#,'+',markersize=1)
plt.plot(target,'|',color='tab:orange', markersize=5)
plt.plot(pred,'+',color='tab:blue',markersize=1)

plt.plot(target-pred,'+',markersize=0.1)

plt.hist((target-pred).transpose(),500, density=True,log=False)


fig, axs = plt.subplots(1, 1,sharex='col')
axs.set_xlim([0,t[-1]*1/1e5*1e3])
axs.plot(t*1/1e5*1e3, current,color='tab:green',label='Normalized current')
axs.plot(t*1/1e5*1e3,target,'|',color='tab:orange', markersize=5)
axs.plot(t*1/1e5*1e3,pred,'+',color='tab:blue',markersize=1)
axs.set(xlabel=r'Time (ms)',ylabel=r'Arc current (a.u.)')
#axs.get_yaxis().set_label_coords(-0.15,0.5)
axs.set_ylim([-1.05,1.05])
