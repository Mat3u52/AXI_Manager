import tkinter as tk
import pyperclip
from tkinter import Menu, StringVar
from RemoveRecord import RemoveRecord


class ContextualMenu(RemoveRecord):
    def __init__(self,
                 root: tk,
                 id_record: str = "0",
                 copy: bool = True,
                 paste: bool = True,
                 remove: bool = True) -> None:
        """
        Initialization of the variables and define list of options

        :param root: handle to main window
        :type root: tkinter
        :param id_record: give id of the record from database
        :type id_record: str
        :param copy: give the status for the copy option
        :type copy: bool
        :param paste: give the status for the paste option
        :type paste: bool
        :param remove: give the status for the remove option
        :type remove: bool
        :return: list of options
        :rtype: None
        """
        super(ContextualMenu, self).__init__(id_record)

        self.root = root
        self.captureEntry = StringVar()
        self.id_record = id_record

        self.copy = copy
        self.paste = paste
        self.remove = remove
        # self.entry_fild = ''

        self.context_menu = Menu(self.root, tearoff=0)
        if copy is True:
            self.context_menu.add_command(label="Copy", command=self._copy)
        if paste is True:
            self.context_menu.add_command(label="Paste", command=self._paste)
        if remove is True:
            self.context_menu.add_command(label=f"Remove {self.id_record}", command=self._remove)

    def do_popup(self, event: any) -> None:
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def release_contextual_menu(self, event: any) -> None:
        try:
            # self.context_menu.tk_popup(event.x_root, event.y_root)
            self.context_menu.unpost()
        finally:
            pass
    # def popupFocusOut(self, event=None):
    #     rcmenu.unpost()

    def _copy(self) -> None:
        try:
            pyperclip.copy(self.captureEntry.get())
        except AttributeError:
            pass

    def set_entry(self, entry_fild: any) -> None:
        self.entry_fild = entry_fild

    def _paste(self) -> None:
        self.entry_fild.insert(tk.END, pyperclip.paste())

    def _remove(self) -> None:
        self.remove_total()
