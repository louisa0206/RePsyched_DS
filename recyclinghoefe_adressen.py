# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#pip install bs4


# %%
#pip install pandas


# %%
import requests
import bs4
import pandas as pd 
from bs4 import BeautifulSoup


# %%
url = 'https://www.berlin.de/special/immobilien-und-wohnen/adressen/recyclinghof/'


# %%
headers = {
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


# %%
r = requests.get(url, {'headers': headers})


# %%
soup = bs4.BeautifulSoup(r.text,'html.parser')


# %%
recyclinghoefe_adressen = {}
adresse_no = 0


# %%
items = soup.find_all('span',{'class':'address'})


# %%
for item in items:
        
        adressen = item.get_text()
        print(adresse_no, adressen)
    
        adresse_no +=1
        
        recyclinghoefe_adressen [adresse_no] = [adressen]
    
    
print (recyclinghoefe_adressen)


# %%
recyclinghoefe_adressen_df = pd.DataFrame.from_dict(recyclinghoefe_adressen, orient = 'index', columns = ['Adresse'])


# %%
recyclinghoefe_adressen_df.to_csv('recyclinghoefe_adressen.csv')


# %%



