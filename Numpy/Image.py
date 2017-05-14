# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:35:52 2017

@author: xiaoxiao
"""

from PIL import Image
import numpy as np


im=np.array(Image.open("三生三世.png"))
print(im.shape,im.dtype)#三维数组，高、宽、像素的RGB值  结果是(395, 687, 3) uint8

b=[255,255,255]-im

newIm=Image.fromarray(b.astype('uint8'))#生成一个新的图像对象
newIm.save('新三生三世.png')

im=np.array(Image.open("三生三世.png").convert('L'))
b=255-im
newIm=Image.fromarray(b.astype('uint8'))#生成一个新的图像对象
newIm.save('新三生三世_灰.png')