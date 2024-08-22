from ultralytics import YOLO

model = YOLO("yolov8.yaml")

results - model.train(data="coco128.yaml", epochs=3)