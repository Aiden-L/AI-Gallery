import time
import cv2
from utils.fast_neural_style_implementor import StyleImplementor

# 读取视频
cap = cv2.VideoCapture(0)
# 载入模型
implementor = StyleImplementor("models/instance_norm/udnie.t7", 400, 300)
#视频流变换
while True:
    # 接受键盘输入
    k = cv2.waitKey(1)
    # 检测到esc键退出
    if k == 27:
        break
    # 图像读取处理
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv2.waitKey()
        break
    # implementor.show_video()
    # 灰度图像展示
    out = implementor.show_video(frame)
    # 检测s键保存图片，图像路径为当前时间，保存在capture文件夹下
    if k == ord('s'):
        filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".jpg"
        print(filename + " 已保存")
        cv2.imwrite('./capture/' + filename, out * 255)
cap.release()
cv2.destroyAllWindows()