import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure()
axes = fig.add_subplot(111)

axes.axis('equal')
plt.title('Drawing Circle')

with open('posi1/bubble_raft-modified.bmp.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split(' ')
        r = float(line[-1])
        a, b = (float(line[1]), 1024. - float(line[2]))
        theta = np.arange(0, 2 * np.pi, 0.01)
        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)
        fig = plt.figure()
        axes.plot(x, y, color = 'k')
plt.show()
# ==========================================
#设置坐标轴与图形不留白
#plt.margins(x=0)
#plt.margins(y=0)
# ==========================================
#限制坐标轴范围
#plt.ylim([0,1300])
#plt.xlim([0,1300])
# ==========================================
# 圆的基本信息
# 1.圆半径
# r = 50.0
# 2.圆心坐标
# a, b = (300., 300.)
# ==========================================
# 方法一：参数方程
# theta = np.arange(0, 2 * np.pi, 0.01)
# x = a + r * np.cos(theta)
# y = b + r * np.sin(theta)
# fig = plt.figure()
# axes = fig.add_subplot(111)
# axes.plot(x, y)
# 在这之前用循环将每一个圆画一遍
# ==========================================
# 方法二：标准方程
# x = np.arange(a - r, a + r, 0.01)
# y = b + np.sqrt(r ** 2 - (x - a) ** 2)
# fig = plt.figure()
# axes = fig.add_subplot(111)
# axes.plot(x, y)  # 上半部
# axes.plot(x, -y)  # 下半部
# plt.axis('equal')
# plt.title('圆形绘制2')
# ==========================================


