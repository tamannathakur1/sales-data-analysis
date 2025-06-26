#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales dataset
data = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 106],
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Frank'],
    'Product': ['Laptop', 'Tablet', 'Laptop', 'Monitor', 'Tablet', 'Monitor', 'Monitor'],
    'Amount': [50000, 15000, 50000, 12000, 15000, None, None],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Chennai', 'Chennai']
}

df = pd.DataFrame(data)
print(df)


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.tail()


# In[8]:


print(df.dtypes)


# In[9]:


print(df.isnull())


# In[10]:


print(df.fillna(0))


# In[11]:


df.describe()


# In[12]:


print(df.duplicated())


# In[14]:


print(df.drop_duplicates(inplace=True))


# In[21]:


print(df.columns)


# In[20]:


df.rename(columns={"Customer": "Customer_Name"},inplace = True)


# In[22]:


df.loc[2]


# In[23]:


df.iloc[1]


# In[25]:


print(df[df['Amount']>2000])


# # Profit by Product

# In[29]:


df.groupby('Product')['Amount'].sum().plot(kind='bar')

plt.title('Amount per Product')
plt.xlabel('Product')
plt.ylabel('Amount')
plt.show()


# In[9]:


df_clean = df_clean.drop_duplicates()             
df_clean['Cost'] = df_clean['Amount'] * 0.7       
df_clean['Profit'] = df_clean['Amount'] - df_clean['Cost'] 


# # Sales by City

# In[10]:


df_clean.groupby('City')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales by City')


plt.show()


# # Sales Trend

# In[11]:


df_sorted = df_clean.sort_values('Order_ID')

plt.plot(df_sorted['Order_ID'], df_sorted['Amount'], marker='o', color='royalblue')
plt.title('Sales Trend by Order ID')
plt.xlabel('Order ID')
plt.ylabel('Sales Amount (₹)')


plt.show()


# # Top Products by Profit

# In[13]:


top_products = df_clean.groupby('Product')['Profit'].sum().sort_values(ascending=False).head(3).plot(kind='bar', color="pink")


plt.title('Top 3 Profitable Products')
plt.xlabel('Product')
plt.ylabel('Profit (₹)')

plt.show()


# In[15]:


sns.barplot(x='Product', y='Profit', data=df_clean)
plt.title('Profit by Product')
plt.show()


# # using seaborn library

# In[17]:


import seaborn as sns

sns.barplot(x='Product', y='Profit', data=df_clean, color='red')
plt.title('Profit by Product')
plt.show()


# In[18]:


summary = df_clean.groupby('Product')[['Amount', 'Cost', 'Profit']].sum()
print(summary)


# In[19]:


plt.boxplot(df_clean['Amount'])
plt.title('Amount Distribution')
plt.ylabel('₹')
plt.grid(True)


plt.show()


# In[20]:


df_sorted = df_clean.sort_values('Order_ID')
df_sorted['Cumulative_Sales'] = df_sorted['Amount'].cumsum()

plt.plot(df_sorted['Order_ID'], df_sorted['Cumulative_Sales'], marker='o')


# # Order Count by City

# In[21]:


sns.countplot(x='City', data=df_clean, palette='pastel')
plt.title('Order Count by City')
plt.show()


# In[22]:


print("Key Insights:")
print("- Delhi had the highest sales overall.")
print("- Laptops generated the most revenue and profit.")
print("- Average profit margin is around 30%.")


# In[ ]:




