import tkinter
import time
import os
from PIL import Image
from Config import Config


class Animation:

    def __init__(self,
                 ai_root: tkinter.Tk,
                 canvas: tkinter.Canvas,
                 img_path: str = "board.png",
                 ) -> None:
        """
        Initialize the variables.

        :param ai_root: Given object from tkinter.Tk
        :type ai_root: tkinter.Tk
        :param canvas: Given object from tkinter.Canvas
        :type canvas: tkinter.Canvas
        :param img_path: Given path to .png file
        :type img_path: str
        :return: Initialize the variables
        :rtype: None
        """

        self.ai_root: tkinter.Tk = ai_root
        self.canvas: tkinter.Canvas = canvas
        self.x_pos: int = -1
        self.y_pos: int = -1
        self.img_path: str = img_path

    def move_image(self) -> None:
        """
        The function moves the picture from the right to the left side.

        :return: animate the picture
        :rtype: None
        """
        start_x_position: int = 170
        start_y_position: int = 85
        refresh_sec: float = 0.01
        if os.path.isfile(self.img_path):
            img = tkinter.PhotoImage(file=self.img_path)
        else:
            # img = tkinter.PhotoImage(file="img/lackOfPicture/board.png")
            img = tkinter.PhotoImage(Config().pathImgDefault)

        ai_image = self.canvas.create_image(start_x_position, start_y_position, image=img)

        while True:
            self.canvas.move(ai_image, self.x_pos, 0)
            self.ai_root.update()
            time.sleep(refresh_sec)
            img_pos = self.canvas.coords(ai_image)
            al, bl = img_pos
            if al < abs(self.x_pos):
                self.x_pos = -self.x_pos
            if bl < abs(self.y_pos):
                self.y_pos = -self.y_pos
            if al == int(start_x_position) / 2:
                break
    # print(move_image.__doc__)

    @staticmethod
    def resize_image(path: str) -> None:
        """
        The function resizes an image

        :param path: Given path to file
        :type path: str
        :return: New size of file
        :rtype: None
        """

        base_width: int = 120
        if os.path.isfile(path):
            if path.endswith(".jpg"):
                convert_jpg_to_png = Image.open(r"" + path)
                width_percent = base_width / float(convert_jpg_to_png.size[0])
                hsize = int((float(convert_jpg_to_png.size[1]) * float(width_percent)))
                convert_jpg_to_png = convert_jpg_to_png.resize(
                    (base_width, hsize), Image.Resampling.NEAREST
                )
                path_png = path.replace(".jpg", ".png")
                convert_jpg_to_png.save(r"" + path_png)

            # elif path.endswith(".png"):
            #     print("f: resizeImage - .png")
    # print(resize_image.__doc__)
