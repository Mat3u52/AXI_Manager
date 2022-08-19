from tkinter import ttk
from tkinter import *
import pyperclip

class ContextualMenu:
    def __init__(self, root):
        self.root = root

        self.contextInsertMenu = Menu(self.root, tearoff=0)
        #self.contextInsertMenu.add_command(label="Copy", command=self.test)
        #self.contextInsertMenu.add_command(label="Copy", command=pyperclip.copy(self.test))
        #self.contextInsertMenu.add_command(label="Paste", command=contextPasteEI2)


    def doPopup(self, event):
        #print(event.x_root)
        #print(event.y_root)
        try:
            self.contextInsertMenu.tk_popup(event.x_root, event.y_root)
        finally:
            self.contextInsertMenu.grab_release()

    def test(self, ee):
        self.ee = ee
        print(self.ee)


    #def contextCopyEI2(self):
        #self.copy = copy
        #self.contextInsertMenu.add_command(label="Copy", command=pyperclip.copy(self.copy))
        #self.contextInsertMenu.add_command(label="Copy", command=pyperclip.copy(self.EI2))
        #pyperclip.copy(EI2.get())

    #def contextPasteEI2(self):
    #    EI2.insert(tk.END, pyperclip.paste())