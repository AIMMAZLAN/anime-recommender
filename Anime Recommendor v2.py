#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[2]:


#make API call
url = "https://api.jikan.moe/v4/anime"
r = requests.get(url).json()


# In[3]:


#build dataframe
df = pd.DataFrame(columns=["anime_title", "genre", "total_eps", "rating_score", "anime_status"])


# In[4]:


for anime in r["data"]:
    anime_title = anime['titles'][0]['title']
    genre = anime['genres'][0]['name']
    total_eps = anime['episodes']
    rating_score = anime['score']
    anime_status = anime['status']
    
    #save data in pandas df
    df = df.append({"anime_title": anime_title, "genre": genre, "total_eps": total_eps,
                  "rating_score": rating_score, "anime_status": anime_status},ignore_index=True)


# In[5]:


df.head()


# In[6]:


y = 'Name: ' + df.anime_title.astype(str) + '  Genre: ' + df.genre.astype(str) + '  Total eps: ' + df.total_eps.astype(str) + '  Status: ' + df.anime_status.astype(str) 


# In[7]:


from random import choice


# In[8]:


#random anime choice
print(choice(y))

