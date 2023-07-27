from tkinter import *
import tkinter as tk
import pyperclip


class ContextualMenu:
    def __init__(self, root: tk) -> None:
        self.root = root
        self.captureEntry = StringVar()

        # self.contextMenu = Menu(self.root, tearoff=0)
        # self.contextMenu.add_command(label="Copy", command=self._copy)
        # self.contextMenu.add_command(label="Paste", command=self._paste)
        # self.contextMenu.add_command(label="Remove", command=self._remove)

    def doPopup(self,
                # event: str,
                x,
                y,
                copy: bool = True,
                paste: bool = True,
                remove: bool = True) -> None:

        context_menu = Menu(self.root, tearoff=0)
        if copy is True:
            context_menu.add_command(label="Copy", command=self._copy)
        if paste is True:
            context_menu.add_command(label="Paste", command=self._paste)
        if remove is True:
            context_menu.add_command(label="Remove", command=self._remove)
        try:
            context_menu.tk_popup(x, y)
            # context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            context_menu.grab_release()

    def _copy(self) -> None:
        try:
            pyperclip.copy(self.captureEntry.get())
        except AttributeError:
            pass

    def setEntry(self, entry_fild) -> None:
        self.entry_fild = entry_fild

    def _paste(self) -> None:
        self.entry_fild.insert(tk.END, pyperclip.paste())

    def _remove(self) -> None:
        pass
