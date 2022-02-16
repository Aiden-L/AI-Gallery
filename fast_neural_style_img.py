import cv2
from utils.fast_neural_style_implementor import StyleImplementor

# 读取图片
image = cv2.imread('img/example.png')
# 图像尺寸
(height, width) = image.shape[:2]
# 生成风格化图像
implementor = StyleImplementor("models/eccv16/the_wave.t7", width, height)
# implementor.show_img()
# 灰度图像展示
implementor.show_gray_img(image)
