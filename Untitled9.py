#!/usr/bin/env python
# coding: utf-8

# In[51]:


from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

url = "https://allaboutberlin.com/guides/sorting-trash-in-germany#everything-else"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(urlopen(req).read(), "html.parser")
main_tag = soup.find('div', {'class': 'article-body'})
headers = main_tag.find_all('h3')

for header in headers[1:]:
    print('\n\n', header.text, '\n')
    list = header.find_next('ul')
    list_items = list.findAll('li')
    for list_item in list_items:
        print(list_item.text)


# In[ ]:




