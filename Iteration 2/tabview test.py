import customtkinter
from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


screen = ctk.CTk()
screen.title("Login and Registration")
screen.geometry("500x350")
master = screen
    
frame = customtkinter.CTkFrame(master=screen)
self = customtkinter.CTkTabview(master=screen)
frame.pack(pady=20, padx=60, fill ="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Tabview Test")
label.pack(pady=12, padx=10)

#creating tabview
self.tabview = ctk.CTkTabview(frame, width=450)
self.tabview = self.tabview.add("Homescreen")

self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                      values=["Value 1", "Value 2", "Value Long Long Long"])


screen.mainloop()