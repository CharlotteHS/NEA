import tkinter
import tkinter.messagebox
import customtkinter
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(screen):
        super().__init__()

        #configuring the window and frame layout
        screen.title("Main Screen")
        screen.geometry("500x350")
        frame = customtkinter.CTkFrame(master=screen)
        frame.pack(pady=0, padx=0, fill ="both", expand=True)

        #creating tabview
        screen.tabview = ctk.CTkTabview(frame, width=500, height=350)
        #size of the tabview frame
        screen.tabview.pack(pady=0, padx=0)
        screen.tabview.add("Homescreen")
        screen.tabview.add("Learning")
        screen.tabview.add("Progress")

        screen.optionmenu_1 = ctk.CTkOptionMenu(screen.tabview.tab("Homescreen"), screen.textbox = ctk.CTkTextbox(screen, width=500, height=350))


if __name__ == "__main__":
    app = App()
    app.mainloop()