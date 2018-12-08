#!/usr/bin/env python
# coding: utf-8

# In[29]:


Input = "   -419 uk 3 with words"
#Input = "words and 987"

lt_list = []
for lt in Input:
    lt_list.append(lt)
print(lt_list)
#generate an iterator object
it_obj= iter(Input)
result_list = list()

for obj in it_obj:
    if not obj.isdigit():
        if obj == " ":
            continue
        elif obj == "-" or obj =="+":
            result_list.append(obj)
        else:
            if len(result_list) == 0:
                print(0)
            else:
                print(result_list)
            break
    elif obj.isdigit():
        result_list.append(obj)

