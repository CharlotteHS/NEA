import customtkinter
from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk
from tkinter import messagebox
import time
#in normal tkinter::: root = tkinter.Tk()
#in custom::: root = customtkinter.CTk 

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
    def learn_pg():
        learn = ctk.CTkToplevel(new_window)
        learn.title("Start Learning Soon :)")
        learn.geometry("500x350")
    learning = ctk.CTkButton(master=frame, text="Learning", command=learn_pg)
    learning.pack(pady=12, padx=8)

    def progress_pg():
        progress = ctk.CTkToplevel(new_window)
        progress.title("Progress Page")
        progress.geometry("500x350")
    progress = ctk.CTkButton(master=frame, text="View Progress", command=progress_pg)
    progress.pack(pady=12, padx=2)

    time.sleep(2)
    frame.destroy(screen)

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