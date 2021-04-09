
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[8]:


# Load data from csv file into a pandas data frame
df = pd.read_csv("data.csv")
df.columns = ["year", "rank", "company", "revenue", "profit"]
print("Total number of records: {}".format(df.shape[0]))


# In[9]:


# convert profit columns to numeric and filter nas
df.profit = df['profit'].apply(pd.to_numeric, errors='coerce')
df = df[~df['profit'].isna()]
print("Total number of records after filtering non-numeric profit: {}".format(df.shape[0]))


# In[10]:


# Sort by profit and print top 20 rows
print("Top 20 records sorted by profit in descending order")
print(df.sort_values(by='profit', ascending=False).head(20).to_string(index=False))


# In[12]:


#Writing the dataframe to a file in json format
df.to_json(r'data2.json', orient='table')

