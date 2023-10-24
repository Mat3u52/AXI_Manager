from tkinter import ttk
from Config import Config


class Scrollbar(Config):

    def __init__(self, tab: ttk.tkinter, tree: ttk.tkinter) -> None:
        """
        Initialization of variables

        :param tab: handle to tab
        :type tab: ttk.tkinter
        :param tree: handle to tree view
        :type tree: ttk.tkinter
        :return: Init of variables
        :rtype: None
        """
        Config.__init__(self)
        self.tab = tab
        self.tree = tree

    def tree_scrollbar(self) -> None:
        """
        Scrollbar for tree view

        :return: show scrollbar for tree view
        :rtype: None
        """
        vsb = ttk.Scrollbar(self.tab, orient="vertical", command=self.tree.yview)
        vsb.place(
            x=Config().scrollX, y=Config().scrollY, height=Config().scrollHeight
        )
        self.tree.configure(yscrollcommand=vsb.set)
