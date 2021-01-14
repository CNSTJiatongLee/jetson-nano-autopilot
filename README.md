# Jetson-Nano-Autopilot

#### 简介
本项目是基于Jetson-Nano平台，使用NVIDIA JetRacer ROS框架进行开发的一套智能车应用。

 **v1.0版本主要实现了多车道巡航。** 

#### 演示视频
<a href="https://www.bilibili.com/video/BV1HN411d7AT" target="_blank">
<img src="https://images.gitee.com/uploads/images/2021/0115/012707_38350180_4772764.png" alt="Demo" width="320" height="180" border="10" /></a>

#### 主要功能：
1. 基于Jupyter Notebook搭建的数据样本采集标注平台。
2. 易于使用的卷积神经网络训练交互平台，通过深度学习回归任务，解决车道感知。
3. 使用tensorRT前向网络加速。
4. 交互控制台通过变道按钮进行车道变换。
5. 动态PD实现转角闭环控制。
6. 直道/弯道判断，并切换巡航速度。

#### 软件支持
- Python 3.6
- Pytorch 1.4
- CUDA 10.0
- OpenCV 3.4
- Jupyter Lab
- Ipywidgets
- JetRacer

#### 使用说明
##### 1.  数据采集
运行 ``notebook/data_collection_multi_target.ipynb`` 

采集的数据命名为 **目标标签+唯一ID**

- 修改 ``target_names`` 字段数量以更改感知车道数
- 修改 ``DATASET_DIR `` 更改数据保存地址
##### 2.  训练模型
运行 ``notebook/train_model_multi_target.ipynb`` 
- 修改 ``target_number`` 更改感知车道数
- 修改 ``epochs_widget`` 更改训练迭代数
- 修改 ``save_model_widget`` 更改模型保存地址及名称
##### 3.  构建推理加速引擎
运行 ``notebook/build_trt_model.ipynb`` 
##### 4.  车道巡航
运行 ``notebook/inference_control.ipynb`` 