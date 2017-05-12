# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
def pySum():
    a=[1,2,3,4,5]
    b=[6,7,8,9,10]
    c=[]
    
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
        
    return c
print(pySum())
    
