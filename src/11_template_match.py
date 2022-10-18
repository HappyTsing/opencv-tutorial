import cv2
import numpy as np
from loguru import logger
"""
@Description 图像匹配
"""

# 对于探测的图，保留原本的RGB版本，并创建一个灰度版本
img_rgb = cv2.imread('img/opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# 探测模板加载灰度版本
template = cv2.imread('img/opencv-template-for-matching.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.matchTemplate 参数: (检测图, 模板图, 匹配方法)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.8
# threshold = 0.7 # 0.8只能匹配一些，0.7可以匹配更多
loc = np.where( res >= threshold)

# 使用灰度图像中找到的坐标，标记原始图像上的所有匹配：
w, h = template.shape[::-1]
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()