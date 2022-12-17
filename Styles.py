from tkinter import ttk


class Styles:
    def __init__(self, root: ttk.tkinter) -> None:
        self.root = root
        self.style = ttk.Style()
        self.style.theme_create('style_class',
                           settings={
                               'TLabelframe': {
                                   'configure': {
                                       'background': '#333333',
                                       'foreground': '#FFFFFF',
                                       'borderwidth': '10'
                                   }
                               },

                               'TLabelframe.Label': {
                                   'configure': {
                                       'background': '#000000',
                                       'foreground': '#FFFFFF'
                                   }
                               },

                               'TButton': {
                                   'configure': {
                                       'background': '#111111',
                                       'foreground': '#FFFFFF',
                                       'anchor': 'N',
                                       'font': ("Arial", 12, 'bold'),
                                       'borderwidth': 1,
                                       'relief': "solid"
                                   }
                               },

                               'AutomaticInsert.TRadiobutton': {
                                   'configure': {
                                       'indicatorrelief': 'tk.FLAT',
                                       'indicatormargin': '-1',
                                       'indicatordiameter': '-1',
                                        'relief': 'tk.RAISED',
                                        'focusthickness': '8',
                                        'highlightthickness': '#000000',
                                        'padding': '4',
                                        'background': '#333333',
                                        'foreground': '#AAAAAA'
                                   },
                                   'map': {
                                       'background': [('selected', '#444444'), ('active', '#777777')]
                                   }
                               }
                           }
                           )
        self.style.theme_use('style_class')

        # ---Notebook Style---
        self.noteStyler = ttk.Style()
        self.noteStyler.configure("TNotebook", background='#555555', borderwidth=0)
        self.noteStyler.configure("TNotebook.Tab", background='#555555', foreground='#FFFFFF', lightcolor='#FFFFFF',
                             borderwidth=1)
        self.noteStyler.configure("TFrame", background='#444444', foreground='#FFFFFF', borderwidth=1)

        self.style.configure("TCombobox", fieldbackground="#333333", background="#302928", borderwidth=0)
        self.root.option_add("*TCombobox*Listbox*Background", "#302928")
        self.root.option_add("*TCombobox*Listbox*Foreground", "#AAAAAA")

        self.style.configure("Treeview", background="#000000", foreground="#FFFFFF", rowheight=40, filedbackground="#777777")
        self.style.map('Treeview', background=[('selected', '#46464A'), ('active', '#000000')])

