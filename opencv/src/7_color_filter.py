"""
@Description 创建过滤器，用于过滤特定的颜色。

"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # 获取视频帧
    _, frame = cap.read()
    
    # 将视频帧转换成HSV，即色调饱和度纯度。其和RGB一样，也有三个通道：
    #       Hue（色调、色相）
    #       Saturation（饱和度、色彩纯净度）
    #       Value（明度
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 定义过滤的颜色上下界，此处是想要显示的颜色
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    # 为特定范围创建掩码
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # 比特运算，指定范围内红色的被转换为白色，其余全部是黑色
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()