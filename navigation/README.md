[TOC]



# 机器人导航

## 建图

机器人自主导航无论是在室内或者室外，都依赖于高精度地图，所以第一步就是建图

激光雷达的性能指标：http://bbs.eetop.cn/thread-676484-1-1.html

激光SLAM与视觉SLAM的比较

![img](https://upload-images.jianshu.io/upload_images/2968079-d81d27365239c1e4?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

rplidar雷达的wiki：http://wiki.ros.org/rplidar

#### 算法

[RSLAM: A System for Large-Scale Mapping in Constant-Time Using Stereo](http://link-springer-com.vpn.whu.edu.cn:8118/article/10.1007/s11263-010-0361-7)



## 定位



## 导航

移动机器人自主规划路径，需要实现至少两个层次的模块：

一个是全局规划，就是在地图上预先规划一条线路，也要有当前机器人的位置，这是由 SLAM系统提供的，行业内一般通过先进的搜索算法来实现这个过程。

另一个是局部规划，现实场景中有很多突发情况，比如有障碍物挡道了，移动机器人需调整原先的路径。此时，它并不需要重新计算一遍全局路径，稍微绕个弯就可以。

http://bbs.eetop.cn/thread-635585-1-1.html



未知环境中的路径规划算法 D*