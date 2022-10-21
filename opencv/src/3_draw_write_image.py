import numpy as np
import cv2

"""
@Description 使用 opencv 绘制图片和写字

在 1_load_image 中，已经使用在图片中绘制，但 Matplotlib 并不真正用于此目的，特别是不能用于视频源。
幸运的是，opencv提供了很棒的工具帮助实施绘制和标记。
"""
img = cv2.imread('img/snowman.png',cv2.IMREAD_COLOR)

# cv2.line()参数：(图像/帧，开始坐标，结束坐标，颜色_bgr，线条粗细)。
cv2.line(img,(0,0),(750,750),(255,255,255),15)

# cv2.rectangle() 参数: (图像/帧，左上角坐标，右下角坐标，颜色，线条粗细)
cv2.rectangle(img,(15,25),(700,550),(0,0,255),15)

# cv2.circle() 参数: (图像/帧，圆心，半径，颜色，线条粗细)。 
# 当粗细为 -1 时，意味着将填充对象，所以我们会得到一个实心圆。
cv2.circle(img,(400,400), 200, (0,255,0), -1)


# 绘制多边形
# 坐标数组 pts（点的简称），此时会绘制一个四边形。
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)

# OpenCV documentation had this code, which reshapes the array to a 1 x 2. 
# I did not find this necessary, but you may:
# pts = pts.reshape((-1,1,2))

# cv2.polylines() 参数: (图像/帧，坐标数组, 是否连接重点和起始点，颜色，线条粗细)
cv2.polylines(img, [pts], True, (0,255,255), 3)

# 图像上写字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()