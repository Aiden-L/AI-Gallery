# AI-Graphic-Arts

#### 介绍
* 项目通过图像风格化处理实现艺术效果，其中fast-neural-style引用fast-neural-style项目训练模型，模型来自: <https://github.com/jcjohnson/fast-neural-style>
* 项目中包含了一些图片处理常用的方法

#### 软件架构
* Python 3.9
* OpenCV

#### 安装教程
1. 运行 `models/download_style_transfer_models.sh`下载模型(模型来自: <https://github.com/jcjohnson/fast-neural-style>)
2. `pip install -r requirements.txt`

#### 使用说明
1. 像素块随机风格demo：`python pixel_block_style_img.py`
2. 图片版本demo：`python fast_neural_style_img.py`
3. 视频实时版本demo：`python fast_neural_style_video.py`

#### 通用函数
1. 添加水印，测试demo：调用`singleton_test.py`单例测试demo中的`test_water_mark()`函数
