from tkinter import ttk
from tkinter import *
from ContextualMenu import ContextualMenu
from DBConnect import DBConnect
from Tip import Tip

class NewItem:
    def __init__(self, tab, root):
        self.tab = tab
        self.root = root
        self.objDB = DBConnect()

    #def _insertData(self, newItem, amountOfTheBoards):
    #    self.newItem = newItem
    #    self.amountOfTheBoards = amountOfTheBoards
                     #EIV8103553S2EX_0.get(), EIV8103553S2EX_1.get(), CIV8103553S2EX_2.get(),
                     #CIV8103553S2EX_3.get(), CIV8103553S2EX_4.get(), EIV8103553S2EX_5.get(),

                     #EIV8103483S2EX_0.get(), EIV8103483S2EX_1.get(), CIV8103483S2EX_2.get(),
                     #CIV8103483S2EX_3.get(), CIV8103483S2EX_4.get(), EIV8103483S2EX_5.get(),

                     #EIV8103163_0.get(), EIV8103163_1.get(), CIV8103163_2.get(),
                     #CIV8103163_3.get(), CIV8103163_4.get(), EIV8103163_5.get()):

    #    self.objDB.insert(self.newItem, self.amountOfTheBoards)
        #             EIV8103553S2EX_0.get(), EIV8103553S2EX_1.get(), CIV8103553S2EX_2.get(),
        #             CIV8103553S2EX_3.get(), CIV8103553S2EX_4.get(), EIV8103553S2EX_5.get(),

        #             EIV8103483S2EX_0.get(), EIV8103483S2EX_1.get(), CIV8103483S2EX_2.get(),
        #             CIV8103483S2EX_3.get(), CIV8103483S2EX_4.get(), EIV8103483S2EX_5.get(),

         #            EIV8103163_0.get(), EIV8103163_1.get(), CIV8103163_2.get(),
         #            CIV8103163_3.get(), CIV8103163_4.get(), EIV8103163_5.get()
         #            )
    #    self.objDB.closeDB()

        #objTipNew = Tip(root, mainFrameInsert)
        #objTipNew.animateTip()

    def mainFrameInsert(self):
        self.mainFrameInsert = ttk.LabelFrame(self.tab, text=" Insert Main ")
        self.mainFrameInsert.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)
        self.LI2 = Label(self.mainFrameInsert, text="Item:", width=12, borderwidth=1,
                         relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI2.config(font=("Arial", 10))
        self.LI3 = Label(self.mainFrameInsert, text="Qty:", width=12, borderwidth=1,
                         relief="solid", bg="#212121", fg="#555555", pady="1")
        self.LI3.config(font=("Arial", 10))
        self.LI2.grid(row=0, column=0, sticky=W)
        self.LI3.grid(row=0, column=2, sticky=W)
        self.objCM = ContextualMenu(self.root)
        self.EI2 = Entry(self.mainFrameInsert, relief="solid", textvariable=self.objCM.captureEntry,
                         borderwidth=1, width=35, bg="#212121", fg="#FFFFFF")
        self.EI2.config(font=("Arial", 10))
        self.EI2.grid(row=0, column=1, pady=1)
        self.EI2.bind("<Button-3>", self.objCM.doPopup)
        self.objCM.setEntry(self.EI2)

        self.EI3 = Entry(self.mainFrameInsert, relief="solid", borderwidth=1, width=10, bg="#212121", fg="#FFFFFF")
        self.EI3.config(font=("Arial", 10))
        self.EI3.grid(row=0, column=3, pady=1, stick=W)

        #self.BI1 = ttk.Button(self.mainFrameInsert, text="Insert", width=55, command=self.objDB.insert(
        #                        self.EI2.get(), self.EI3.get()), cursor="hand2")
        #self.BI1.grid(row=1, column=0, columnspan=4, pady=2)