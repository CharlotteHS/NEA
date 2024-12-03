from ultralytics import YOLO
import cv2
import numpy as np


model = YOLO('yolov8n.pt')
#loading the yolo nano pretrained model
model.export(format='onnx')
#exporting to ONNX and creating a file

model_path = 'yolov8n.onnx'

cap = cv2.VideoCapture(0)

