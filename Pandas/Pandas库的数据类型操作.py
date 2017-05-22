# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:38:20 2017

@author: xiaoxiao
"""
import pandas as pd


#重新索引 .reindex()能改变或重排Series和DataFrame索引
#d是之前写的DataFrame类型,
d.reindex(index=['d','b','a'])#行按这个索引顺序排列
d.reindex(columns=['two','one'])#列按这个索引顺序排列
#.reindex()有许多参数 可以增加行列索引及内容值


#.drop()删除指定索引对象  删除Series和DataFrame指定行或列索引
d.drop(['d','e'])#删除b,c两行
#DataFrame有多列（即多轴）,默认删除零轴，可以通过axis控制是哪一个轴
d.drop('同比',axis=1)#删除DataFrame的1轴,即第二列

        



