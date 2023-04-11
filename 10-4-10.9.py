#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Thing(): # the class is thing 
    pass # A empty code 
print(Thing) # creates two individual objects from the Thing  class
class example(): # Another class which is example 
    pass # an empy code 
print(example)  # creates two individual objects from the Thing  class
    
    
    


# In[14]:


class Element():
    def __init__(self, name, number, symbol): # Turns the Class Element into a Parent super class 
        self.name = name # the first object 
        self.number = number # the second object 
        self.symbol = symbol # the third object 
    def __str__(self):
        return "name={}, symbol={}, number={}".format(self.name, self.number, self.symbol) # returns the object names
element = Element('Hydrogen', 'H', 1) # declares the object 
print(element) # prints the object
    


# In[22]:


d = {
    "name": "hydrogen",
    "symbol": "H",
    "number": 1,
} # the dictionary 
    
    
hydrogen = Element(**d) # the object 
print(hydrogen) # returns the object
    


# In[25]:


class Bear(): # the first class 
    def eats(self):
        return 'A Bear eats Berries' # returns statement
class Rabbit(): # sub class 
    def eats(self):
        return 'A Rabbit eats CLovers' # returns statement 
class Octothorpe(): # Sub Class 
    def eats(self):
        return 'A Octothorpe eats Campers' # returns Sub Class
bear = Bear()
print(bear.eats())
rabbit = Rabbit()  
print(rabbit.eats())
octothorpe = Octothorpe()
print(octothorpe.eats())


# In[ ]:





# In[ ]:




