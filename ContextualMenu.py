from tkinter import *
import tkinter as tk
import pyperclip

class ContextualMenu:
    def __init__(self, root):
        self.root = root
        self.captureEntry = StringVar()

        self.contextMenu = Menu(self.root, tearoff=0)
        self.contextMenu.add_command(label="Copy", command=self._copy)
        self.contextMenu.add_command(label="Paste", command=self._paste)

    def doPopup(self, event):
        try:
            self.contextMenu.tk_popup(event.x_root, event.y_root)
        finally:
            self.contextMenu.grab_release()

    def _copy(self):
        try:
            pyperclip.copy(self.captureEntry.get())
        except AttributeError:
            pass

    def setEntry(self, entryFild):
        self.entryFild = entryFild

    def _paste(self):
        self.entryFild.insert(tk.END, pyperclip.paste())