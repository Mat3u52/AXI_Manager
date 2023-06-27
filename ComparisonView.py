from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage, Button, StringVar
import tkinter as tk
from Comparison import Comparison
from Styles import Styles


class ComparisonView(Comparison):

    def __init__(self, dir_name: str, db_name: str, root: tk) -> None:
        """
        Constructor of ComparisonView class. Preparation of a few properties.

        param root: Given instance to tkinter
        :type root: tkinter
        :return: Init class
        :rtype: None
        """
        super().__init__(dir_name, db_name)

        self.v = StringVar(root, "0")
        self.v0 = StringVar(root, "0")
        self.extract_set: dict = {}
        self.extract_set0: dict = {}

        self.root = root

    def compare_list_to_db(self):
        print(self.recipes_list().difference(self.recipes_db()))

        i: int = 0
        self.extract_set0.clear()
        for value in dict.fromkeys(self.recipes_list().difference(self.recipes_db()), 0):
            self.extract_set0[i] = value
            i += 1

        row_count: int = 0
        for (text, value) in self.extract_set0.items():
            if len(value) > 0:
                ttk.Radiobutton(tab_3163_to_db,
                                text=value,
                                variable=self.v0,
                                value=text,
                                style="Comparison.TRadiobutton",
                                command=insert_from_comparison0,
                                ).grid(row=int(row_count),
                                       column=0,
                                       sticky=W)
                row_count += 1



