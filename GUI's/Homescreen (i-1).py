import customtkinter
from tkinter import *
from tkinter.ttk import *
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


new_window = customtkinter.CTk()
new_window.title("Homescreen")
new_window.geometry("500x350")
#master = new_window

###############################################################
    
frame = customtkinter.CTkFrame(master=new_window)
frame.pack(pady=20, padx=60, fill ="both", expand=True)

new_window.mainloop()