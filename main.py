import tkinter
import customtkinter as ctk

# System Settings
ctk.set_appearance_mode("Dark")
#ctk.set_default_color_theme("green")

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Book Inventory")

# Content
intro = ctk.CTkLabel(app, text="Welcome to book inventory manager")
intro.grid(row=0, column=0, sticky="nsew")

bookLabel = ctk.CTkLabel(app, text="Enter name of Book")
bookLabel.grid(row=1, column=0)
bookValue = ctk.CTkEntry(app)
bookValue.grid(row=1, column=1)


# Keep app running
app.mainloop()