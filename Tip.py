from tkinter import *
import tkinter as tk
import time
from PIL import Image

class Tip:
    def __init__(self, capture, mainFrameView, root):
        self.capture = capture
        self.mainFrameView = mainFrameView
        self.startXPosition = 120
        self.startYPosition = 20
        self.minMovement = -1
        self.refreshSec = 0.01
        self.root = root

    #def animateTip(self, root, xinc=minMovement, yinc=minMovement):
    #def animateTip(self, root):
    def animateTip(self):



        self.canvasFrame1 = Label(self.mainFrameView)
        self.canvasFrame1.configure(bg="#333333", bd=0)
        self.canvasFrame1.grid(row=0, column=7, sticky=W)
        self.canvas1 = tk.Canvas(self.canvasFrame1, width=120, height=30)
        self.canvas1.configure(bg="#333333", bd=0, highlightthickness=0, highlightbackground="black")
        self.canvas1.pack(expand=False)

        print("f: animateTip")

        self.im = Image.open('img/tip/okBegin.png')
        self.im.putalpha(120)
        self.im.save('img/tip/ok.png')
        self.photo = PhotoImage(file='img/tip/ok.png')
        self.imageB = self.canvas1.create_image(120, 15, image=self.photo)



        while True:
            #self.canvas1.move(self.imageB, xinc, 0)
            self.canvas1.move(self.imageB, self.minMovement, 0)
            self.root.update()
            time.sleep(self.refreshSec)
            self.imgPos = self.canvas1.coords(self.imageB)

            #al = self.imgPos
            self.al, self.bl = self.imgPos

            self.transparency = 120 + (2*(int(self.al) - 120))
            print(self.transparency)
            self.im = Image.open('img/tip/ok.png')
            # im.putalpha(155)
            self.im.putalpha(self.transparency)
            self.im.save('img/tip/ok.png')
            self.photo = PhotoImage(file='img/tip/ok.png')
            #self.photo = PhotoImage(file='cat-and-fish.png')
            self.imageB = self.canvas1.create_image(self.al, self.bl, image=self.photo)

            #if self.al < abs(xinc):
            if self.al < abs(self.minMovement):
                #xinc = -xinc
                self.minMovement = -self.minMovement
            #if bl < abs(yinc):
            #    yinc = -yinc
            if self.al == int(self.startXPosition) / 2:
                break
            print(self.al)














    def __del__(self):
        return print(f"class tip - delete")