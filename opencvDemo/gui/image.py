'''
cv.imread（）
cv.imshow（）
cv.imwrite（）
Matplotlib
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('xiaohua.jpg', 1)
print(img.shape)

# cv.imshow('校花', img)
# cv.waitKey(0)

# cv.imwrite('xiaohua.png', img)


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])   #隐藏X和Y轴上的刻度值
plt.show()