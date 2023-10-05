import tkinter
import time
import os


class Animation:
    min_movement: int = -1

    def __init__(self,
                 ai_root: tkinter.Tk,
                 canvas: tkinter.Canvas,
                 x_pos: int = -1,
                 y_pos: int = -1,
                 img_path: str = "board.png",
                 ) -> None:
        """
        Initialize the variables.

        :param ai_root: Given object from tkinter.Tk
        :type ai_root: tkinter.Tk
        :param canvas: Given object from tkinter.Canvas
        :type canvas: tkinter.Canvas
        :param x_pos: Given value of axis x
        :type x_pos: int
        :param y_pos: Given value of axis y
        :type y_pos: int
        :param img_path: Given path to .png file
        :type img_path: str
        :return: Initialize the variables
        :rtype: None
        """
        self.ai_root: tkinter.Tk = ai_root
        self.canvas: tkinter.Canvas = canvas
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.img_path: str = img_path

        self.start_x_position: int = 170
        self.start_y_position: int = 85
        self.refresh_sec: float = 0.01

    def move_image(self) -> None:
        """
        The function moves the picture from the right to the left side.

        :return: animate the picture
        :rtype: None
        """
        # start_x_position: int = 170
        # start_y_position: int = 85
        # refresh_sec: float = 0.01
        if os.path.isfile(self.img_path):
            img = tkinter.PhotoImage(file=self.img_path)
        else:
            img = tkinter.PhotoImage(file="img/lackOfPicture/board.png")

        ai_image = self.canvas.create_image(self.start_x_position, self.start_y_position, image=img)

        while True:
            self.canvas.move(ai_image, x_pos, 0)
            self.ai_root.update()
            time.sleep(self.refresh_sec)
            img_pos = self.canvas.coords(ai_image)
            al, bl = img_pos
            if al < abs(x_pos):
                x_pos = -x_pos
            if bl < abs(y_pos):
                y_pos = -y_pos
            if al == int(self.start_x_position) / 2:
                break
