#!/usr/bin/env python
# coding: utf-8

# In[1]:


dividend = 10
divisor = -3
abs_dividend = abs(dividend)
abs_divisor = abs(divisor)
counter = abs_divisor
result = 0
while divisor != 0 and counter < abs_dividend:
    result += 1
    counter += abs_divisor 

if abs_dividend == abs_divisor:
    result = 1
elif dividend < 0 or divisor < 0:
    result = -result
elif dividend < 0 and divisor < 0:
    result = result
else:
    result = result

print(result)

