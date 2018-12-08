#!/usr/bin/env python
# coding: utf-8

# In[25]:


Input = "  the sky     is blue  "
Output= "blue is sky the"
word_list = Input.split(" ")
final_list = []
for word in word_list:
    if len(word) >= 1:
        final_list.append(word)
    

print(" ".join(final_list[::-1]))


# In[ ]:




