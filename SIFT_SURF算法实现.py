#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: admin
# datetime: 2022/8/10 14:41
# ide: PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#读取图像
img = cv.imread('test.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#sift关键点检测
sift =cv.xfeatures2d.SIFT_create()
kp,des=sift.detectAndCompute(gray,None)
#绘制检测结果
cv.drawKeypoints(img,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#图像显示
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('sift关键点检测')
plt.xticks([]),plt.yticks([])
plt.show()