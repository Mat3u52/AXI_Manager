from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage, Button, StringVar
import tkinter as tk
from Comparison import Comparison


class ComparisonView(Comparison):

    # v = StringVar(root, "0")
    # v0 = StringVar(root, "0")
    # extract_set: dict = {}
    # extract_set0: dict = {}

    def __init__(self, dir_name: str, db_name: str, root: tk) -> None:
        """
        Constructor of ComparisonView class. Preparation of a few properties.

        param root: Given instance to tkinter
        :type root: tkinter
        :return: Init class
        :rtype: None
        """
        super().__init__(dir_name, db_name)

        self.root = root

    def compare(self):
        pass
        # obj_comparison = Comparison(dir_name="/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3163/",
        #                             db_name="VITROXI_PROG")
        # i: int = 0
        # extract_set0.clear()
        # for value in dict.fromkeys(obj_comparison.recipes_list().difference(obj_comparison.recipes_db()), 0):
        #     extract_set0[i] = value
        #     i += 1
        #
        # row_count: int = 0
        # for (text, value) in extract_set0.items():
        #     if len(value) > 0:
        #         ttk.Radiobutton(tab_3163_to_db,
        #                         text=value,
        #                         variable=v0,
        #                         value=text,
        #                         style="Comparison.TRadiobutton",
        #                         command=insert_from_comparison0,
        #                         ).grid(row=int(row_count),
        #                                column=0,
        #                                sticky=W)
        #         row_count += 1



