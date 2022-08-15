from tkinter import ttk
from tkinter import *

class NewItem:
    def __init__(self, tab):
        self.tab = tab

    def mainFrameInsert(self):
        self.mainFrameInsert = ttk.LabelFrame(self.tab, text=" Insert Main ")
        self.mainFrameInsert.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)

        self.LI2 = Label(self.mainFrameInsert, text="Item:", width=12, borderwidth=1, relief="solid",
                         bg="#212121", fg="#555555", pady="1")
        self.LI2.config(font=("Arial", 10))
        self.LI2.grid(row=0, column=0, sticky=W)

        self.LI3 = Label(self.mainFrameInsert, text="Qty:", width=12, borderwidth=1, relief="solid",
                         bg="#212121", fg="#555555", pady="1")
        self.LI3.config(font=("Arial", 10))
        self.LI3.grid(row=0, column=2, sticky=W)

        self.EI2 = Entry(self.mainFrameInsert, relief="solid", borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI2.config(font=("Arial", 10))
        self.EI2.grid(row=0, column=1, pady=1)
        self.EI2.bind("<Button-3>", doPopupInsert)

        self.EI3 = Entry(self.mainFrameInsert, relief="solid", borderwidth=1, width=10, bg="#212121", fg="#FFFFFF")
        self.EI3.config(font=("Arial", 10))
        self.EI3.grid(row=0, column=3, pady=1, stick=W)