from time import time
import cv2

from tools.watermark import addWaterMarkAtTopLeft


# 添加水印工具测试
def test_water_mark():
    begin = time()
    ori_img = cv2.imread('img/image10.jpg', cv2.IMREAD_UNCHANGED)  # 原图
    watermark = cv2.imread('img/logo1.png', cv2.IMREAD_UNCHANGED)  # 水印
    addWaterMarkAtTopLeft(ori_img, watermark, "img/result.png", 0.8, 0, 0, True, 0.2)
    end = time()
    print("水印添加完成, 计算用时:", end - begin, "秒")


if __name__ == '__main__':
    test_water_mark()
