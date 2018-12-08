#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numerator = 4
denominator = 3

result = numerator/denominator
str_result = str(result)
str_num = []

if numerator%denominator == 0:
    print(int(result))
for idxx, num in enumerate(str_result):
    str_num.append(num)
idx = str_num.index(".")
counter_dict = {}
for num in str_num[(idx+1):]:
    if num in counter_dict.keys():
        counter_dict[num] += 1
    else:
        counter_dict[num] = 1

result_list = []
if len(str_num[idx:])-1 == counter_dict[num]:
    #lst_num = "(" +str(counter_dict[num])
    left_part = "".join(str_num[: idx+1])
    final_part = left_part + "(" + str_num[idx+2]+ ")" 
    print(final_part)
else:
    print(str_result)

