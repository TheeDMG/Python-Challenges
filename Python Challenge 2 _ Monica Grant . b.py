#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create basic calculations:
# Add two integers together. 
# What is the result?
# Subtract two integers. 
# What is the result?
# Divide two values. Have the result be an integer by using floor division. 
# What is the result?
# Create a variable ‘x’, have it’s value be 10+5. Print ‘x’. 
# What is the result?
# Create two strings and combine them using the + operator. 
# What was the result?
# Create variable ‘y’ and have the value be ‘program’. Omit letters o and g. Print the result.
# Create a list called ‘calendar_months’.
# How long is the list?
# Print only February, March, and April.
# Create a sample list of your choice, using string variables. 
# Create a second sample list of your choice, using string variables. 
# Create a third list that concats the two sample lists you created above.
# Remove one item from the third list. 
# Create a dictionary that has four keys and assign those keys values. 
# What is the length of the dictionary?


# In[1]:


# Create basic calculations:
# Add two integers together. 
2 + 3 


# In[2]:


# Subtract two integers. 
# What is the result?
18-12


# In[3]:


# Divide two values. Have the result be an integer by using floor division. 
# What is the result?

24//3


# In[4]:


# Create a variable ‘x’, have it’s value be 10+5. Print ‘x’. 
# What is the result?

x = (10+5)
print(x)


# In[7]:


# Create two strings and combine them using the + operator. 
# What was the result?

M = "Mo " 
G = "Money"
print(M + G)


# In[14]:


# Create variable ‘y’ and have the value be ‘program’. Omit letters o and g. Print the result.

y= 'program'


b = y[0:2]
c = y[4:]
print (b + c)




# In[15]:


# Create a list called ‘calendar_months’.
# How long is the list?
# Print only February, March, and April.

lst1 = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
print(len(lst1))


# In[16]:


print(lst1[1:4])


# In[50]:


# Create a sample list of your choice, using string variables. 
lst2 = 'Keith', "Krste", "Janice", 'Kim', 'Cedric' , "Nellis" , "Mignon" , "Glenn", "Mark"
lst3 = 'Darrin' , 'Nycole' , " Christopher" , "Monica" , " Menyon", "Amanda", "Tori", "Ashley", "Natalie" , "Andrew", "Shawnee", "Cedric"
lst4 =lst2 + lst3
print(lst4)



# In[52]:


# Remove one item from the third list.
t1 = lst4
# type (t1)
# print(t1)
# print(t1[0:3])
print(t1[0:18])
print(t1[19:])


# In[57]:


# Create a dictionary that has four keys and assign those keys values. 
# What is the length of the dictionary?

d = {"Gender": "female", "Grade": 12, "Sport": "Track", "GPA": 3.2}
len(d)


# In[59]:


e = {"Gender": "female", "Grade": 12, "Sport": ["Track", 'Soccer', 'Tennis', 'Volleyball'], "GPA": 3.2}
len(e)


# In[ ]:




