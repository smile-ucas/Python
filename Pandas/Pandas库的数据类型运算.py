# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:00:22 2017

@author: xiaoxiao
"""

import pandas as pd
import numpy as np

#Pandas库的数据类型运算
a=pd.DataFrame(np.arange(12).reshape(3,4))
b=pd.DataFrame(np.arange(20).reshape(4,5))
#print(a)
#print(b)
#
#print(a+b)
#print(b.add(a,fill_value=100))
#print(a*b)
#print(a.mul(b,fill_value=0))
##fill_value参数可以替代NaN,替代后参与运算（方法运算）



#不同维度之间的运算
b=pd.DataFrame(np.arange(20).reshape(4,5))
c=pd.Series(np.arange(4))
print(b)
print(c)
print(c-10)#官博运算：低维的都作用到高维的每一个数上
print(b-c)




