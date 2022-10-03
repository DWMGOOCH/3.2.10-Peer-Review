#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Import the libraries.
import pandas as pd
import numpy as np

# Import the CSV file.
products = pd.read_csv('products.csv')

# View the DataFrame.
products


# In[14]:


products.columns


# In[10]:


# Question 1: How many products contain the word 'Fire' in their description? 
# lambda function to check if the word Fire appears in a product 
products[
    products['Description'].apply(lambda x:
                                 'Fire' in x.upper())
]


# In[20]:


# Question 1 cont: How many products contain the word 'Fire' in their description?
# Wanted to check if the above result was correct by running a user defined function
# User defined function to check if the word Fire appears in a product 
def contains_Fire(x):
    """ does the product contain Fire in the description? """
    y = x.lower()
    return "Fire" in y

ab = products['Description'].apply(contains_Fire)

# View the DataFrame.
print(ab)

# Filter the DataFrame.
products[ab]


# In[17]:


# Question 2: How many products contain the work 'candle' in their description?
# User defined fucntion to check if candle appears in a product description
def contains_candle(x):
    """ does the product contain candle in the description? """
    y = x.lower()
    return "candle" in y

# View the output.
# Test to see if user-defined function works
print(contains_candle(x="candle"))
print(contains_candle(x="Candle"))


# In[21]:


# Apply the function
cd = products['Description'].apply(contains_candle)

# View the DataFrame.
print(cd)

# Filter the DataFrame.
products[cd]


# In[22]:


# Question 3: How many products contain the word 'matches' in their description?
# lambda fucntion to test is matches appears in a product description
products[
    products['Description'].apply(lambda x:
                                 'matches' in x.lower())
]

