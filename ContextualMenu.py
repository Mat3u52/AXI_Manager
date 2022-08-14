from tkinter import ttk
from tkinter import *
import pyperclip

class ContextualMenu:
    def __init__(self, root):
        self.root = root
        self.contextInsertMenu = Menu(self.root, tearoff=0)
        #self.contextInsertMenu.add_command(label="Copy", command=contextCopyEI2)
        #self.contextInsertMenu.add_command(label="Paste", command=contextPasteEI2)

    def doPopup(event, self):
        try:
            self.contextInsertMenu.tk_popup(event.x_root, event.y_root)
        finally:
            self.contextInsertMenu.grab_release()

    def doPopupInsert(self, EI2):
        self.EI2 = EI2

    def contextCopyEI2(self, copy):
        self.copy = copy
        self.contextInsertMenu.add_command(label="Copy", command=pyperclip.copy(self.copy))
        #pyperclip.copy(EI2.get())

    #def contextPasteEI2(self):
    #    EI2.insert(tk.END, pyperclip.paste())