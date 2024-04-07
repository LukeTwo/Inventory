import customtkinter as c
import tkinter as t
from tkinter import ttk

class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        self.title("Book Inventory")
        self.iconbitmap("book.ico")
        self.grid_columnconfigure((0,4), weight=1)
        self.frame = ttk.Frame(self, relief="ridge", width=200, height=100)
        self.frame.grid(row=0, column=0,sticky='e')
        self.frame2 = ttk.Frame(self, relief="ridge")
        self.frame2.grid(row=0, column=1,sticky='w,e')
        self.frame3 = ttk.Frame(self, borderwidth=5, relief="ridge",  width=200, height=100)
        self.frame3.grid(row=0, column=2,sticky='w,e')
        self.frame4 = ttk.Frame(self, borderwidth=5, relief="ridge", width=200, height=100)
        self.frame4.grid(row=0, column=3,sticky='w,e')
        self.frame5 = ttk.Frame(self, borderwidth=5, relief= "ridge",width=200, height=100)
        self.frame5.grid(row=0, column=4,sticky='w')
        # add widgets to app
        
        self.button = c.CTkButton(self, command=self.button_click, text="Button")
        self.button.grid(row=2,columnspan=5)
        
        self.bookLabel = c.CTkLabel(self, text="Enter name of Book")
        self.bookLabel.grid(row=1, column=0)
        self.bookValue = c.CTkEntry(self)
        self.bookValue.grid(row=1, column=1)

    # add methods to app
    def button_click(self):
        print("button click")

app = App()
app.mainloop()