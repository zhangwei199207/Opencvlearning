#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: admin
# datetime: 2022/8/10 11:15
# ide: PyCharm
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#读取图像，并装换成灰度图
img = cv.imread('test.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#角点检测
gray = np.float32(gray)
#最后一个参数在0.04到0.05之间
dst = cv.cornerHarris(gray,2,3,0.04)
#设置阈值，将角点检测出来，阈值根据图像进行选择
img[dst>0.001*dst.max()]=[0,0,255]
#图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('Marris角点检测')
plt.xticks([]),plt.yticks([])
plt.show()