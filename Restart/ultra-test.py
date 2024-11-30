#from ultralytics import YOLO
#import YOLO

#model = YOLO('yolov8n.pt')

#model.train(data='custom_dataset.yaml', epochs=50, imgsz=640)

#yolo task=detect mode=train model=yolov8n.pt data=dataInfo.yaml epochs=100 imgsz=640 batch=16

#C:\Users\xthec>.\venv\Scripts\activate
#The system cannot find the path specified.

import os

val_path = r"C:/Users/xthec/OneDrive/Documents/GitHub/NEA/datasets/Dataset/labels (annotated)/val"
print(os.listdir(val_path))
#working

#yolo task=detect mode=train model=yolov8n.pt data=dataInfo.yaml epochs=100 imgsz=640 batch=16
#yolo task=detect mode=val model=runs/detect/train3/weights/best.pt data=dataInfo.yaml
#yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=Restart/Tensorflow/workspace/testimages

#restart epoch by inputting: yolo task=detect mode=train model=runs/detect/train/weights/last.pt data=dataInfo.yaml epochs=100
