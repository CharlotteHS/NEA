from ultralytics import YOLO

#builds a new model from scratch
model = YOLO("yolov8.yaml")

#use the model
results = model.train(data="Config.yaml", epochs=1)