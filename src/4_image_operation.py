import numpy as np
import cv2
from loguru import logger
"""
@Description 简单的图像操作

cv2.imread 读取后的图片被表示为一个 numpy.ndarray 类型的对象，其秩的维数为 3。
以左上角为原点，通过 img[高度值，宽度值]，可以获取对应点的像素。
    cv2.IMREAD_COLOR:     每个像素点是秩 = 1的数组，即[R,B,G]，三色通道。R|B|G -> 0~255
    cv2.IMREAD_GRAYSCALE: 每个像素点是一个int8的数字，其范围是 0~255 表示黑色的深度
"""
img = cv2.imread('img/snowman.png',cv2.IMREAD_COLOR)

# 获取高度为20，宽度为30位置处的像素
px = img[20,30]
logger.info("像素点颜色: {}".format(px))

# 修改该像素点的颜色
img[55,55] = [255,255,255]

# 修改高度 100:150 ，宽度 100:150 这块正方形内的所有像素的颜色，改为白色。
img[100:150,100:150] = [255,255,255]


# ndarray.shape 数组的维度，对于opencv:
#       cv2.IMREAD_COLOR:     (高度像素, 宽度像素, 通道数)
#       cv2.IMREAD_GRAYSCALE: (高度像素, 宽度像素)
# 
# ndarray.size 数组元素的总个数, 等于 ndarray.shape 中所有值相乘
#
# ndarray.dtype 数组对象的元素类型，此处用 unit8 存储，因为颜色的范围是 0~255
logger.info("IMREAD_COLOR img.shape: {}".format(img.shape))
logger.info("IMREAD_COLOR img.size: {}".format(img.size))
logger.info("IMREAD_COLOR img.dtype: {}".format(img.dtype))

img_gray = cv2.imread('img/snowman.png',cv2.IMREAD_GRAYSCALE)
logger.info("IMREAD_GRAYSCALE img_gray.shape: {}".format(img_gray.shape))
logger.info("IMREAD_GRAYSCALE img_gray.size: {}".format(img_gray.size))
logger.info("IMREAD_GRAYSCALE img_gray.dtype: {}".format(img_gray.dtype))


# 截取一块图片
snowman = img[200:600,300:600]
img[200:600,800:1100] = snowman

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()