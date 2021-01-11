#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[1]:


import requests


# In[2]:


import bs4
from bs4 import BeautifulSoup


# In[3]:


url = 'https://www.in-berlin-brandenburg.com/Wohnen/Versorger/recyclinghoefe.html'


# In[5]:


headers = {
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


# In[6]:


r = requests.get(url, {'headers': headers})


# In[7]:


soup = bs4.BeautifulSoup(r.text,'html.parser')


# In[8]:


soup.find_all('div',{'class':'cards'})


# In[ ]:




