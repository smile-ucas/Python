# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:47:42 2017

@author: xiaoxiao
"""
import pandas as pd
#基于索引的运算，更精确    它是一维带标签的数组

#series+series
a=pd.Series([1,2,3],['c','d','e'])
b=pd.Series([9,8,7],['a','b','c'])
print(a+b)  #Series在运算时会自动对齐不同索引的数据

