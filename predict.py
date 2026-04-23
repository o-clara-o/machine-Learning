from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import glob
import os

os.makedirs("result", exist_ok=True)
os.makedirs("position",exist_ok=True)
model = YOLO("new.pt")
imgs = glob.glob("./sjj/*.bmp")
for im in imgs:
    pred = model.predict(source=im)
    img = Image.open(im).convert("RGB")
    position = open(f"posi/{os.path.basename(im)}.txt","w",encoding="utf-8")
    for i in pred:
        boxex = i.boxes
        for index,box in enumerate(boxex):
            draw = ImageDraw.Draw(img)
            xywh = box.xywh.cpu().numpy()
            x, y, w, h = xywh[0]
            center_x = x
            center_y = y
            position.write(f"{index} {center_x} {center_y} {w/4+h/4}\n")
            draw.rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], outline='red')

    #cv2.imwrite("333.jpg", cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    cv2.imwrite(f"res/{os.path.basename(im)}", cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
