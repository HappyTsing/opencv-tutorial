import cv2
"""
@Description 视频和摄像头的基本操作

除了起始行，处理视频的帧和处理图像是相同的。
"""

def show_cap():
    # 从计算机上的第一个网络摄像头返回视频
    cap = cv2.VideoCapture(0)

    while(True):
        # ret 是一个代表是否有返回的布尔值
        # frame 是每个返回的帧。 如果没有帧，不会得到错误，只会得到 None。
        ret, frame = cap.read()
        
        # 在这里，我们定义一个新的变量gray，作为转换为灰度的帧。 
        # 注意这个BGR2GRAY: OpenCV 将颜色读取为 BGR（蓝绿色红色），但大多数计算机应用程序读取为 RGB（红绿蓝）。 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        
        # 按键 q 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放网络摄像头，关闭所有 imshow() 打开的窗口
    cap.release()
    cv2.destroyAllWindows()

def save_cap():
    cap = cv2.VideoCapture(0)
    
    # mp4 需要安装依赖: brew install ffmpeg
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')   # .mp4 
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # .avi
    
    fps = cap.get(cv2.CAP_PROP_FPS)  # 帧数
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 宽高
    out = cv2.VideoWriter('output.avi',fourcc, fps, (width,height))

    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 写入帧
        out.write(frame)
        
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
save_cap()