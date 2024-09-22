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
        screen.title("Login and Registration")
        screen.geometry("500x350")
        frame = customtkinter.CTkFrame(master=screen)
        frame.pack(pady=20, padx=60, fill ="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Tabview Test")
        label.pack(pady=12, padx=10)

        #creating tabview
        screen.tabview = ctk.CTkTabview(frame, width=450)
        screen.tabview.pack(pady=1, padx=1)
        screen.tabview.add("Homescreen")

        screen.optionmenu_1 = ctk.CTkOptionMenu(screen.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])


if __name__ == "__main__":
    app = App()
    app.mainloop()