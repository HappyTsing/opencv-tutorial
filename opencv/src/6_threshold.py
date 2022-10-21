import cv2
import numpy as np
from loguru import logger
"""
@Description 阈值，阈值的思想是进一步简化视觉数据的分析。

首先，图片转换为灰度，但是你必须考虑灰度仍然有至少 255 个值。而阈值可以做的事情（THRESH_BINARY），是将图片转换为两个颜色: 0, maxval
Example:
阈值为 125（maxval = 255），那么 125 以下的所有内容都将被转换为 0，也就是黑色，而高于 125 的所有内容都将被转换为 255，即白色。

如果将图片成灰度图，在进行阈值操作，图片会变成白色和黑色。如果采用彩图，你会得到二值化的图片，但会有颜色。
"""

img = cv2.imread('img/bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.threshold() 参数: (图像，阈值，maxval, type)
# maxval: 填充值。当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值（当type指定为THRESH_BINARY或THRESH_BINARY_INV时，需要设置该值）
# type: 二值化操作的类型，包含以下5种类型：
#   cv2.THRESH_BINARY； 
#   cv2.THRESH_BINARY_INV；
#   cv2.THRESH_TRUNC；
#   cv2.THRESH_TOZERO；
#   cv2.THRESH_TOZERO_INV
# References: https://www.jianshu.com/p/f58dcffdcb30

# 1. 彩色图比较。一般都会比较灰度图。此处只是举例
# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# 2. 灰度图
# retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)

# 3. 自适应阈值
threshold = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# 4. 大津阈值，此处效果并不好
# retval2,threshold = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()