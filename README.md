# Numpy库

# matplotlib库

[matplotlib库：可用于数据可视化](https://matplotlib.org/gallery.html)

[pandas库](http://pandas.pydata.org/)

Matplotlib库




## ndarry

# n维数组对象，所有元素类型相同
np.ndarry([1,2],[3,4]);

**使用NumPy函数创建ndarray数组**
np.arange(10)

np.ones(shape) x=np.ones((3,6))//三行六列   x.shape是(3,6)

np.zeros(shape)

np.eye(5)//正方的N*N单位矩阵，对角线1，其余0

np.ones_like(a)//根据数组a的形状生成一个全1的数组

np.zeros_like(a)

np.full_like(a,val)//根据数组a的形状生成一个全val的数组

np.linspace(1，10，4)//根据起始数据等间距地填充数组  结果array([1.,4.,7.,10.])

np.linspace(1，10，4,endpoint=False)//结果array([1.,3.25,5.5,7.75])

np.concatenate(a,b)//将多个数组合并成一个数组

**ndarray维度变换**

.reshape(shape)//返回一个新数组，原数组不变

.resize(shape)//原数组改变

.flatten()//原数组改变，成为一维数组

**类型改变**

.astype(np.float)

**转换成列表**

.tolist()

**索引**

//一维a[0]   //多维a[1,3,2]//每个维度一个索引

**切片**

//一维a[1:4:2]//起：终(不含):步长  

//多维a[:,:,::2]//三个维度上，::2是第三维度上的跳跃步长

**运算**

a.mean()

np.cos()//每个元素cos

## 数据存储和读取

**csv只能有效存储一维和二维数组**
np.savetxxt('a.csv',array,fmt='%d',delimiter=',')//分割字符串是,

np.loadtxt('a.csv',delimiter=',')

**多维数据存取**

a.tofile('a.scv',sep=',',dormat='%d')

np.fromfile('a.csv',dtype=float,count=-1,sep=',')//count为-1代表读入整个文件

np.save("a.npy",a)

b=np.load("a.npy")





## Series   一组数据与之相关的数据索引组成,索引从0开始
pd.Series([9,8,7,6])


**从标量值创建**
pd.Series(25,index=['a','b'])//index不能省略,每一项都是25

**从字典类型创建**
pd.Series({'a':9,'b':1})   pd.Series({'a':9,'b':1},index=['c','a'])//这里index只是从字典中进行选择，没有的显示NaN，比如索引c对应NaN

**从ndarray创建**

pd.Series(np.arange(5),index=np.arange(9,4,-1))//数据从0到5，index省略时为0-5，这里索引是9到5，步长1

##排序

a=pd.DataFrame(np.arange(20).reshape(4,5),index=['a','b','c','d'])

a.sort_values(2,ascending=False)//第2轴，就是第三列，降序   NaN统一放到末尾

##基本的统计分析函数
a.describe()

##数据的累积分析
.cummsum()//每个元素都是此位置加上上一行同位置元素之和
.cumprod()//每个元素都是此位置与上一行同位置元素之乘积
.cummin()//每个元素都是此列最小值
.cummiax()//每个元素都是此列最大值

**滚动计算**

.rolling(w).sum() //依次计算相邻w个元素（纵着看）的和

.rolling(w).mean()

.rolling(w).var()//方差

.rolling(w).std()//标准差

.rolling(w).min()

.rolling(w).max()

##数据的相关分析  (两个事物正相关、负相关、不相关)

**可以用协方差来判断**

**Pearson相关系数，【-1，1】**

.cov()//计算协方差矩阵

.corr()//计算相关系数矩阵，Pearson等系数

例如，a.corr(b)就可以得到一个[-1,1]范围的Pearson系数值










   




