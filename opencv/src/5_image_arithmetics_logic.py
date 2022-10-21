import cv2
import numpy as np
from loguru import logger
"""
@Description 图像算术和逻辑运算

本代码共实现两件事：
1. force_add()  opencv_add()  opencv_addWeighted() 三个函数，测试三种方法实现图片重叠
2. add_logo() 添加一个python logo 到给定图片的右上方。但是如果是 4_image_operation 中的粗暴添加
              即直接将给定图片的像素颜色值修改为logo的像素值即可，但由于完全替换，此时logo中自带的白色背景也会被替换。
              因此需要用到阈值，此处只是用于展示，阈值的详细内容将在下一章讲解。
"""

# 500 x 250
img1 = cv2.imread('img/3D-Matplotlib.png')
img2 = cv2.imread('img/mainsvmimage.png')
img3 = cv2.imread('img/mainlogo.png')


logger.info(img1[125,250])
logger.info(img2[125,250])


def force_add():
    #越界时: img1 + img2 - 255
    add = img1+img2
    logger.info(add[125,250])

    cv2.imshow('add',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def opencv_add():
    #越界时: 直接取 255
    add = cv2.add(img1,img2)
    logger.info(add[125,250])
    
    
    cv2.imshow('add',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def opencv_addWeighted():
    # cv2.addWeighted() 参数: (图像1, 权重1, 图像2, 权重2, 伽马值)
    # 伽马值是光的测量值，此处将其保留为零
    weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
    logger.info(weighted[125,250])
    
    cv2.imshow('add',weighted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def add_logo():
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img3.shape
    roi = img1[0:rows, 0:cols ]

    # Now create a mask of logo and create its inverse mask
    img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

    # add a threshold
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    img3_fg = cv2.bitwise_and(img3,img3,mask = mask)

    dst = cv2.add(img1_bg,img3_fg)
    img1[0:rows, 0:cols ] = dst

    cv2.imshow('res',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# force_add()
# opencv_add()
# opencv_addWeighted()
add_logo()
