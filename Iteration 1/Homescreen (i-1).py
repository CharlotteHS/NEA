import customtkinter
from tkinter import *
from tkinter.ttk import *
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


new_window = customtkinter.CTk()
new_window.title("Homescreen")
new_window.geometry("500x350")
#master = new_window

# TO BE INSERTED #
###############################################################
    
frame = customtkinter.CTkFrame(master=new_window)
frame.pack(pady=5, padx=5, fill ="both", expand=True)

more = Menu(new_window)
new_window.config(menu=more)
more_opt = Menu(more, tearoff=0)
#setting bar at the top of the screen

#The options:
def exit():
    new_window.destroy()

def help():
    new_window.showinfo("Working on it...")

def settings():
    new_window.showinfo("Working on it...")


more.add_cascade(label="More", menu=more_opt)
more_opt.add_command(label="Settings", command=settings)
more_opt.add_command(label="Help", command=help)
more_opt.add_separator()
#adds a line dividing the above instructions and the ones below
more_opt.add_command(label="Log Out", command=exit)

#Different pages:
def learn_page():
    learn = customtkinter.CTkToplevel(new_window)
    learn.title("Start Learning Soon :)")
    learn.geometry("500x350")

def progress():
    progress = customtkinter.CTkToplevel(new_window)
    progress.title("Progress Page")
    progress.geometry("500x350")





###############################################################
new_window.mainloop()