import cv2
import numpy as np

"""
@Description 边缘计算

基于opencv边缘检测算子有很多，比如Canny算子，Robert算子，Sobel算子，Laplacian算子，Prewitt算子，Krisch算子和Scharr滤波器等
# References: https://blog.csdn.net/weixin_42240915/category_9729864.html

本章主要是两个算子的使用：
1. 索贝尔 Sobel 算子 cv2.Sobel(src: Mat, ddepth, dx, dy, dts: Mat = ..., ksize=..., scale=..., delta=..., borderType=...)
        必要参数: 
            src: 处理图像
            ddepth: 图像深度,-1表示与原图像深度相同
            dx、dy: 求导的阶数，0表示没有求导，一般是0,1，2
        
        可选参数:
            dst: destination，生成目标。
            ksize: Soberl算子大小，必须是1、3、5、7
            scale: 缩放倒数的比例常数，默认情况下无
            delta: 一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；
            borderType: 判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。
        
2. Laplacian 算子 cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
        参数和Sobel算子类似，少了两个必要参数
"""
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])


    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
         

cv2.destroyAllWindows()
cap.release()