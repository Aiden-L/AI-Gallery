import cv2

from utils.color_filter import three_filer


class StyleImplementor:

    def __init__(self, model, width, height):
        """
        :param width: 输出图像宽
        :param height: 输出图像高
        :param model: 模型地址
        :return:
        """
        try:
            self.net = cv2.dnn.readNetFromTorch(model)
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        except Exception as e:
            print(e)
            print("模型路径不正确，请检查传入的model参数！已采用默认模型")
            self.net = cv2.dnn.readNetFromTorch("models/instance_norm/udnie.t7")
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.width = width
        self.height = height
        self.window_name = "AI Gallery"

    def implementor(self, source, filter):
        # 去均值处理
        blob = cv2.dnn.blobFromImage(source, 1.0, (self.width, self.height), (103.939, 116.779, 123.680),
                                     swapRB=False, crop=False)
        # 计算/处理
        self.net.setInput(blob)
        out = self.net.forward()
        out = out.reshape(3, out.shape[2], out.shape[3])
        # 还原
        out[0] += 103.939
        out[1] += 116.779
        out[2] += 123.680
        # 过滤器
        if filter:
            out[2], out[1], out[0] = filter(out[2], out[1], out[0])
        out /= 255
        out = out.transpose(1, 2, 0)
        return out

    # :param source: 需要处理的图像/视频流
    def show_img(self, source):
        cv2.imshow(self.window_name, self.implementor(source, False))
        cv2.waitKey(0)

    def show_video(self, source):
        out = self.implementor(source, False)
        cv2.imshow(self.window_name, out)
        return out

    def show_gray_img(self, source):
        out = cv2.cvtColor(self.implementor(source, False), cv2.COLOR_BGR2GRAY)
        cv2.imshow(self.window_name, out)
        cv2.waitKey(0)

    def show_gray_video(self, source):
        out = cv2.cvtColor(self.implementor(source, False), cv2.COLOR_BGR2GRAY)
        cv2.imshow(self.window_name, out)
        return out

    def show_three_color_img(self, source):
        cv2.imshow(self.window_name, self.implementor(source, three_filer))
        cv2.waitKey(0)

    def show_three_color_video(self, source):
        out = self.implementor(source, three_filer)
        cv2.imshow(self.window_name, out)
        return out
