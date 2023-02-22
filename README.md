# AI-Gallery

#### 介绍
> 项目通过图像风格化处理实现艺术效果
> 
> 其中fast-neural-style引用fast-neural-style项目训练模型
> 
> (模型来自: <https://github.com/jcjohnson/fast-neural-style>)
> 
> 项目中包含了一些图片处理常用的方法

#### 软件架构
* Python 3.9
* OpenCV

#### 安装教程
1. 运行 `models/download_style_transfer_models.sh`下载模型 (模型来自: <https://github.com/jcjohnson/fast-neural-style>)
2. `pip install -r requirements.txt`

#### 使用说明
1. 像素块随机风格demo：`python pixel_block_style_img.py`
2. 图片版本demo：`python fast_neural_style_img.py`
3. 视频实时版本demo：`python fast_neural_style_video.py`

#### 通用函数
1. 添加水印，测试demo：调用`singleton_test.py`单例测试demo中的`test_water_mark()`函数

#### 更新日志
* 1.0.0: 像素运算生成风格化图像
* 1.1.0: 新增fast-neural-style模型支持，新增生成风格图像demo
* 1.1.1: 新增摄像头实时生成风格demo
* 1.1.2: 新增摄像头实时预览时捕捉快照功能
* 1.1.3: 对视频和图片支持灰度显示，生成灰度风格图
* 1.2.0: 新增带有颜色过滤器的风格图
* 1.2.1: 优化算法，新增颜色过滤器实时视频预览
* 1.3.0: 新增图片工具模块
* 1.3.1: 新增图片添加水印工具，水印透明度调整
* 1.3.2: 添加水印工具支持png水印，透明背景
* 1.3.3: 添加水印工具支持自适应位置调整，支持右下开始的布局
