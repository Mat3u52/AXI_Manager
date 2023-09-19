from tkinter import W, ttk, StringVar, Scrollbar
import tkinter as tk

import pyperclip
from Comparison import Comparison
from Styles import Styles


class ComparisonView(Comparison):

    def __init__(self, dir_name: str, db_name: str, root: tk) -> None:
        """
        Constructor of ComparisonView class. Preparation of a few properties.

        :param dir_name: Given the name of machine directory
        :type dir_name: str
        :param db_name: Given the name of machine table
        :type db_name: str
        :param root: Given instance to tkinter
        :type root: tkinter
        :return: Init class
        :rtype: None
        """
        super().__init__(dir_name, db_name)

        self.root = root
        self.var = StringVar(self.root, "0")
        self.extract_set_to_dic: dict = {}
        self.extract_set_to_dic0: dict = {}
        self.radio_box: ttk = None

    def compare_list_to_db(self, tab: ttk.Frame) -> None:
        """
        Show difference between two set list

        :param tab: Given tab element
        :type tab: ttk.Frame
        :return: Init class
        :rtype: None
        """

        tab = tab

        i: int = 0
        self.extract_set_to_dic0.clear()
        for value in dict.fromkeys(self.recipes_list().difference(self.recipes_db()), 0):
            self.extract_set_to_dic0[i] = value
            i += 1
        row_count: int = 0
        for (text, value) in self.extract_set_to_dic0.items():
            if value is not None:
                if len(value) > 0 and value != "thumb":
                    self.radio_box = ttk.Radiobutton(tab,
                                                     text=value,
                                                     variable=self.var,
                                                     value=text,
                                                     style="Comparison.TRadiobutton",
                                                     command=self._insert_from_comparison0,)
                    self.radio_box.grid(row=int(row_count),
                                        column=0,
                                        sticky=W)
                    row_count += 1

    def compare_db_to_list(self, tab: ttk.Frame) -> None:
        """
        Show difference between two set list

        :param tab: Given tab element
        :type tab: ttk.Frame
        :return: Init class
        :rtype: None
        """

        tab = tab
        i: int = 0
        self.extract_set_to_dic.clear()
        for value in dict.fromkeys(self.recipes_db().difference(self.recipes_list()), 0):
            self.extract_set_to_dic[i] = value
            i += 1
        row_count: int = 0
        for (text, value) in self.extract_set_to_dic.items():
            if value is not None:
                if len(value) > 0 and value != "thumb":
                    ttk.Radiobutton(tab,
                                    text=value,
                                    variable=self.var,
                                    value=text,
                                    style="Comparison.TRadiobutton",
                                    command=self._insert_from_comparison,
                                    ).grid(row=int(row_count),
                                           column=0,
                                           sticky=W)
                    row_count += 1

    def _insert_from_comparison(self) -> None:
        """
        Put data to clipboard after click on name

        :return: None
        :rtype: None
        """

        pyperclip.copy(self.extract_set_to_dic[int(self.var.get())])

    def _insert_from_comparison0(self) -> None:
        """
        Put data to clipboard after click on name

        :return: None
        :rtype: None
        """

        pyperclip.copy(self.extract_set_to_dic0[int(self.var.get())])
