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
'''print(pySum())'''
    
#创建nparray
a = np.array([11,2,2])
b = np.arange(3) #默认整数类型
c = np.ones((3,6)) #默认浮点类型
d = np.zeros((3,6)) #默认浮点类型
e = np.full((2,3),9,int)
f = np.eye(5) #默认浮点类型
'''print(a)
print(b)
print(c)
print(d)
print(e)
print(f)'''
np.ones_like(a)
np.zeros_like(a)
np.full_like(a,9)
'''print(np.ones_like(a))
print(np.zeros_like(a))
print(np.full_like(a,9))'''
np.linspace(1,10,4)
np.linspace(1,10,4,endpoint=False)
np.concatenate((d,c))#必须是相同维度的

a=np.ones((2,3,4),dtype=np.int)
b=a.reshape((3,8))#不改变原数组
a.resize((3,8))#改变原数组
a.tolist()#数组向列表转换
c=a.flatten()  #不改变原数组,降维成一维  
d=c.astype(np.float)     #即使两个类型一致，astype也会创建一个新的数组
'''print(d)'''

#一维数组索引
a=np.array([9,8,7,6,5])
a[1:4:2]#前闭后开，第三个参数是步长
#二维数组索引
a=np.arange(24).reshape((2,3,4))
#a(1,2,3)#三个参数各指从外到内的维度 结果：23
#a(-1,-2,-3)#负数倒着数 倒数第一个倒数第二个 倒数第三个  结果：17 
 #多维数组的切片
a[:,1:2,:]#第二个参数前闭后开
a[:,:,::2]#跳跃步长

 
#Numpy一元函数
a.mean()#数组a中所有元素加起来后的平均值

      
      #                 csv只能有效存储一维和二维数组
#生成一个csv文件
a=np.arange(100).reshape((5,20))
np.savetxt('a.csv',a,fmt='%d',delimiter=',')      
#读入一个csv
b=np.loadtxt('a.csv',delimiter=',')
#print(b)
b=np.loadtxt('a.csv',dtype=np.int,delimiter=',')
#print(b)
      
      
     #          任意维度的数据的存储
a=np.arange(100).reshape(5,10,2)
#print(a)     
a.tofile("b.bat",sep=",",format='%d')          
a.tofile("b_binary.bat",format='%d')     #sep不写，为空串，生成的文件是二进制文件 
      
a=np.fromfile("b.bat",dtype=np.int,sep=",").reshape(2,10,5)
#print(a)      
      
      
      # Numpy的方式
a=np.arange(100).reshape(5,10,2)
np.save('a.npy',a)
b=np.load('a.npy')
#print(b)
      


     #          np.random的随机数函数
a=np.random.rand(3,4,5)
#print(a)
sn=np.random.randn(3,4,5)
#print(a)
a=np.random.randint(100,200,(3,4))
#print(a)




np.random.seed(1)  #使两个同样方式生成的数组是一样的
a=np.random.randint(100,200,(3,4))
print(a)
np.random.seed(1)
a=np.random.randint(100,200,(3,4))
print(a)




            #Numpy的统计函数


            #Numpy的梯度函数  只有一个np.gradient(f)
              
              