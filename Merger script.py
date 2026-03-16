#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import os
from glob import glob


# In[2]:


df=pd.read_csv('March_transactions-Copy1.csv')
df2=pd.read_csv('20260316050455-ADMIN REPORT.csv')
df3=pd.read_csv('20260316050821-ADMIN REPORT.csv')
df4=pd.read_csv('20260316055253-ADMIN REPORT.csv')


# In[3]:


for df_temp in [df, df2, df3, df4]:
    df_temp.columns = df_temp.columns.str.strip().str.lower().str.replace(" ", "_")


# In[6]:


for df_temp in [df, df2, df3, df4]:
    df_temp['transaction_date'] = df_temp['transaction_date'].astype(str).str.strip()


# In[7]:


df = pd.concat([df, df2, df3, df4], ignore_index=True)
print(f"Total merged rows: {len(df)}")


# In[8]:


df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')


# In[9]:


missing_dates = df['transaction_date'].isna().sum()
print(f"Rows with missing transaction_date: {missing_dates}")


# In[10]:


df['month'] = df['transaction_date'].dt.month
df = df[df['month'] == 3].copy()


# In[11]:


print(f"March date range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
print(f"March rows: {len(df)}")


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


output_path = r"C:\Users\StephenNgungi\march transactions\march_1_to_15_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"Cleaned merged dataset saved to: {output_path}")


# In[ ]:




