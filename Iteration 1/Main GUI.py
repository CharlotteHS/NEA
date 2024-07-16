import customtkinter
from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk
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

    

def exit():
    screen.destroy()
    #exits the main screen


loginB = ctk.CTkButton(master=frame, text="Login", command=NewWindow)
#command=lambda:[(NewWindow),(exit)])
loginB.pack(pady=12, padx=10)
#The button which will move you onto the next page

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)
#to ensure login details are remebered, e.g. on personal devices 

screen.mainloop()