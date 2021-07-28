#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 14:25
# @Author  : raychiu
# @File    : videoCaptureTest2.py

# 使用摄像头进行动态捕捉

# 1.导入库
import cv2

# 2.打开摄像头
capture = cv2.VideoCapture(0)

#设置固定帧率
timeF = 25
i = 0

# 3.获取摄像头的实时画面
while True:
    #3.1读取每一帧的画面 image <class 'numpy.ndarray'> (480, 640, 3)
    ret, image = capture.read()

    #3.2灰度处理
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    if (i % timeF == 0):
        print(i)
    i = i + 1
    #3.3显示图片
    cv2.imshow('video',image)

    #3.4暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 4.释放资源
capture.release()

# 5.销毁窗口
cv2.destroyAllWindows()