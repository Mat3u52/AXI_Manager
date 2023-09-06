from tkinter import ttk
from tkinter import *
from ContextualMenu import ContextualMenu


class NewItem:
    def __init__(self, tab: ttk, root: ttk) -> None:
        """
        Template for insert a new recoed.

        :param tab: handle to frame
        type tab: ttk
        :param root: handle to main window
        :type root: ttk
        :return: template of form
        :rtype: None
        """

        self.tab: ttk = tab
        self.root: ttk = root
        self.main_frame: ttk = None

    def main_frame_insert(self, main_name: str = " ") -> None:
        main_name: str = main_name
        self.main_frame = ttk.LabelFrame(self.tab, text=main_name)
        self.main_frame.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)
        self.LI2 = Label(self.main_frame, text="Item:", width=12, borderwidth=1,
                         relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI2.config(font=("Arial", 10))
        self.LI3 = Label(self.main_frame, text="Qty:", width=12, borderwidth=1,
                         relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI3.config(font=("Arial", 10))
        self.LI2.grid(row=0, column=0, sticky=W)
        self.LI3.grid(row=0, column=2, sticky=W)
        self.objCM = ContextualMenu(self.root, '0', True, True, False)
        self.EI2 = Entry(self.main_frame, relief="solid", textvariable=self.objCM.captureEntry,
                         borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI2.config(font=("Arial", 10), highlightbackground="#000000", highlightcolor="#33FFBE")
        self.EI2.grid(row=0, column=1, pady=1)
        self.EI2.bind("<Button-3>", self.objCM.do_popup)
        self.objCM.set_entry(self.EI2)

        self.EI3 = Entry(self.main_frame, relief="solid", borderwidth=1, width=10, bg="#212121", fg="#FFFFFF")
        self.EI3.config(font=("Arial", 10), highlightbackground="#000000", highlightcolor="#33FFBE")
        self.EI3.grid(row=0, column=3, pady=1, stick=W)

    def checkboxTitle(self, title0, row):
        self.row = row
        self.title0 = title0
        self.checkboxFrame = ttk.LabelFrame(self.tab, text=self.title0)
        self.checkboxFrame.grid(column=0, row=self.row, sticky='W', padx=10, pady=10)

    def cleanUp(self):
        self.EI2.delete(0, END)
        self.EI3.delete(0, END)
