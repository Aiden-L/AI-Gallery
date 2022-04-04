import cv2
from utils.fast_neural_style_implementor import StyleImplementor

# 读取图片
image = cv2.imread('img/image10.jpg')
# 图像尺寸
(height, width) = image.shape[:2]
# 生成风格化图像
implementor = StyleImplementor("models/instance_norm/udnie.t7", width, height)

# 原风格图像
# implementor.show_img(image)
# 灰度风格图像
# implementor.show_gray_img(image)
# 三色风格图像
implementor.show_three_color_img(image)
