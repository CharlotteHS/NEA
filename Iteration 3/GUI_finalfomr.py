import customtkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import customtkinter as ctk
from tkinter import messagebox
#in normal tkinter::: root = tkinter.Tk()
#in custom::: root = customtkinter.CTk 
import time
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
#this sets the background to dark, light, or system
ctk.set_default_color_theme("dark-blue")
#the theme can be dark blue, blue, or green

screen = ctk.CTk()
screen.title("Login and Registration")
screen.geometry("500x350")
#creating the screen size and title
master = screen

    
frame = customtkinter.CTkFrame(master=screen)
frame.pack(pady=20, padx=60, fill ="both", expand=True)
#creates a frame which buttons can be placed and moved inside

label = ctk.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)
#title

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
#puts 'username' in the box when there's no other text there
entry1.pack(pady=12, padx=10)
#boarder
entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
#show = "*" encodes the password so no one can see it
entry2.pack(pady=12, padx=10)

#creating a second page
def NewWindow():
    new_window = ctk.CTkToplevel(screen)
    new_window.title("Homescreen")
    new_window.geometry("500x350")
    #new_window.grab_set()
    #this means we cant use the login screen (focus is on the new screen)

    frame = ctk.CTkFrame(master=new_window)
    frame.pack(pady=5, padx=5, fill ="both", expand=True)
    #frame.grid()

    more = Menu(new_window)
    new_window.config(menu=more)
    more_opt = Menu(more, tearoff=0)
    #setting bar at the top of the screen

    #The options:
    def exit():
        new_window.destroy()

    def help():
        messagebox.showinfo("Working on it...")

    def settings():
        messagebox.showinfo("Working on it...")


    more.add_cascade(label="More", menu=more_opt)
    more_opt.add_command(label="Settings", command=settings)
    more_opt.add_command(label="Help", command=help)
    more_opt.add_separator()
    #adds a line dividing the above instructions and the ones below
    more_opt.add_command(label="Log Out", command=exit)


    #Different pages & their Buttons:
    gap = ctk.CTkLabel(master=frame, text="")
    gap.pack(pady=32, padx=10)
    #so that the buttons are in the middle

    ########################################################################
    
    #learning page leading in from the login page
    def learn_pg():
        #def learn_pg(sep):
        #super().__init__()

        #creating title and sizing
        learn = ctk.CTkToplevel(new_window)
        learn.title("Start Learning Soon :)")
        learn.geometry("500x350")


        #help and settings stuff
        more = Menu(learn)
        learn.config(menu=more)
        more_opt = Menu(more, tearoff=0)
        #setting bar at the top of the screen
        #The options:
        def exit():
            learn.destroy()

        def help():
            messagebox.showinfo("Working on it...")

        def settings():
            messagebox.showinfo("Working on it...")
        more.add_cascade(label="More", menu=more_opt)
        more_opt.add_command(label="Settings", command=settings)
        more_opt.add_command(label="Help", command=help)
        more_opt.add_separator()
        more_opt.add_command(label="Log Out", command=exit)


        #sep.sidebar_frame = ctk.CTkFrame(sep, width=140, corner_radius=0)
        #sep.sidebar_frame

        #creating the rest of the alphabet buttons
        def display_message():
            messagebox.showinfo("Denied","Coming Soon")
            #title = 'denied', message = 'Coming soon'
            #if the button is pressed this procedure will run

        c2 = ctk.CTkButton(learn,text="f-j",command=display_message)
        c2.place(x=189, y=110)
        #placement of the button using coordinates
        c2 = ctk.CTkButton(learn,text="k-o",command=display_message)
        c2.place(x=189, y=140)
        c2 = ctk.CTkButton(learn,text="p-t",command=display_message)
        c2.place(x=189, y=170)
        c2 = ctk.CTkButton(learn,text="u-z",command=display_message)
        c2.place(x=189, y=200)

        #Object Detection Here ↓
        def a_e():
            print("Loading")

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

        c1 = ctk.CTkButton(learn,text="a-e",command=a_e)
        c1.place(x=189, y=80)

    learning = ctk.CTkButton(master=frame, text="Learning", command=learn_pg)
    learning.pack(pady=12, padx=8)
    ########################################################################

    def progress_pg():
        progress = ctk.CTkToplevel(new_window)
        progress.title("Progress Page")
        progress.geometry("500x350")
    progress = ctk.CTkButton(master=frame, text="View Progress", command=progress_pg)
    progress.pack(pady=12, padx=2)
    #### NEED TO MAKE A COMING SOON POP UP EITHER ON THE PAGE OR BEFORE ###

    #time.sleep(2)
    #frame.destroy(screen)

    new_window.mainloop()


    
    

def exit():
    screen.destroy()
    #exits the home screen


loginB = ctk.CTkButton(master=frame, text="Login", command=NewWindow)
#command=lambda:[(NewWindow),(exit)])
loginB.pack(pady=12, padx=10)
#The button which will move you onto the next page

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)
#to ensure login details are remebered, e.g. on personal devices 

#def shutDown():
    

screen.mainloop()