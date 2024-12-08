web_frame = ctk.CTkFrame(abcde, width=500, height=350)
web_frame.pack(side=ctk.LEFT, padx=12, pady=10)
#creating a frame in the window for the webcam to be placed in

web_frame = ctk.Label(web_frame)
web_frame.pack()
#lavelling the webcam feed


#inputting the detection.py work here
model = YOLO('runs/detect/train3/weights/best.pt')
#loading the pretrained model which holds the best ver. of our data

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error")
    exit()

while True:
    ret, abcde = cap.read()
    if not ret:
        break

    show = model(abcde)
    #initiates object detection

    annotations = show[0].plot()
    cv2.imshow("BSL Detector", annotations)
    #shows detection on the screen
    
    if cv2.waitKey(1) & 0xFF == ord('x'): #
        #shuts the window down when you press x
        break

cap.release()
cv2.destroyAllWindows()
#shuts the webcam screen down
#end of detection.py file