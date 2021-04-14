#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


data = pd.read_csv ("D:/Code/EDA/StudentsPerformance.csv")


# In[8]:


data.head()


# In[10]:


data.shape


# In[11]:


data.tail()


# In[13]:


data.describe()


# In[14]:


data.columns


# In[15]:


data.nunique()


# In[21]:


data['race/ethnicity'].unique()


# In[23]:


data.isnull().sum()


# In[25]:


StudentsPerformance = data.drop(['race/ethnicity', 'parental level of education'], axis=1)


# In[27]:


StudentsPerformance.head()


# In[30]:


corelation = StudentsPerformance.corr()


# In[31]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)


# In[32]:


sns.pairplot(StudentsPerformance)


# In[39]:


sns.relplot(x='math score', y='reading score', hue='gender', data=StudentsPerformance)


# In[ ]:





# In[37]:


sns.displot(StudentsPerformance['math score'], bins=10)


# In[38]:


sns.catplot(x="math score", kind="box", data=StudentsPerformance)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




