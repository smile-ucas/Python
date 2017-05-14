# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:54:44 2017

@author: xiaoxiao
"""
import numpy as np
import matplotlib.pyplot as plt

#plt.plot([2,3,4,1,6]) #一维数组这个是y轴的数据   这里x轴是索引
plt.ylabel("grade")
plt.savefig('test',dpi=600)#默认png
#plt.show()


#plt.plot([2,4,6,8,9],[12,23,30,4,5])#二维数组，第一个是x轴  第二个是y轴
plt.ylabel('grade')
#plt.axis([-2,10,0,30])#分别对应x,y轴的起始、终止值
#plt.show()




#绘图区域  plt.subplot(3,2,4)
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
a=np.arange(0.0,5.0,0.02)
#plt.subplot(2,3,5)
#plt.plot(a,f(a))
#plt.show()


#同时绘制多条曲线
a=np.arange(10)
#plt.plot(a,a*7,a,a*10,a,a*12,a,a*15)
plt.plot(a,a*7,'ro-',a,a*10,'b*',a,a*12,'x',a,a*15,'b-.')#加曲线风格
plt.show()

























