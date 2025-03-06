#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'


# In[5]:


page = requests.get(url)


# In[6]:


soup = BeautifulSoup(page.text, 'html')


# In[7]:


print(soup)


# In[8]:


table = soup.find_all('table')[1]

print(table)


# In[9]:


soup.find_all('th')


# In[10]:


world_titles = table.find_all('th')


# In[11]:


world_titles


# In[12]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[15]:


column_data = table.find_all('tr')


# In[16]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data


# In[17]:


df


# In[21]:


df.to_csv(r'C:\Users\DELL\Documents\Python Webscraping Project\companies.csv', index = False)


# In[ ]:




