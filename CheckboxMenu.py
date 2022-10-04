from tkinter import ttk
from tkinter import *
import tkinter as tk
from ContextualMenu import ContextualMenu
from DBConnect import DBConnect

class CheckboxMenu:
    def __init__(self, tab, root, frame, description):
        self.tab = tab
        self.root = root
        self.checkboxFrame = frame
        self.description = description

        self.insertFrame = ttk.LabelFrame(self.checkboxFrame, text=self.description)
        self.LI_0 = Label(self.insertFrame, text="Program name:",
                          width=12, borderwidth=1, relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_0.config(font=("Arial", 10))
        self.LI_0.grid(row=0, column=0, sticky=W)
        self.objCM = ContextualMenu(self.root)
        self.EI_0 = Entry(self.insertFrame, relief="solid",
                          textvariable=self.objCM.captureEntry,
                          borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI_0.config(font=("Arial", 10))
        self.EI_0.grid(row=0, column=1, pady=1)
        self.EI_0.bind("<Button-3>", self.objCM.doPopup)
        self.objCM.setEntry(self.EI_0)
        self.LI_1 = Label(self.insertFrame, text="Scanning Time:", width=12, borderwidth=1,
                          relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_1.config(font=("Arial", 10))
        self.LI_1.grid(row=0, column=2, sticky=W)
        self.EI_1 = Entry(self.insertFrame,
                          relief="solid", borderwidth=1, bg="#212121", fg="#FFFFFF")
        self.EI_1.config(font=("Arial", 10))
        self.EI_1.grid(row=0, column=3, pady=1, sticky=W)
        self.LI_2 = Label(self.insertFrame, text="LC:", width=12, borderwidth=1,
                          relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_2.config(font=("Arial", 10))
        self.LI_2.grid(row=1, column=0, sticky=W)
        self.VI_2 = tk.StringVar
        self.CI_2 = ttk.Combobox(self.insertFrame, width=37,
                                 textvariable=self.VI_2, state='readonly')
        self.CI_2['values'] = ("NONE", "YES", "NO", "LACK")
        self.CI_2.grid(row=1, column=1, pady=1, sticky=W)
        self.CI_2.current(0)
        self.LI_3 = Label(self.insertFrame, text="EPI:", width=12, borderwidth=1,
                          relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_3.config(font=("Arial", 10))
        self.LI_3.grid(row=1, column=2, sticky=W)
        self.VI_3 = tk.StringVar
        self.CI_3 = ttk.Combobox(self.insertFrame, width=20,
                                 textvariable=self.VI_3, state='readonly')
        self.CI_3['values'] = ("NONE", "YES", "NO", "LACK")
        self.CI_3.grid(row=1, column=3, pady=1, sticky=W)
        self.CI_3.current(0)
        self.LI_4 = Label(self.insertFrame, text="BAAN:", width=12, borderwidth=1,
                          relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_4.config(font=("Arial", 10))
        self.LI_4.grid(row=2, column=0, sticky=W)
        self.VI_4 = tk.StringVar
        self.CI_4 = ttk.Combobox(self.insertFrame, width=37,
                                 textvariable=self.VI_4, state='readonly')
        self.CI_4['values'] = ("NONE", "YES", "NO", "LACK")
        self.CI_4.grid(row=2, column=1, pady=1, sticky=W)
        self.CI_4.current(0)
        self.LI_5 = Label(self.insertFrame, text="Comments:", width=12, borderwidth=1,
                          relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_5.config(font=("Arial", 10))
        self.LI_5.grid(row=2, column=2, sticky=W)
        self.objCM_Comments = ContextualMenu(self.root)
        self.EI_5 = Entry(self.insertFrame,
                          textvariable=self.objCM_Comments.captureEntry,
                          relief="solid", borderwidth=1, bg="#212121", fg="#FFFFFF")
        self.EI_5.config(font=("Arial", 10))
        self.EI_5.grid(row=2, column=3, pady=1)
        self.EI_5.bind("<Button-3>", self.objCM_Comments.doPopup)
        self.objCM_Comments.setEntry(self.EI_5)


    def alignmentTime(self):
        self.LI_6 = Label(self.insertFrame, text="Aligment Time:",
                          width=12, borderwidth=1, relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_6.config(font=("Arial", 10))
        self.LI_6.grid(row=3, column=0, sticky=W)
        self.EI_6 = Entry(self.insertFrame, relief="solid",
                          borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI_6.config(font=("Arial", 10))
        self.EI_6.grid(row=3, column=1, pady=1)
        self.LI_7 = Label(self.insertFrame, text="Laser Points:",
                          width=12, borderwidth=1, relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_7.config(font=("Arial", 10))
        self.LI_7.grid(row=4, column=0, sticky=W)
        self.EI_7 = Entry(self.insertFrame, relief="solid",
                          borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI_7.config(font=("Arial", 10))
        self.EI_7.grid(row=4, column=1, pady=1)
        self.LI_8 = Label(self.insertFrame, text="Auto Thickness:",
                          width=12, borderwidth=1, relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI_8.config(font=("Arial", 10))
        self.LI_8.grid(row=5, column=0, sticky=W)
        self.EI_8 = Entry(self.insertFrame, relief="solid",
                          borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI_8.config(font=("Arial", 10))
        self.EI_8.grid(row=5, column=1, pady=1)

    def checkboxMenu(self, name, number):
        self.name = name
        self.number = int(number)
        self.var = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.checkboxFrame, text=self.name,
                                        variable=self.var, onvalue=1, offvalue=1-1,
                                        command=self._checkbox)
        self.checkbox1.config(font=("Arial", 10), borderwidth=1, relief="solid", bg="#333333", fg="#000000")
        self.checkbox1.grid(column=self.number-1, row=0, sticky='W', padx=10, pady=10)

    def _checkbox(self):
        if self.var.get() == 1:
            self.insertFrame.grid(column=0, row=5+self.number, columnspan=10, sticky='W', padx=10, pady=10)

        elif self.var.get() == 0:
            self.insertFrame.grid_forget()

    def cleanUp(self):
        self.EI_0.delete(0, END)
        self.EI_1.delete(0, END)
        self.CI_2.current(0)
        self.CI_3.current(0)
        self.CI_4.current(0)
        self.EI_5.delete(0, END)

    def cleanUp5DX(self):
        self.EI_6.delete(0, END)
        self.EI_7.delete(0, END)
        self.EI_8.delete(0, END)
