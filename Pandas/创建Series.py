# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:19:18 2017

@author: xiaoxiao
"""

import pandas as pd
import numpy as np


#   
a=pd.Series([8,8,7,6])#Series对象 默认索引是0,1,2,....
#print(a)

a=pd.Series([9,8,76,5],index=['a','b','c','d'])#自己写索引
#print(a)

#               创建Series类型
#    从标量值创建
s=pd.Series(2,index=['a','b','c'])#index必须写
#print(s)


#   从字典类型创建
d=pd.Series({'a':11,'b':23,'c':78})
d=pd.Series({'a':11,'b':23,'c':78},index=['f','b','e','d'])#index还可以改变结构，大小
#print(d)



#   从ndarray类型创建
n=pd.Series(np.arange(5))
n=pd.Series(np.arange(5),index=np.arange(9,4,-1))
#print(n)


#   Python列表创建,index与列表元素个数一致
a=pd.Series([8,8,7,6])#Series对象 默认索引是0,1,2,....





