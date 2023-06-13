#!/usr/bin/env python
# coding: utf-8

# In[1]:


### class
"""
defines a new class
a real world concept
object oriented programming
"""

class Beer:
    def __init__(self):
        self.content = 1.0
    def drink(self):
        self.content = 0.0
        
becks = Beer() # constructor - creater class
becks.drink() # beer empty: b.content == 0

"""
Def defines a new function or class method
for class, the first parameter ("self") points to the class object.
when clalling class methodm first parameter is implicit
"""


# In[2]:


class Beer:
    def __init__(self, brand, content = 1.0):
        self.brand = brand
        self.content = content

    def drink(self, amount = 1.0):
        if self.content >= amount:
            self.content -= amount
            print(f"You drank {amount} of {self.brand}. Remaining content: {self.content}")
        else:
            print(f"Not enough {self.brand} left to drink that amount!")

    def check_content(self):
        return f"{self.content} of {self.brand} left to drink."

becks = Beer('Becks') # create a Beer object with 'Becks' brand

print(becks.check_content()) # Check how much is left

becks.drink(0.3) # Drink 0.3 of the content

print(becks.check_content()) # Check how much is left

becks.drink(0.8) # Try to drink more than what's left

print(becks.check_content()) # Check how much is left

becks.drink() # Finish off whatever's left


# In[ ]:




