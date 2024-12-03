from ultralytics import YOLO
import cv2
import numpy as np


model = YOLO('yolov8n.pt')
#loading the yolo nano pretrained model
model.export(format='onnx')
#exporting to ONNX and creating a file

model_path = 'yolov8n.onnx'
net = cv2.dnn.readNetFromONNX(model_path)



cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error")
    exit()

while True:
    ret, screen = cap.read()

    cv2.imshow("Screen", screen)
    cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #
        #shuts the window down when you press q
        break

cap.release()
cv2.destroyAllWindows()