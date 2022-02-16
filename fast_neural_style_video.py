import cv2
from utils.fast_neural_style_implementor import StyleImplementor

# 读取视频
cap = cv2.VideoCapture(0)

implementor = StyleImplementor("models/instance_norm/udnie.t7", 400, 300)

while cv2.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv2.waitKey()
        break
    # implementor.show_video()
    # 灰度图像展示
    implementor.show_gray_video(frame)
