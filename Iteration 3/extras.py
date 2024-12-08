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



abcde = ctk.CTkToplevel(frame)
            abcde.title("BSL Alphabet: A to E")
            abcde.geometry("650x450")

            web_frame = ctk.CTkFrame(abcde, width=450, height=350)
            web_frame.pack(side=ctk.LEFT, padx=12, pady=10)
            #creating a frame in the window for the webcam to be placed in
            web_label = ctk.CTkLabel(web_frame)
            web_label.pack()
            #labelling the webcam feed

show = model(frame)
                #initiates object detection

                annotations = show[0].plot()
                cv2.imshow("BSL Alphabet: A to E", annotations)
                #shows detection on the screen

                annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(annotated_frame)
                imgtk = ImageTk.PhotoImage(image=img)
                #converting frame for display
                
                web_label.imgTk = imgtk
                web_label.configure(image=imgtk)
                #updating the video label

                abcde.after(10, check_frame)
                #schedule frame update


check_frame()
            abcde.mainloop()
            #starting loop