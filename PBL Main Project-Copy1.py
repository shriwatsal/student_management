#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import tabula as tb
from matplotlib import pyplot as plt


# In[3]:


df = tb.read_pdf(r"/Users/rajdeep/Desktop/PBL/Result_Main.pdf",pages='all')
tb.convert_into(r'/Users/rajdeep/Desktop/PBL/Result_Main.pdf', r'/Users/rajdeep/Desktop/git-folder/outputmain.csv' , output_format="csv",pages='all', stream=True)


# In[5]:


data = pd.read_csv(r"/Users/rajdeep/Desktop/git-folder/outputmain.csv")


# In[6]:


data


# In[7]:


data.columns


# In[8]:


data.tail()


# In[9]:


#To find average score of each subject
a=input("Enter the subject of which you want average score\n")
data[a].mean()


# In[8]:


#How many students have given the exam..
a=input("Enter the subject of which you want to how many students have attended it\n")
data[a].count()


# In[19]:


#Minimum scores subjectwise
a=input("Enter the subject you want to know minimum score of\n")
data[a].min()


# In[21]:


#to show how many people have scored how much marks in particular subject
a=input("Enter the subject you want count of\n")
b=data[a].value_counts()
print(b)


# In[22]:


#Graphical representation of how many scored how much marks in particular subject
a=input("Enter subject name you want graph of\n")
sns.distplot(data[a]);


# In[25]:


# To find the topper of subject.
c=input("Enter the subject you want\n")
topper = data[data[c]==max(data[c])]


# In[26]:


print(topper)


# In[27]:


#To find about failed students considering 15 or less score is fail
a=input("Enter the subject name of which you want to find failed students\n")
failed = data[data[a]<=15] 


# In[28]:


print(failed)

