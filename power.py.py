#!/usr/bin/env python
# coding: utf-8

# In[2]:


def power(base,exp):
    if(exp==1):
        return base
    else:
        return(base*power(base,exp-1))
base=int(input("enter base value"))
exp=int(input("enter exp value"))

print("result",power(base,exp))

