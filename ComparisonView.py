from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage, Button, StringVar
import tkinter as tk
from Comparison import Comparison
from Styles import Styles


class ComparisonView(Comparison):

    def __init__(self, dir_name: str, db_name: str, root: tk, tab: ttk.Frame) -> None:
        """
        Constructor of ComparisonView class. Preparation of a few properties.

        param root: Given instance to tkinter
        :type root: tkinter
        :return: Init class
        :rtype: None
        """
        super().__init__(dir_name, db_name)

        self.root = root
        self.tab = tab

        # self.v = StringVar(root, "0")
        self.var = StringVar(self.root, "0")
        # self.extract_set: dict = {}
        self.extract_set_to_dic: dict = {}

    def compare_list_to_db(self):
        # print(self.recipes_list().difference(self.recipes_db()))

        i: int = 0
        self.extract_set_to_dic.clear()
        for value in dict.fromkeys(self.recipes_list().difference(self.recipes_db()), 0):
            self.extract_set_to_dic[i] = value
            i += 1
        print(self.extract_set_to_dic)
        row_count: int = 0
        for (text, value) in self.extract_set_to_dic.items():
            if len(value) > 0:
                ttk.Radiobutton(self.tab,
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
        pass
        # print(extract_set[int(v.get())])
        # pyperclip.copy(extract_set[int(v.get())])



