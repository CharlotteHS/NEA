import customtkinter
#in normal tkinter::: root = tkinter.Tk()
#in custom::: root = customtkinter.CTk 

customtkinter.set_appearance_mode("dark")
#this sets the background to dark, light, or system
customtkinter.set_default_color_theme("dark-blue")
#the theme can be dark blue, blue, or green

screen = customtkinter.CTk()
screen.geometry("500x350")

def login():
    print("Test")
    
frame = customtkinter.CTkFrame(master=screen)
frame.pack(pady=20, padx=60, fill ="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
#puts 'username' in the box when there's no other text there
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
#show = "*" encodes the password so no one can see it
entry2.pack(pady=12, padx=10)

loginB = customtkinter.CTkButton(master=frame, text="Login", command=login)
loginB.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

screen.mainloop()