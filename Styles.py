from tkinter import ttk
class Styles:
    def __init__(self, root):
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
                                       'background': '#111111',  # 302928
                                       'foreground': '#FFFFFF',
                                       'anchor': 'N',
                                       'font': ("Arial", 12, 'bold'),
                                       'borderwidth': 1,
                                       'relief': "solid"
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
        self.style.map('Treeview', background=[('selected', '#46464A')])
