from tkinter import ttk
from tkinter import *
import pyperclip

class ContextualMenu:
    def __init__(self, root):
        self.root = root
        self.captureEntry = StringVar()

        self.contextMenu = Menu(self.root, tearoff=0)
        self.contextMenu.add_command(label="Copy", command=self.copy)
        #self.contextInsertMenu.add_command(label="Copy", command=pyperclip.copy(self.test))
        #self.contextInsertMenu.add_command(label="Paste", command=contextPasteEI2)



    def doPopup(self, event):
        try:
            self.contextMenu.tk_popup(event.x_root, event.y_root)
            #print(self.text)
        finally:
            self.contextMenu.grab_release()

    def copy(self):
        pyperclip.copy(self.captureEntry.get())
        #print(self.text.get())


    #def contextPasteEI2(self):
    #    EI2.insert(tk.END, pyperclip.paste())