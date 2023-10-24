import tkinter
from tkinter import ttk


class Search:
    def __init__(self, tree: ttk.Treeview, e_search: tkinter.Entry) -> None:
        self.tree = tree
        self.e_search = e_search

    def search_phrase(self) -> None:
        """
        The function is looking for the recipe by the phrase

        :return: records from DB according to phrase
        :rtype: None
        """
        self.tree.selection_clear()
        self.tree.selection_remove(self.tree.focus())
        for record in self.tree.get_children():
            content = self.tree.item(record, "values")
            if content[1].find(self.e_search.get()) >= 0:
                pass
            else:
                self.tree.delete(record)
