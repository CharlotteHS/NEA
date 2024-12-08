import customtkinter
from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk
from tkinter import messagebox
import time

ctk.set_appearance_mode("dark")
#this sets the background to dark, light, or system
ctk.set_default_color_theme("dark-blue")
#the theme can be dark blue, blue, or green

screen = ctk.CTk()
screen.title("Login and Registration")
screen.geometry("500x350")
#creating the screen size and title
master = screen

def learn_pg():
        learn = ctk.CTkToplevel(screen)
        learn.title("Start Learning Soon :)")
        learn.geometry("500x350")

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

        def display_message():
            messagebox.showinfo("Denied","Coming Soon")
            #title = 'denied', message = 'Coming soon'
            #if the button is pressed this procedure will run

        c1 = Button(screen,text="f-j",command=display_message)
        c1.place(x=189, y=200)
        #placement of the button using coordinates