from time import time
import cv2
import numpy as np

'''
在左上方添加水印
参数: 原图对象, 水印对象, 结果图片路径/名称, 水印透明度, 水印相对原图的x坐标, 水印相对原图的y坐标, 是否改为右下添加, 水印相对原图的缩放比例
注意: 缩放比例最大是1，大于1会自动转化为1，位置x,y最好设置为0,0需要边距请在水印图片中调整，这样可以自适应画面，非0,0可能会因水印超出原图边界报错
'''


def addWaterMarkAtTopLeft(ori_img, watermark, result_name, transparency, position_x, position_y, convert, scale):
    # 确保scale值正常
    if scale > 1 or scale <= 0:
        scale = 1
    # 判断原图通道，添加alpha通道
    if ori_img.shape[2] == 3:
        b_channel, g_channel, r_channel = cv2.split(ori_img)
        a_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
        ori_img = cv2.merge((b_channel, g_channel, r_channel, a_channel))
    # 根据比例缩放图片
    watermark_h, watermark_w = watermark.shape[:2]  # 获取水印的高度、宽度
    ori_img_h, ori_img_w = ori_img.shape[:2]  # 获取原图的高度、宽度
    mark_scale = min((ori_img_h - position_y) / watermark_h, (ori_img_w - position_x) / watermark_w) * scale
    # print(mark_scale, (int(watermark_w*mark_scale), int(watermark_h*mark_scale)))
    watermark = cv2.resize(watermark, (int(watermark_w * mark_scale), int(watermark_h * mark_scale)))
    watermark_h, watermark_w = watermark.shape[:2]  # 重新获取水印的高度、宽度

    # 判断是否为右下
    if convert:
        position_x, position_y = ori_img_w - watermark_w - position_x, ori_img_h - watermark_h - position_y

    ori_img_part = ori_img[position_y:watermark_h + position_y, position_x:watermark_w + position_x]  # 截取原图中需要替换位置

    # dst = cv2.addWeighted(watermark, transparency, roi, 1-transparency, 0)  # 图像融合
    # 抽取截取部分的BGRA
    part_b_channel, part_g_channel, part_r_channel, part_a_channel = cv2.split(ori_img_part)
    # 抽取水印部分的BGRA
    mark_b_channel, mark_g_channel, mark_r_channel, mark_a_channel = cv2.split(watermark)
    # 运算融合
    part_b_channel = np.where(mark_a_channel == 0, part_b_channel,
                              transparency * mark_b_channel + (1 - transparency) * part_b_channel)
    part_g_channel = np.where(mark_a_channel == 0, part_g_channel,
                              transparency * mark_g_channel + (1 - transparency) * part_g_channel)
    part_r_channel = np.where(mark_a_channel == 0, part_r_channel,
                              transparency * mark_r_channel + (1 - transparency) * part_r_channel)

    # 运算融合算法2, 类型不同无法生效，舍弃
    # part_b_channel += (mark_a_channel != 0) * (transparency * mark_b_channel - transparency * part_b_channel)
    # part_g_channel += (mark_a_channel != 0) * (transparency * mark_g_channel - transparency * part_g_channel)
    # part_r_channel += (mark_a_channel != 0) * (transparency * mark_r_channel - transparency * part_r_channel)

    marked_part = cv2.merge((part_b_channel.astype(part_a_channel.dtype), part_g_channel.astype(part_a_channel.dtype),
                             part_r_channel.astype(part_a_channel.dtype), part_a_channel))

    result_img = ori_img.copy()
    result_img[position_y:watermark_h + position_y, position_x:watermark_w + position_x] = marked_part  # 将融合后的区域放进原图

    cv2.imwrite(result_name, result_img)


if __name__ == '__main__':
    begin = time()
    ori_img = cv2.imread('image10.jpg', cv2.IMREAD_UNCHANGED)  # 原图
    watermark = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)  # 水印
    addWaterMarkAtTopLeft(ori_img, watermark, "result.png", 0.8, 0, 0, True, 0.2)
    end = time()
    print("水印添加完成, 计算用时:", end - begin, "秒")
