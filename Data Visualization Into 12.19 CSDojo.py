#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###This project done as I followed along with the example on CSDojo ###


# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[5]:


x = [1,2,3]
y = [1,4,9]
z = [10,5,0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("Test")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[6]:


sample_data = pd.read_csv('sample_data.csv')


# 

# In[9]:


type(sample_data)
type(sample_data.column_c)


# In[10]:


sample_data.column_c.iloc[1]


# In[14]:


plt.plot(sample_data.column_a,sample_data.column_b, "o")
plt.plot(sample_data.column_a,sample_data.column_c, "o")
plt.show()


# In[16]:


data = pd.read_csv("countries.csv")


# In[ ]:


# comparing pop growth between the United States and China


# In[18]:


us = data[data.country == 'United States']
China = data[data.country == 'China']


# In[25]:


#gonna divide the population column by 1000000 to get yaxis in understandable units
plt.plot(us.year, us.population / 10**6)
plt.plot(China.year, China.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel("Years")
plt.ylabel("Population in Millions")
plt.show()


# In[26]:


us.population


# In[28]:


us.population / us.population.iloc[0] * 100


# In[29]:


#growth per percent
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(China.year, China.population / China.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel("Years")
plt.ylabel("Population Growth")
plt.show()

