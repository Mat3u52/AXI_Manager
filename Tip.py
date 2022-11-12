import tkinter as tk
from tkinter import Label, W, PhotoImage
import time
from PIL import Image

class Tip:
    def __init__(self, root, mainFrameView, primePng = 'img/tip/okBegin.png'):
        self.root = root
        self.mainFrameView = mainFrameView
        self.startXPosition = 120
        self.startYPosition = 20
        self.minMovement = -1
        self.refreshSec = 0.01
        self.primePng = primePng

    def animateTip(self):

        self.canvasFrame1 = Label(self.mainFrameView)
        self.canvasFrame1.configure(bg="#333333", bd=0)
        self.canvasFrame1.grid(row=0, column=7, sticky=W)
        self.canvas1 = tk.Canvas(self.canvasFrame1, width=120, height=30)
        self.canvas1.configure(bg="#333333", bd=0, highlightthickness=0, highlightbackground="black")
        self.canvas1.pack(expand=False)

        self.im = Image.open(self.primePng)
        self.im.putalpha(120)
        self.im.save('img/tip/ok.png')
        self.photo = PhotoImage(file='img/tip/ok.png')
        self.imageB = self.canvas1.create_image(120, 15, image=self.photo)



        while True:
            self.canvas1.move(self.imageB, self.minMovement, 0)
            self.root.update()
            time.sleep(self.refreshSec)
            self.imgPos = self.canvas1.coords(self.imageB)

            self.al, self.bl = self.imgPos

            self.transparency = 120 + (2*(int(self.al) - 120))
            self.im = Image.open('img/tip/ok.png')
            self.im.putalpha(self.transparency)
            self.im.save('img/tip/ok.png')
            self.photo = PhotoImage(file='img/tip/ok.png')
            self.imageB = self.canvas1.create_image(self.al, self.bl, image=self.photo)

            if self.al < abs(self.minMovement):
                self.minMovement = -self.minMovement
            if self.al == int(self.startXPosition) / 2:
                break

    def __del__(self):
        pass
        #return print(f"class tip - delete")