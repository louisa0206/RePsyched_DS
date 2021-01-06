#!/usr/bin/env python
# coding: utf-8

# In[23]:


from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

url = "https://www.bsr.de/die-berliner-stadtreinigung-in-englischer-sprache-26142.php"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(urlopen(req).read(), "html.parser")
#main_tag = soup.find('div', {'class': 'container'})
next_main_tags = soup.find_all('div', {'class': 'mod mod-text-img'})
#text_main_tags = soup.find_all('div', {'class': 'mod mod-listing'})
#text_data = text_main_tags.find('div', {'class': 'wysiwyg'})

for next_main_tag in next_main_tags:
    #print('\n\n', next_main_tag, '\n')
    header= next_main_tag.find_next('h3')
    print(header.text)
    listing = next_main_tag.find_next('div', {'class': 'mod mod-listing'})
    #print(listing)
    description_listings = listing.find_all('div', {'class': 'wysiwyg'})
    #print(description_listings)
    for description_listing in description_listings:
        paragraphs = description_listing.findAll('p')
        for paragraph in paragraphs:
            print(paragraph.text)
        
    #for paragraph in text_data:
        #belongings = paragraph.find_next('p')
        #print(belongings.text)
    


# In[ ]:





# In[ ]:




