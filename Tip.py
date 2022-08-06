from tkinter import *
import tkinter as tk

class tip:
    def __init__(self, capture, mainFrameView):
        self.capture = capture
        self.text = tk.StringVar()
        self.text.set(self.capture)

        self.mainFrameView = mainFrameView
        self.tipLabel = Label(self.mainFrameView, textvariable=self.text, bg="#444444", fg="#AAAAAA", relief=FLAT)
        self.tipLabel.grid(row=0, column=6, sticky=W)

    def labelTip(self):
        self.text.set("Clipboard: "+self.capture)

    def newRecordTip(self):
        self.text.set("Added new: "+self.capture)

    def destroyTip(self):
        self.tipLabel.after(250, self.tipLabel.destroy())

    def __del__(self):
        return print(f"class tip - delete")