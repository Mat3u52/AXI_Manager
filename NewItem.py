from tkinter import ttk
from tkinter import *
from ContextualMenu import ContextualMenu


class NewItem:
    def __init__(self, tab: ttk, root: ttk) -> None:
        """
        Template for insert a new record.

        :param tab: handle to frame
        type tab: ttk
        :param root: handle to main window
        :type root: ttk
        :return: template of form
        :rtype: None
        """

        self.tab: ttk = tab
        self.root: ttk = root
        self.main_frame: ttk = None
        self.entry_item: ttk = None
        self.entry_qty: ttk = None
        self.checkbox_frame = None

    def main_frame_insert(self, main_name: str = " ") -> None:
        """
        template with two main input fields: item and qty.

        :param main_name: name of frame
        :type main_name: str
        :return: template of form
        :rtype: None
        """

        main_name: str = main_name
        self.main_frame = ttk.LabelFrame(self.tab, text=main_name)
        self.main_frame.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)
        label_item = Label(self.main_frame,
                           text="Item:",
                           width=12,
                           borderwidth=1,
                           relief="solid",
                           bg="#212121",
                           fg="#555555",
                           pady="1")
        label_item.config(font=("Arial", 10))
        label_qty = Label(self.main_frame,
                          text="Qty:",
                          width=12,
                          borderwidth=1,
                          relief="solid",
                          bg="#212121",
                          fg="#555555",
                          pady="1")
        label_qty.config(font=("Arial", 10))

        label_item.grid(row=0, column=0, sticky=W)
        label_qty.grid(row=0, column=2, sticky=W)

        obj_contextual_menu = ContextualMenu(self.root, '0', True, True, False)
        self.entry_item = Entry(self.main_frame,
                                relief="solid",
                                textvariable=obj_contextual_menu.captureEntry,
                                borderwidth=1,
                                width=35,
                                bg="#212121",
                                fg="#FFFFFF")
        self.entry_item.config(font=("Arial", 10),
                               highlightbackground="#000000",
                               highlightcolor="#33FFBE")
        self.entry_item.grid(row=0, column=1, pady=1)
        self.entry_item.bind("<Button-3>", obj_contextual_menu.do_popup)
        obj_contextual_menu.set_entry(self.entry_item)

        self.entry_qty = Entry(self.main_frame,
                               relief="solid",
                               borderwidth=1,
                               width=10,
                               bg="#212121",
                               fg="#FFFFFF")
        self.entry_qty.config(font=("Arial", 10),
                              highlightbackground="#000000",
                              highlightcolor="#33FFBE")
        self.entry_qty.grid(row=0, column=3, pady=1, stick=W)

    def checkbox_title(self, checkbox_title: str, row: int) -> None:
        """
        template for checkbox with kinds of axi.

        :param checkbox_title: type name of axi
        :type checkbox_title: str
        :param row: checkbox row
        :type row: int
        :return: template of checkbox
        :rtype: None
        """

        row = row
        checkbox_title = checkbox_title
        self.checkbox_frame = ttk.LabelFrame(self.tab, text=checkbox_title)
        self.checkbox_frame.grid(column=0, row=row, sticky='W', padx=10, pady=10)

    def clean_up(self) -> None:
        """
        The method clean up the form.

        :return: clean up entry
        :rtype: None
        """

        self.entry_item.delete(0, END)
        self.entry_qty.delete(0, END)
