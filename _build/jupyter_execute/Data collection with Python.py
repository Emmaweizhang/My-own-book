#!/usr/bin/env python
# coding: utf-8

# # Data collection and processing with Python

# ## Nested Data 

# In[1]:


#list
nested_list = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]  
for l in nested_list:
    print(l)


# In[2]:


# dictionary
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
info['personal_data']['physical_features']['color']


# JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists in python when we write them out as literals in a program, but with a few small differences (e.g., the word null instead of None). When your program receives a JSON-formatted string, generally you will want to convert it into a python object, a list or a dictionary.
# 
# **json.loads()** takes a string as input and produces a python object (a dictionary or a list) as output.
# 
# **json.dumps()** does the inverse of loads. It takes a python object (a dictionary or a list) and returns a string in JSON format.

# In[3]:


import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))   #'dict'
print(d.keys())
print(d['resultCount'])


# In[4]:


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))


# ## Nested Iteration

# In[5]:


nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)


# In[6]:


nested2 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested2:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)


# ## Deep and Shallow Copies

# When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change. We can see this happen in the following nested list, which only has two levels.

# In[7]:


original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)  #False
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)


# Assuming that you don’t want to have aliased lists inside of your nested list, then you’ll need to perform nested iteration. 
# 
# Or equivalently, you could take advantage of the slice operator to do the copying of the inner list.

# In[8]:


original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)


# In[9]:


original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)


# This process above works fine when there are only two layers or levels in a nested list. However, if we want to make a copy of a nested list that has more than two levels, then we recommend using the copy module. In the **copy** module there is a method called deepcopy that will take care of the operation for you.

# In[10]:


import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)


# ## Map

# In[11]:


def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)


# In[12]:


things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))


# ## Filter

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




