#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[86]:


marketing_costumer = pd.read_csv(r"C:\Users\Utilizador\Desktop\Labround3\lab-customer-analysis-round-3\files_for_lab\csv_files\marketing_customer_analysis.csv")
marketing_costumer


# In[87]:


marketing_costumer.info()


# In[88]:


cols = []
for i in range(len(marketing_costumer.columns)): 
    cols.append(marketing_costumer.columns[i].lower().replace(' ', '_'))
marketing_costumer.columns = cols
marketing_costumer


# In[89]:


marketing_costumer.describe()


# In[90]:


plt.hist(marketing_costumer['response'])
plt.xlabel('Count')
plt.ylabel('Response')
plt.title('Total Number of Responses')
plt.show()


# In[91]:


marketing_costumer.groupby('sales_channel')['response'].value_counts(normalize=True).unstack().fillna(0)
plt.hist(marketing_costumer['sales_channel'])
plt.xlabel('Sales Channel')
plt.ylabel('Response Rate')
plt.title('Response Rate by Sales Channel')
plt.show()


# In[101]:


marketing_costumer.groupby('total_claim_amount')['response'].value_counts(normalize=True).unstack().fillna(0)
plt.hist(marketing_costumer['total_claim_amount'], bins=10, edgecolor='k')
plt.xlabel('Total Claim Amount')
plt.ylabel('Response Rate')
plt.title('Response rate by the total claim amount')
plt.show()


# In[105]:


marketing_costumer.groupby('income')['response'].value_counts(normalize=True).unstack().fillna(0)
sns.histplot(marketing_costumer['income'])
plt.show()


# In[ ]:




