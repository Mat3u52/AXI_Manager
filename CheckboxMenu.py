from tkinter import ttk
from tkinter import *
import tkinter as tk
from ContextualMenu import ContextualMenu

class CheckboxMenu:
    def __init__(self, tab, root, frame):
        self.tab = tab
        self.root = root
        self.checkboxFrameViTroxEx = frame

    #def checkboxTitle(self, title):
    #    self.title = title
    #    self.checkboxFrameViTroxEx = ttk.LabelFrame(self.tab, text=self.title)
    #    self.checkboxFrameViTroxEx.grid(column=0, row=4, sticky='W', padx=10, pady=10)

    def checkboxMenu(self, name, number, description):
        self.name = name
        self.number = int(number)
        self.description = description

        self.varV8103553S2EX = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.checkboxFrameViTroxEx, text=self.name,
                                        variable=self.varV8103553S2EX, onvalue=1, offvalue=1-1,
                                        command=self._checkbox)
        self.checkbox1.config(font=("Arial", 10), borderwidth=1, relief="solid", bg="#333333", fg="#000000")
        self.checkbox1.grid(column=self.number-1, row=0, sticky='W', padx=10, pady=10)


    def _checkbox(self):
        if self.varV8103553S2EX.get() == 1:
            print(self.varV8103553S2EX.get())

        # ---INSERT V810-3553S2EX---
            self.insertFrameV8103553S2EX = ttk.LabelFrame(self.tab, text=self.description)

            self.LIV8103553S2EX_0 = Label(self.insertFrameV8103553S2EX, text="Program name:",
                                          width=12, borderwidth=1, relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_0.config(font=("Arial", 10))
            self.LIV8103553S2EX_0.grid(row=0, column=0, sticky=W)

            self.objCMV8103553SEX = ContextualMenu(self.root)
            self.EIV8103553S2EX_0 = Entry(self.insertFrameV8103553S2EX, relief="solid",
                                          textvariable=self.objCMV8103553SEX.captureEntry,
                                          borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
            self.EIV8103553S2EX_0.config(font=("Arial", 10))
            self.EIV8103553S2EX_0.grid(row=0, column=1, pady=1)
            self.EIV8103553S2EX_0.bind("<Button-3>", self.objCMV8103553SEX.doPopup)
            self.objCMV8103553SEX.setEntry(self.EIV8103553S2EX_0)

            self.LIV8103553S2EX_1 = Label(self.insertFrameV8103553S2EX, text="Scanning Time:", width=12, borderwidth=1,
                                        relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_1.config(font=("Arial", 10))
            self.LIV8103553S2EX_1.grid(row=0, column=2, sticky=W)
            self.EIV8103553S2EX_1 = Entry(self.insertFrameV8103553S2EX,
                                        relief="solid", borderwidth=1, bg="#212121", fg="#FFFFFF")
            self.EIV8103553S2EX_1.config(font=("Arial", 10))
            self.EIV8103553S2EX_1.grid(row=0, column=3, pady=1, sticky=W)

            self.LIV8103553S2EX_2 = Label(self.insertFrameV8103553S2EX, text="LC:", width=12, borderwidth=1,
                                            relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_2.config(font=("Arial", 10))
            self.LIV8103553S2EX_2.grid(row=1, column=0, sticky=W)
            self.VIV8103553S2EX_2 = tk.StringVar
            self.CIV8103553S2EX_2 = ttk.Combobox(self.insertFrameV8103553S2EX, width=37,
                                                textvariable=self.VIV8103553S2EX_2, state='readonly')
            self.CIV8103553S2EX_2['values'] = ("NONE", "YES", "NO", "LACK")
            self.CIV8103553S2EX_2.grid(row=1, column=1, pady=1, sticky=W)
            self.CIV8103553S2EX_2.current(0)

            self.LIV8103553S2EX_3 = Label(self.insertFrameV8103553S2EX, text="EPI:", width=12, borderwidth=1,
                                          relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_3.config(font=("Arial", 10))
            self.LIV8103553S2EX_3.grid(row=1, column=2, sticky=W)
            self.VIV8103553S2EX_3 = tk.StringVar
            self.CIV8103553S2EX_3 = ttk.Combobox(self.insertFrameV8103553S2EX, width=20,
                                                 textvariable=self.VIV8103553S2EX_3, state='readonly')
            self.CIV8103553S2EX_3['values'] = ("NONE", "YES", "NO", "LACK")
            self.CIV8103553S2EX_3.grid(row=1, column=3, pady=1, sticky=W)
            self.CIV8103553S2EX_3.current(0)

            self.LIV8103553S2EX_4 = Label(self.insertFrameV8103553S2EX, text="BAAN:", width=12, borderwidth=1,
                                          relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_4.config(font=("Arial", 10))
            self.LIV8103553S2EX_4.grid(row=2, column=0, sticky=W)
            self.VIV8103553S2EX_4 = tk.StringVar
            self.CIV8103553S2EX_4 = ttk.Combobox(self.insertFrameV8103553S2EX, width=37,
                                                 textvariable=self.VIV8103553S2EX_4, state='readonly')
            self.CIV8103553S2EX_4['values'] = ("NONE", "YES", "NO", "LACK")
            self.CIV8103553S2EX_4.grid(row=2, column=1, pady=1, sticky=W)
            self.CIV8103553S2EX_4.current(0)

            self.LIV8103553S2EX_5 = Label(self.insertFrameV8103553S2EX, text="Comments:", width=12, borderwidth=1,
                                          relief="solid", bg="#212121", fg="#555555", pady="1")
            self.LIV8103553S2EX_5.config(font=("Arial", 10))
            self.LIV8103553S2EX_5.grid(row=2, column=2, sticky=W)

            self.objCMV8103553SEX_Comments = ContextualMenu(self.root)
            self.EIV8103553S2EX_5 = Entry(self.insertFrameV8103553S2EX,
                                          textvariable=self.objCMV8103553SEX_Comments.captureEntry,
                                            relief="solid", borderwidth=1, bg="#212121", fg="#FFFFFF")
            self.EIV8103553S2EX_5.config(font=("Arial", 10))
            self.EIV8103553S2EX_5.grid(row=2, column=3, pady=1)
            self.EIV8103553S2EX_5.bind("<Button-3>", self.objCMV8103553SEX_Comments.doPopup)
            self.objCMV8103553SEX_Comments.setEntry(self.EIV8103553S2EX_5)

            self.insertFrameV8103553S2EX.grid(column=0, row=4+self.number, columnspan=10, sticky='W', padx=10, pady=10)

        elif self.varV8103553S2EX.get() == 0:
            print(self.varV8103553S2EX.get())
            self.insertFrameV8103553S2EX.grid_forget()
