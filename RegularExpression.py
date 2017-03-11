
# coding: utf-8

# In[13]:

import re
example ="Nikhil is 21 and Soumya is 22. Sunil is 49 and my grandfather, Bhola is 68."


# example ='''
# Nikhil is 21 and Soumya is 22. My father, Sunil is 49 and ,my grandfather, Bhola is 68.
# '''

# In[14]:

ages = re.findall(r'\d{1,3}', example)
names = re.findall(r'[A-Z][a-z]*', example)


# In[15]:

print (ages)
print (names)


# In[16]:

x = 0
ageDict = {}

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
    
print (ageDict)



# In[ ]:



