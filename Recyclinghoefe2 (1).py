#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[3]:


import requests


# In[4]:


import bs4
from bs4 import BeautifulSoup


# In[5]:


url = 'https://www.berlin.de/special/immobilien-und-wohnen/adressen/recyclinghof/'


# In[6]:


headers = {
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


# In[7]:


r = requests.get(url, {'headers': headers})


# In[8]:


soup = bs4.BeautifulSoup(r.text,'html.parser')


# In[11]:


adressen = soup.find_all('span',{'class':'address'})


# In[12]:


print(adressen)


# In[15]:


print adressen.replace("<strong>","")


# In[19]:


import csv


# In[20]:


csvFile = open('reclyclinghoefe_adressen.csv', 'w+', newline='')


# In[23]:


try:
    writer = csv.writer(csvFile)
    writer.writerow(('Straße + Hausnr','Plz + Stadt'))
finally: csvFile.close()


# In[ ]:




