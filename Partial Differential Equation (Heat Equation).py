#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[30]:


h = 0.025
k = 0.025
x = np.arange(0,1+h,h).round(3)
t = np.arange(0,0.1+k,k).round(3)

boundaryCond = [0,0]
initialCond = np.sin(np.pi*x)

n = len(x)
m = len(t)
T = np.zeros((n,m))
T[0,:] = boundaryCond[0]
T[-1,:] = boundaryCond[1]
T[:,0] = initialCond

factor = k/h**2
for j in range(1, m):
    for i in range(1, n-1):
       T[i,j] = factor*T[i-1,j-1] + (1-2*factor)*T[i,j-1] + factor*T[i+1,j-1]


# In[31]:


plt.plot(T)
plt.legend(t)
plt.xlabel('distance')
plt.ylabel('temperature')


# In[ ]:




