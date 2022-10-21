import cv2
from matplotlib import pyplot as plt

"""
@Description 图片导入

将img定义为: cv2.read(image_file, parms)。可选参数如下：

    cv2.IMREAD_COLOR：加载彩色图片，这个是默认参数，可以直接写1。
    cv2.IMREAD_GRAYSCALE：以灰度模式加载图片，可以直接写0。
    cv2.IMREAD_UNCHANGED：包括alpha通道，可以直接写-1。alpha 是不透明度
    
很多时候，你会读取颜色版本，然后将其转换为灰度。如果你没有网络摄像机，这将是你在本教程中使用的主要方法，即加载图像。

加载完成后，使用cv2.imshow(title,image)来显示图像。

cv2.waitKey(0)                 等待，直到有任何按键被按下。
cv2.destroyAllWindows()        关闭所有的串口。
cv2.imwrite(image_file, img)   保存图片
"""
def show_by_opencv():
    img = cv2.imread('img/snowman.png',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('avatar',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('img/snowman_gray.png',img)

"""
请注意，你可以绘制线条，就像任何其他 Matplotlib 图表一样，使用像素位置作为坐标的。 
不过，如果你想绘制你的图片，Matplotlib 不是必需的。 OpenCV 为此提供了很好的方法。
"""
def show_by_matplotlib():
    img = cv2.imread('img/snowman.png',cv2.IMREAD_GRAYSCALE)

    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
    plt.show()
    cv2.imwrite('img/snowman_gray.jpg',img)

show_by_opencv()