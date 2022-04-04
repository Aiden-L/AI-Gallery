import numpy as np


def three_filer(inputR, inputG, inputB):
    """
    三色颜色过滤器
    :param inputR: 输入图片R通道
    :param inputG: 输入图片G通道
    :param inputB: 输入图片B通道
    :return: 转换完成的RGB通道
    """
    # color1,2,3: 转换的颜色，用RGB元组表示，例如 (255, 255, 255)
    color1, color2, color3 = (49, 50, 49), (158, 125, 90), (214, 224, 226)
    # border1: 转换颜色的边界1，如需要颜色1占比75/255，则border1为75
    # border2: 转换颜色的边界1，如需要颜色2占比75/255，则border1为75+border1=150
    border1, border2 = 75, 150
    # 颜色过滤
    inputR = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border1, color1[0], inputR)
    inputG = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border1, color1[1], inputG)
    inputB = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border1, color1[2], inputB)
    inputR = np.where((0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border1) & (
            0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border2), color2[0], inputR)
    inputG = np.where((0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border1) & (
            0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border2), color2[1], inputG)
    inputB = np.where((0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border1) & (
            0.299 * inputR + 0.587 * inputG + 0.114 * inputB < border2), color2[2], inputB)
    inputR = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border2, color3[0], inputR)
    inputG = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border2, color3[1], inputG)
    inputB = np.where(0.299 * inputR + 0.587 * inputG + 0.114 * inputB >= border2, color3[2], inputB)
    return inputR, inputG, inputB
