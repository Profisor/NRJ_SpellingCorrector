
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import re
from collections import Counter


# In[2]:


os.chdir("C:/Users/NIRANJAN REDDY/Desktop/Data/NLP-master/NLP-master")


# In[3]:


data=pd.read_csv("sentences.csv")


# In[4]:


data


# In[5]:


data.rename(columns={'comment_id':'id','comment_message':'reviews'},inplace=True)


# In[6]:


data


# In[7]:


def words(text): return re.findall(r'\w+', text.lower())


# In[8]:


data = Counter(words(open('sentences.csv').read()))


# In[9]:


len(data)


# In[10]:


Counter(data)


# In[11]:


def P(word, N=sum(data.values())): 
    "Probability of `word`."
    return data[word] / N


# In[12]:


def correction(word): 
    "Nearest probability of the word."
    return max(candidates(word), key=P)


# In[13]:


def candidates(word): 
    "Create nearest spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


# In[14]:


def known(words): 
    "The subset of `words` which we will find in the dictionary of data."
    return set(w for w in words if w in data)


# In[15]:


def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


# In[16]:


def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))



# In[18]:


correction('vater')


# In[19]:


correction('smyle')


# In[20]:


correction('sae')


# In[21]:


correction('myke')


# In[23]:


correction('aplycation')


# In[24]:


correction('sam')


# In[25]:


correction('syme')


# In[26]:


correction('lyttle')


# In[64]:


correction('floood')


# In[28]:


correction('sylk')


# In[31]:


correction('kool')


# In[37]:


correction('myn')


# In[45]:


correction('juyce')


# In[51]:


correction('feeet')


# In[52]:


correction('chyll')


# In[62]:


Accuracy= 13.0/15


# In[63]:


print(Accuracy)

