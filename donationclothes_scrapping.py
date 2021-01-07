#!/usr/bin/env python
# coding: utf-8

# In[46]:


from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

url = "https://allaboutberlin.com/guides/donate-clothes"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(urlopen(req).read(), "html.parser")
main_tag = soup.find('div', {'class': 'article-body'})
ul_tag = main_tag.find_all('ul')[1]

association_tags = main_tag.findAll('li')

links_set = set()

for list_item in association_tags:
    list_item_strong = list_item.find('strong')
    list_item_anchor = list_item.find('a')
    list_item_em = list_item.find('em')

    if list_item_anchor is not None:
        links_set.add(list_item_anchor.get('href'))

    if list_item_strong is not None:
        strong_anchor = list_item_strong.find('a')
        if strong_anchor is not None:
            links_set.add(strong_anchor.get('href'))

    if list_item_em is not None:
        em_anchor = list_item_em.find_all('a')[0]
        if em_anchor is not None:
            links_set.add(em_anchor.get('href'))

print(len(links_set))

for each in links_set:
    print(each)


# In[ ]:





# In[ ]:




