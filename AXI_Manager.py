from DBConnect import DBConnect
import tkinter as tk
from tkinter import ttk
import math
from tkinter import *
tab = []

def swich(x):
    match x:
        case "NONE":
            return 0
        case "YES":
            return 1
        case "NO":
            return 2
        case "LACK":
            return 3
        case _:
            return 0

def getSelectedRow(event):
    tab.clear()
    E1.config(state="normal")
    objDB = DBConnect()
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
    #print(tree.selection())  # this will print the names of the selected rows
    for nm in tree.selection():
        #content.clear()
        content = tree.item(nm, 'values')
    print(content[0])
    print(type(int(content[0])))
    if int(content[0]) >= 0:
        for row in objDB.selectSearchID(content[0]):
            # E1.insert(0, f"{content[0]}")
            tab.append(row[0])
            # tab.append(row[49])
            E1.insert(0, f"{row[0]}")
            print(row[1])
            E1.config(state="disabled")
            E2.insert(0, f"{row[1]}")
            E3.insert(0, f"{row[3]}")
            E4.insert(0, f"{row[54]}")
            E5.insert(0, f"{row[52]}")
            E6.insert(0, f"{row[57]}")

            LCViTroxIV.current(swich(row[55]))
            EPIViTroxIV.current(swich(row[56]))
            BAANViTroxIV.current(swich(row[53]))


        objDB.closeDB()

def updateDisplay():
    if int(tab[0]) >= 0:
        objDB = DBConnect()
        objDB.update(tab[0], E2.get(), E3.get(), E4.get(), E5.get(), LCViTroxIV.get(), EPIViTroxIV.get(),
                    BAANViTroxIV.get(), E6.get())
        objDB.closeDB()
        #tree.delete(1)
        selected_item = tree.selection()[0]
        tree.item(selected_item, text=E2.get(), values=("foo", "bar")) #<-- in values I have to download data from DB

def insertData():
    objDB = DBConnect()
    objDB.insert(EI2.get(), EI3.get(), EI4.get(), EI5.get(), LCViTroxIVInsert.get(), EPIViTroxIVInsert.get(),
                 BAANViTroxIVInsert.get(), EI6.get())
    objDB.closeDB()

#def delete():
   # Get selected item to Delete
#   selected_item = tree.selection()[0]
#   tree.delete(selected_item)


root = tk.Tk()
root.title('AXI - Manager')
root.resizable(0,0)
root.configure(background='#000000')

style= ttk.Style()
style.theme_create('style_class',

                   # getting the settings
                   settings={

                       # getting through the Labelframe
                       # widget
                       'TLabelframe': {

                           # configure the changes
                           'configure': {
                               'background': '#333333',
                               'borderwidth': '10'
                           }
                       },

                       # getting through the Labelframe's
                       # label widget
                       'TLabelframe.Label': {
                           'configure': {
                               'background': '#000000',
                               'foreground': '#FFFFFF'
                           }
                       },

                       'TButton':{
                           'configure':{
                                'background': '#302928',
                                'foreground': '#FFFFFF',
                                'anchor': N
                           }
                       }
                   }
                   )
style.theme_use('style_class')
#style.theme_use('clam')
#style.theme_use('Arc')

mainFrame = ttk.LabelFrame(root, text="Update Frame:")
mainFrame.grid(column=0, row=0, columnspan=10, sticky='W', padx=10, pady=10)
updateFrameVIV = ttk.LabelFrame(root, text="Update ViTrox V810 Ex III ( V810-3553S2EX ):")
updateFrameVIV.grid(column=0, row=1, columnspan=10, sticky='W', padx=10, pady=10)

L1 = Label(mainFrame, text="ID:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L1.config(font=("Arial", 10))
L2 = Label(mainFrame, text="Item:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L2.config(font=("Arial", 10))
L3 = Label(mainFrame, text="Qty:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L3.config(font=("Arial", 10))
L4 = Label(updateFrameVIV, text="Program name:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L4.config(font=("Arial", 10))
L5 = Label(updateFrameVIV, text="Scanning Time:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L5.config(font=("Arial", 10))
L6 = Label(updateFrameVIV, text="LC:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L6.config(font=("Arial", 10))
L7 = Label(updateFrameVIV, text="EPI:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L7.config(font=("Arial", 10))
L8 = Label(updateFrameVIV, text="BAAN:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L8.config(font=("Arial", 10))
L9 = Label(updateFrameVIV, text="V810 Ex III Comments", width=29, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L9.config(font=("Arial", 10))

L1.grid(row=0, column=0, sticky=W)
L2.grid(row=0, column=2, sticky=W)
L3.grid(row=0, column=4, sticky=W)
L4.grid(row=1, column=0, sticky=W)
L5.grid(row=1, column=2, sticky=W)
L6.grid(row=1, column=4, sticky=W)
L7.grid(row=1, column=6, sticky=W)
L8.grid(row=1, column=8, sticky=W)
L9.grid(row=2, column=0, columnspan = 2, sticky=W)

E1 = Entry(mainFrame, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
E1.config(font=("Arial", 10))
E1.grid(row=0, column=1, pady=0)
E2 = Entry(mainFrame, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
E2.config(font=("Arial", 10))
E2.grid(row=0, column=3, pady=0)
E3 = Entry(mainFrame, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
E3.config(font=("Arial", 10))
E3.grid(row=0, column=5, pady=0)
E4 = Entry(updateFrameVIV, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
E4.config(font=("Arial", 10))
E4.grid(row=1, column=1, pady=0)
E5 = Entry(updateFrameVIV, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
E5.config(font=("Arial", 10))
E5.grid(row=1, column=3, pady=0)
E6 = Entry(updateFrameVIV, relief="solid", width=137, borderwidth=0, bg="#302928", fg="#FFFFFF")
E6.config(font=("Arial", 10))
E6.grid(row=2, column=2, columnspan = 8, pady=0)
#E6 = Entry(root, bd=0)
#E6.grid(row=1, column=5, pady=2)

LC = tk.StringVar
LCViTroxIV = ttk.Combobox(updateFrameVIV, width=20, textvariable=LC, state='readonly')
LCViTroxIV['values'] = ("NONE","YES","NO","LACK")
LCViTroxIV.grid(row=1, column=5, pady=0)
LCViTroxIV.current(0)
EPI = tk.StringVar
EPIViTroxIV = ttk.Combobox(updateFrameVIV, width=20, textvariable=EPI, state='readonly')
EPIViTroxIV['values'] = ("NONE","YES","NO","LACK")
EPIViTroxIV.grid(row=1, column=7, pady=0)
EPIViTroxIV.current(0)
BAAN = tk.StringVar
BAANViTroxIV = ttk.Combobox(updateFrameVIV, width=20, textvariable=BAAN, state='readonly')
BAANViTroxIV['values'] = ("NONE","YES","NO","LACK")
BAANViTroxIV.grid(row=1, column=9, pady=0)
BAANViTroxIV.current(0)

B1 = ttk.Button(updateFrameVIV, text="Update", width=100, command=updateDisplay)
B1.grid(row=3, column=0, columnspan = 10, pady=2)

#-----------------INSERT-------------------
mainFrameInsert = ttk.LabelFrame(root, text="Insert Frame:")
mainFrameInsert.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)

insertFrameVIV = ttk.LabelFrame(root, text="Insert ViTrox V810 Ex III ( V810-3553S2EX ):")
insertFrameVIV.grid(column=0, row=3, columnspan=10, sticky='W', padx=10, pady=10)

#LI1 = Label(mainFrameInsert, text="ID:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
#LI1.config(font=("Arial", 10))
LI2 = Label(mainFrameInsert, text="Item:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI2.config(font=("Arial", 10))
LI3 = Label(mainFrameInsert, text="Qty:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI3.config(font=("Arial", 10))
LI4 = Label(insertFrameVIV, text="Program name:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI4.config(font=("Arial", 10))
LI5 = Label(insertFrameVIV, text="Scanning Time:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI5.config(font=("Arial", 10))
LI6 = Label(insertFrameVIV, text="LC:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI6.config(font=("Arial", 10))
LI7 = Label(insertFrameVIV, text="EPI:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI7.config(font=("Arial", 10))
LI8 = Label(insertFrameVIV, text="BAAN:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI8.config(font=("Arial", 10))
LI9 = Label(insertFrameVIV, text="V810 Ex III Comments", width=29, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI9.config(font=("Arial", 10))

#LI1.grid(row=0, column=0, sticky=W)
LI2.grid(row=0, column=2, sticky=W)
LI3.grid(row=0, column=4, sticky=W)
LI4.grid(row=1, column=0, sticky=W)
LI5.grid(row=1, column=2, sticky=W)
LI6.grid(row=1, column=4, sticky=W)
LI7.grid(row=1, column=6, sticky=W)
LI8.grid(row=1, column=8, sticky=W)
LI9.grid(row=2, column=0, columnspan = 2, sticky=W)

#EI1 = Entry(mainFrameInsert, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
#EI1.config(font=("Arial", 10))
#EI1.grid(row=0, column=1, pady=0)
EI2 = Entry(mainFrameInsert, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
EI2.config(font=("Arial", 10))
EI2.grid(row=0, column=3, pady=0)
EI3 = Entry(mainFrameInsert, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
EI3.config(font=("Arial", 10))
EI3.grid(row=0, column=5, pady=0)
EI4 = Entry(insertFrameVIV, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
EI4.config(font=("Arial", 10))
EI4.grid(row=1, column=1, pady=0)
EI5 = Entry(insertFrameVIV, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
EI5.config(font=("Arial", 10))
EI5.grid(row=1, column=3, pady=0)
EI6 = Entry(insertFrameVIV, relief="solid", width=137, borderwidth=0, bg="#302928", fg="#FFFFFF")
EI6.config(font=("Arial", 10))
EI6.grid(row=2, column=2, columnspan = 8, pady=0)
#E6 = Entry(root, bd=0)
#E6.grid(row=1, column=5, pady=2)

LCInsert = tk.StringVar
LCViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=20, textvariable=LCInsert, state='readonly')
LCViTroxIVInsert['values'] = ("NONE","YES","NO","LACK")
LCViTroxIVInsert.grid(row=1, column=5, pady=0)
LCViTroxIVInsert.current(0)
EPIInsert = tk.StringVar
EPIViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=20, textvariable=EPIInsert, state='readonly')
EPIViTroxIVInsert['values'] = ("NONE","YES","NO","LACK")
EPIViTroxIVInsert.grid(row=1, column=7, pady=0)
EPIViTroxIVInsert.current(0)
BAANInsert = tk.StringVar
BAANViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=20, textvariable=BAANInsert, state='readonly')
BAANViTroxIVInsert['values'] = ("NONE","YES","NO","LACK")
BAANViTroxIVInsert.grid(row=1, column=9, pady=0)
BAANViTroxIVInsert.current(0)

BI1 = ttk.Button(insertFrameVIV, text="Insert", width=100, command=insertData)
BI1.grid(row=3, column=0, columnspan = 10, pady=2)
#-----------------The End INSERT-----------

tree = ttk.Treeview(root)
tree["columns"] = ("one", "two", "three", "Four")
tree.column("#0", width=40, minwidth=40, stretch=tk.NO)
tree.column("one", width=35, minwidth=35, stretch=tk.NO)
tree.column("two", width=190, minwidth=190, stretch=tk.NO)
tree.column("three", width=130, minwidth=130, stretch=tk.NO)
tree.column("Four", width=30, minwidth=30, stretch=tk.NO)

tree.heading("#0", text="Box", anchor=tk.W)
tree.heading("one", text="ID", anchor=tk.W)
tree.heading("two", text="Item", anchor=tk.W)
tree.heading("three", text="Date / Time", anchor=tk.W)
tree.heading("Four", text="Qty", anchor=tk.W)

objDB = DBConnect()

count = 1
count1 = 1
count2 = 0
handling = 15

for row in objDB.selectAll():
    #if row[7] is not float:
    #    scanningTime5DX = 0
    #else:
    scanningTime5DX = int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(handling)

    folder1 = tree.insert(parent='', index=count, iid=count1, text=f'box',
                          values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}'))
    count1 += 1
    if int(len(str(row[17]))) > 4:
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[17]}',
        #            values=(f"5DX I", f"Scanning Time: {scanningTime5DX}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values =(f'{row[0]}', f'5DX I', f"Scanning Time: {scanningTime5DX}", ""))
    count1 += 2
    if int(len(str(row[22]))) > 4:
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[22]}',
        #            values=(f"5DX II", f"Scanning Time: {scanningTime5DX}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values=(f'{row[0]}', f"5DX II", f"Scanning Time: {scanningTime5DX}", ""))
    count1 += 3
    #if row[27] != None:
    if len(str(row[27])) > 4:
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[27]}',
        #            values=(f"ViTroxEx I", f"Scanning Time: {int(row[15]) + handling}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values=(f'{row[0]}', f"ViTroxEx I", f"Scanning Time: {int(row[15]) + handling}", ""))
    count1 += 4
    if row[45] != None and int(row[41]) != 0:
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[45]}',
        #            values=(f"ViTroxEx II", f"Scanning Time: {int(row[41]) + handling}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values=(f'{row[0]}', f"ViTroxEx II", f"Scanning Time: {int(row[41]) + handling}", ""))
    count1 += 4
    if row[54] != None and int(row[50] != 0):
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[54]}',
        #            values=(f"ViTroxEx III", f"Scanning Time: {int(row[52]) + handling}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values=(f'{row[0]}', f"ViTroxEx III", f"Scanning Time: {int(row[52]) + handling}", ""))
    count1 += 5

    if row[31] != None and int(row[37] != 0):
        #tree.insert(folder1, index='end', iid=count1, text=f'{row[31]}',
        #            values=(f"ViTroxXXL I", f"Scanning Time: {int(row[37]) + handling}", ""))
        tree.insert(folder1, index='end', iid=count1, text=f'',
                    values=(f'{row[0]}', f"ViTroxXXL I", f"Scanning Time: {int(row[37]) + handling}", ""))

    tree.bind("<<TreeviewSelect>>", getSelectedRow)

    #tree.pack(side=tk.BOTTOM, fill=tk.X)
    tree.grid(row=4, column=0, columnspan = 10, pady=2)

    count += 1
    count1 += 1
    count2 += 1
objDB.closeDB()

root.mainloop()