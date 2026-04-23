# 图像识别项目：利用机器学习方法研究气泡筏中的动力学行为（院优秀毕业论文）

## 项目简介
基于卷积神经网络的图像分类系统，实现对气泡筏中气泡的识别，并生成简单的数字孪生图像。

## 技术栈
- Python 3.8
- YOLOv8
- PyTorch
- OpenCV

细节：
| 类别 | 具体库/工具 |
|------|-------------|
| 编程语言 | Python 3.8 |
| 深度学习框架 | YOLOv8 (Ultralytics) + PyTorch (底层) |
| 图像处理 | OpenCV (cv2), PIL (Pillow) |
| 数值计算 | NumPy |
| 数据可视化 | Matplotlib |
| 文件与路径处理 | glob, os |

## 核心功能
- 使用 YOLOv8 加载预训练模型，对图像/视频进行目标检测
- 利用 OpenCV 和 PIL 对检测结果进行可视化（画框、添加标签、支持中文显示）
- 批量处理文件夹内的图片（glob/os）
- 使用 Matplotlib 展示对比图

## 效果展示

<img width="871" height="653" alt="装置示意图" src="https://github.com/user-attachments/assets/de1da539-bf9c-4c3f-b523-90d485ac7115" />

[new3.bmp](https://github.com/user-attachments/files/26993438/new3.bmp)
[1.bmp](https://github.com/user-attachments/files/26993457/1.bmp)
[3.bmp](https://github.com/user-attachments/files/26993449/3.bmp)

<img width="1374" height="820" alt="位置信息" src="https://github.com/user-attachments/assets/e04544a3-350d-46f9-ab10-8844f44d217a" />

<img width="1077" height="1080" alt="F1" src="https://github.com/user-attachments/assets/77d74f23-9cca-4bd8-8471-006c35e4d639" />

<img width="1031" height="1080" alt="PR" src="https://github.com/user-attachments/assets/668f8db8-a735-44b2-b4a6-91b582216436" />

<img width="2250" height="1500" alt="P-Curve" src="https://github.com/user-attachments/assets/c99807ca-102d-4b8c-be43-0b7d392c0805" />

<img width="3000" height="2250" alt="confusionmatrix" src="https://github.com/user-attachments/assets/8f19afdb-bdea-423c-b0c0-f866fdafcf9d" />

## 气泡迁移（数字孪生演示）
STEP1
<img width="640" height="480" alt="1-1" src="https://github.com/user-attachments/assets/7385d1b8-9397-486d-b2d3-48bca181da60" />
STEP2
<img width="640" height="480" alt="1-2" src="https://github.com/user-attachments/assets/77f1f68a-9a5f-44b7-8ffb-61cfc91a0f67" />
STEP3
<img width="640" height="480" alt="1-3" src="https://github.com/user-attachments/assets/d2a69874-cc47-4016-9dee-bfb093af877a" />


## 如何运行
### 训练
1. 准备数据集（YOLO格式的标注文件）
2. 修改 `config.yaml` 中的数据集路径和类别
3. 运行训练脚本：
   ```bash
   python train.py --data config.yaml --epochs 200 --batch-size 16


## 环境要求（基于原始开发环境）
- Python 3.8
- PyTorch 1.10+
- Ultralytics YOLOv8
- 其他依赖见 requirements.txt

*注：项目开发于2024年，新环境可能需要调整依赖版本。*





