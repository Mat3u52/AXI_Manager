import tkinter


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
        The function moves the picture from the right to the left side.

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
        :return: animate the picture
        :rtype: None
        """
        self.ai_root: tkinter.Tk = ai_root
        self.canvas: tkinter.Canvas = canvas
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.img_path: str = img_path

        pass
