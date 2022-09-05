#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('ratings.csv')
df.head(10)


# In[3]:


movie_titles=pd.read_csv("movies.csv")
movie_titles.head(10)


# In[4]:


df=pd.merge(df,movie_titles,on='movieId')
df.head()


# In[5]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head(10)


# In[6]:


ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# In[7]:


moviemat = df.pivot_table(index='userId',columns='title',values='rating')
moviemat.head(10)


# In[8]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# In[9]:


Jurassic_Park_userrating=moviemat['Jurassic Park (1993)']
Jurassic_Park_userrating.head(10)


# In[10]:


similar_to_Jurassic_Park = moviemat.corrwith(Jurassic_Park_userrating)
similar_to_Jurassic_Park.head(10)


# In[11]:


corr_Jurassic_Park = pd.DataFrame(similar_to_Jurassic_Park,columns=['Correlation'])
corr_Jurassic_Park.dropna(inplace=True)
corr_Jurassic_Park.head(10)


# In[12]:


corr_Jurassic_Park.sort_values('Correlation',ascending=False).head(10)


# In[13]:


corr_Jurassic_Park = corr_Jurassic_Park.join(ratings['num of ratings'])
corr_Jurassic_Park.head()


# In[14]:


corr_Jurassic_Park[corr_Jurassic_Park['num of ratings']>100].sort_values('Correlation',ascending=False).head(20)