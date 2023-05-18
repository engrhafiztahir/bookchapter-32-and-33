#!/usr/bin/env python
# coding: utf-8

# In[4]:


computer_parts = {1:"Mouse",2:"Keyboard",3:"Mother Board", 4:"RAM", 5:"CPU", 6:"ROM", 7:"GPU"}
for computer_sub_parts in computer_parts.keys():
    print(computer_sub_parts)
for computer_sub_parts in computer_parts.values():
    print(computer_sub_parts)


# In[7]:


Computer_list = [ ] #Calling and empty list
computer_parts = {1:"Mouse",2:"Keyboard",3:"Mother Board", 4:"RAM", 5:"CPU", 6:"ROM", 7:"GPU"}
for computer_sub_parts in computer_parts.keys():
    Computer_list.append(computer_sub_parts)
    print(Computer_list)
    


# In[12]:


y = { }
a = {1:"Mouse",2:"Keyboard",3:"Mother Board", 4:"RAM", 5:"CPU", 6:"ROM", 7:"GPU"}
for x in a.keys():
    a[x] = y[x]
    print(y[x])


# In[17]:


computer_parts = {"one":"Mouse","two":"Keyboard","three":"Mother Board", "four":"RAM", "five":"CPU", "six":"ROM"}
for eachkey,eachvalue in computer_parts.items():
    print("The dictionary has kay " + eachkey + " and value is " + eachvalue)
    


# In[19]:


computer_parts = {1:"Mouse",2:"Keyboard",3:"Mother Board", 4:"RAM", 5:"CPU", 6:"ROM", 7:"GPU"}
for eachkey,eachvalue in computer_parts.items():
    eachkey = str(eachkey)
    print("The dictionary has kay " + eachkey + " and value is " + eachvalue)


# In[ ]:




