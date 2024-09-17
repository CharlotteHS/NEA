from tkinter import *
import customtkinter
from tkinter.ttk import *
import customtkinter as ctk
from tkinter import messagebox
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


new_window = ctk.CTk()
new_window.title("Homescreen")
new_window.geometry("500x350")
#master = new_window

# TO BE INSERTED #
###############################################################
    
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

###############################################################
new_window.mainloop()