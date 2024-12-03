from ultralytics import YOLO
import cv2
import numpy as np


model = YOLO('runs/detect/train3/weights/best.pt')
#loading the pretrained model which holds the best ver. of our data

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error")
    exit()

while True:
    ret, screen = cap.read()

    cv2.imshow("Screen", screen)
    cv2.waitKey(1)

    show = model(screen)
    #initiates object detection

    annotations = show[0].plot()
    cv2.imshow("BSL Detector", annotations)
    #shows detection on the screen
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #
        #shuts the window down when you press q
        break

cap.release()
cv2.destroyAllWindows()
#shuts the webcam screen down