# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:45:32 2019

@author: Khumbelo

Generate a list of 50 unique integers between 100 and 534.
Find the minimum, maximum and median of the list 
Sort the list in Descending order
"""

import random
import statistics
Randomlist = []
i=0
while i<50:
    x = random.randint(100,534)
    if int(x) not in Randomlist:
        Randomlist.append(x)
    i+=1
    
print("Maximum value is : "+str(max(Randomlist)))
print("Minimum value is : "+str(min(Randomlist)))
print("Minimum value is : "+str(statistics.median(Randomlist)))
print("\n\nbefore sort")
print(Randomlist)
print("\n\nAfter sort")
Randomlist.sort(reverse=True)
print(Randomlist)