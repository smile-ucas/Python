# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:54:10 2017

@author: xiaoxiao
"""

#DataFrom表格型数据类型 由共用相同索引的一组列组成

import pandas as pd
import numpy as np

#从二维ndarray对象创建  
d=pd.DataFrame(np.arange(10).reshape(2,5))
#print(d)

#从一维ndarray对象字典创建
dt={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([6,7,8,3],index=['a','e','c','d'])}
d=pd.DataFrame(dt)
#print(d)#one,two两个字典对应DataFrom的两列，字典的索引就是DataFrame的每行索引，DataFrame的每列是one,two
d=pd.DataFrame(dt,index=['b','e','a'],columns=['two','three'])
#print(d)

#用列表类型的字典来创建
dl={'one':[1,2,3,4],'two':[5,6,7,8]}
d=pd.DataFrame(dl,index=['a','b','c','d'])
print(d)
print(d.index)
print(d.columns)
print(d.values)
#获取一行
print(d.ix['c'])
#获取一列
print(d['two'])
print(d['one']['d'])


            #DataFrame的基本操作类似于Series，依据行列索引


