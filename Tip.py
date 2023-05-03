import tkinter as tk
from tkinter import Label, W, PhotoImage
import time
from PIL import Image


class Tip:
    
    def __init__(self, root: tk, mainFrameView: tk, primePng: str = 'img/tip/okBegin.png') -> None:
        """
        Preparation of canvas area.

        :return: prepare canvas area
        :rtype: None
        """

        self.root = root
        self.mainFrameView = mainFrameView
        self.startXPosition = 120
        self.startYPosition = 20
        self.minMovement = -1
        self.refreshSec = 0.01
        self.primePng = primePng

        self.canvas_frame = Label(self.mainFrameView)
        self.canvas_frame.configure(bg="#333333", bd=0)
        self.canvas_frame.grid(row=0, column=7, sticky=W)
        self.canv = tk.Canvas(self.canvas_frame, width=120, height=30)
        self.canv.configure(bg="#333333", bd=0, highlightthickness=0, highlightbackground="black")
        self.canv.pack(expand=False)

    def animate_translucent(self) -> None:

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

    def animate_non_translucent(self) -> None:
        """
        The method display animation if the record is successfully added to the database.

        :return: animation non-transparent
        :rtype: None
        """

        # self.canvas_frame = Label(self.main_frame_view)
        # self.canvas_frame.configure(bg="#333333", bd=0)
        # self.canvas_frame.grid(row=0, column=7, sticky=W)
        # self.canvas_frame = tk.Canvas(self.canvas_frame, width=120, height=30)
        # self.canv.configure(bg="#333333", bd=0, highlightthickness=0, highlightbackground="black")
        # self.canv.pack(expand=False)

        #self.im = Image.open(self.primePng)
        #self.im.putalpha(120)
        #self.im.save('img/tip/ok.png')
        photo = PhotoImage(file='img/tip/okBegin.PNG')
        imageB = self.canv.create_image(120, 15, image=photo)

        while True:
            self.canv.move(imageB, self.minMovement, 0)
            self.root.update()
            time.sleep(self.refreshSec)
            imgPos = self.canv.coords(imageB)

            al, bl = imgPos

            #self.transparency = 120 + (2*(int(self.al) - 120))
            #self.im = Image.open('img/tip/ok.png')
            #self.im.putalpha(self.transparency)
            #self.im.save('img/tip/ok.png')
            photo = PhotoImage(file='img/tip/okBegin.PNG')
            imageB = self.canv.create_image(al, bl, image=photo)

            if al < abs(self.minMovement):
                self.minMovement = -self.minMovement
            if al == int(self.startXPosition) / 2:
                break

    def __del__(self) -> None:
        pass
