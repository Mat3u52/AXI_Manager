import tkinter as tk
from tkinter import Label, W, PhotoImage
import time
from PIL import Image


class Tip:
    def __init__(self, root: tk, main_frame_view: tk, prime_png: str = 'img/tip/okBegin.png') -> None:
        """
        Preparation of canvas area.

        :param root: handel to main window
        :type root: tk
        :param main_frame_view: handel to frame
        :type main_frame_view: tk
        :param prime_png: path to the .png file
        :type prime_png: str
        :return: prepare canvas area
        :rtype: None
        """

        self.root = root
        self.main_frame_view = main_frame_view
        self.start_x_position = 120
        self.start_y_position = 20
        self.min_movement = -1
        self.refresh_sec = 0.01
        self.prime_png = prime_png

        self.canvas_frame = Label(self.main_frame_view)
        self.canvas_frame.configure(bg="#333333", bd=0)
        self.canvas_frame.grid(row=0, column=7, sticky=W)
        self.canvas_created = tk.Canvas(self.canvas_frame, width=120, height=30)
        self.canvas_created.configure(bg="#333333", bd=0, highlightthickness=0, highlightbackground="black")
        self.canvas_created.pack(expand=False)

    def animate_translucent(self) -> None:
        """
        Translucent of image

        :return: transparent
        :rtype: None
        """

        im = Image.open(self.prime_png)
        im.putalpha(120)
        im.save('img/tip/ok.png')
        photo = PhotoImage(file='img/tip/ok.png')
        image_b = self.canvas_created.create_image(120, 15, image=photo)

        while True:
            self.canvas_created.move(image_b, self.min_movement, 0)
            self.root.update()
            time.sleep(self.refresh_sec)
            img_pos = self.canvas_created.coords(image_b)

            al, bl = img_pos

            transparency = 120 + (2*(int(al) - 120))
            im = Image.open('img/tip/ok.png')
            im.putalpha(transparency)
            im.save('img/tip/ok.png')
            photo = PhotoImage(file='img/tip/ok.png')
            image_b = self.canvas_created.create_image(al, bl, image=photo)

            if al < abs(self.min_movement):
                self.min_movement = -self.min_movement
            if al == int(self.start_x_position) / 2:
                break

    def animate_non_translucent(self) -> None:
        """
        The method display animation if the record is successfully added to the database.

        :return: animation non-transparent
        :rtype: None
        """

        photo = PhotoImage(file='img/tip/okBegin.png')
        image_b = self.canvas_created.create_image(120, 15, image=photo)

        while True:
            self.canvas_created.move(image_b, self.min_movement, 0)
            self.root.update()
            time.sleep(self.refresh_sec)
            img_pos = self.canvas_created.coords(image_b)
            al, bl = img_pos
            photo = PhotoImage(file='img/tip/okBegin.png')
            image_b = self.canvas_created.create_image(al, bl, image=photo)

            if al < abs(self.min_movement):
                self.min_movement = -self.min_movement
            if al == int(self.start_x_position) / 2:
                break

    def __del__(self) -> None:
        pass
