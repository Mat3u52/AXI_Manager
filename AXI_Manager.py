from DBConnect import DBConnect
import tkinter as tk
from tkinter import ttk
import math
from tkinter import *
tab = []
def getSelectedRow(event):
    tab.clear()
    E1.config(state="normal")
    objDB = DBConnect()
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    print(tree.selection())  # this will print the names of the selected rows
    for nm in tree.selection():
        content = tree.item(nm, 'values')
    print(content[0])
    #E1.insert(0, f"{content[0]}")

    for row in objDB.selectSearchID(content[0]):
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
        tab.append(row[0])
        tab.append(row[1])
        tab.append(row[3])
        tab.append(row[54])
        tab.append(row[52])
        #tab.append(row[53])
        E1.insert(0, f"{row[0]}")
        E1.config(state="disabled")
        E2.insert(0, f"{row[1]}")
        E3.insert(0, f"{row[3]}")
        E4.insert(0, f"{row[54]}")
        E5.insert(0, f"{row[52]}")
        LCViTroxIV.current(swich(row[55]))


    objDB.closeDB()

def updateDisplay():
    objDB = DBConnect()
    objDB.update(tab[0], E2.get(), E3.get(), E4.get(), E5.get(), LCViTroxIV.get())
    objDB.closeDB()
    #tree.delete(1)
    selected_item = tree.selection()[0]
    tree.item(selected_item, text=E2.get(), values=("foo", "bar")) #<-- in values I have to download data from DB

def insertData():
    objDB = DBConnect()
    objDB.insert(E3)
    objDB.closeDB()

#def delete():
   # Get selected item to Delete
#   selected_item = tree.selection()[0]
#   tree.delete(selected_item)


root = tk.Tk()
root.title('AXI - Manager')
root.resizable(0,0)

L1 = Label(root, text="ID:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L1.config(font=("Arial", 10))
L2 = Label(root, text="Item:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L2.config(font=("Arial", 10))
L3 = Label(root, text="Qty:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L3.config(font=("Arial", 10))
L4 = Label(root, text="V810 Ex III:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L4.config(font=("Arial", 10))
L5 = Label(root, text="Scanning Time:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L5.config(font=("Arial", 10))
L6 = Label(root, text="LC:", borderwidth=1, relief="solid", bg="#302928", fg="#FFFFFF", pady="0")
L6.config(font=("Arial", 10))

L1.grid(row=0, column=0, sticky=W)
L2.grid(row=0, column=2, sticky=W)
L3.grid(row=0, column=4, sticky=W)
L4.grid(row=1, column=0, sticky=W)
L5.grid(row=1, column=2, sticky=W)
L6.grid(row=1, column=4, sticky=W)

E1 = Entry(root, bd=0)
E1.grid(row=0, column=1, pady=2)
E2 = Entry(root, bd=0)
E2.grid(row=0, column=3, pady=2)
E3 = Entry(root, bd=0)
E3.grid(row=0, column=5, pady=2)
E4 = Entry(root, bd=0)
E4.grid(row=1, column=1, pady=2)
E5 = Entry(root, bd=0)
E5.grid(row=1, column=3, pady=2)
#E6 = Entry(root, bd=0)
#E6.grid(row=1, column=5, pady=2)
LC = tk.StringVar
LCViTroxIV = ttk.Combobox(root, width=12, textvariable=LC, state='readonly')
LCViTroxIV['values'] = ("NONE","YES","NO","LACK")
LCViTroxIV.grid(row=1, column=5, pady=2)
LCViTroxIV.current(0)

B1 = ttk.Button(root, text="Update", command=updateDisplay)
B1.grid(row=4, column=0, pady=2)

'''
L3 = Label(root, text="Item:")
L4 = Label(root, text="Program name:")
L3.grid(row=4, column=0, sticky=W, pady=2)
L4.grid(row=5, column=0, sticky=W, pady=2)

E4 = Entry(root, bd=0)
E4 = Entry(root, bd=0)
E4.grid(row=4, column=1, pady=2)
E4.grid(row=5, column=1, pady=2)

B1 = ttk.Button(root, text="Insert", command=insertData)
B1.grid(row=6, column=1, pady=2)
'''

tree = ttk.Treeview(root)
tree["columns"] = ("one", "two", "three")
tree.column("#0", width=200, minwidth=200, stretch=tk.NO)
tree.column("one", width=80, minwidth=80, stretch=tk.NO)
tree.column("two", width=120, minwidth=120, stretch=tk.NO)
tree.column("three", width=30, minwidth=30, stretch=tk.NO)

tree.heading("#0", text="Item", anchor=tk.W)
tree.heading("one", text="ID", anchor=tk.W)
tree.heading("two", text="Date / Time", anchor=tk.W)
tree.heading("three", text="Qty", anchor=tk.W)

objDB = DBConnect()

count = 1
count1 = 1
count2 = 0
handling = 15

for row in objDB.selectAll():
    scanningTime5DX = int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + handling
    folder1 = tree.insert(parent='', index=count, iid=count1, text=f'{row[1]}',
                          values=(f'{row[0]}', f'{row[2]}', f'{row[3]}'))
    count1 += 1
    if len(row[17]) > 4:
        tree.insert(folder1, index='end', iid=count1, text=f'{row[17]}',
                    values=(f"5DX I", f"Scanning Time: {scanningTime5DX}", ""))
    count1 += 2
    if len(row[22]) > 4:
        tree.insert(folder1, index='end', iid=count1, text=f'{row[22]}',
                    values=(f"5DX II", f"Scanning Time: {scanningTime5DX}", ""))
    count1 += 3
    if len(row[27]) > 4:
        tree.insert(folder1, index='end', iid=count1, text=f'{row[27]}',
                    values=(f"ViTroxEx I", f"Scanning Time: {int(row[15]) + handling}", ""))
    count1 += 4
    if row[45] != None and int(row[41]) != 0:
        tree.insert(folder1, index='end', iid=count1, text=f'{row[45]}',
                    values=(f"ViTroxEx II", f"Scanning Time: {int(row[41]) + handling}", ""))
    count1 += 4
    if row[54] != None and int(row[50] != 0):
        tree.insert(folder1, index='end', iid=count1, text=f'{row[54]}',
                    values=(f"ViTroxEx III", f"Scanning Time: {int(row[52]) + handling}", ""))
    count1 += 5
    if row[31] != None and int(row[37] != 0):
        tree.insert(folder1, index='end', iid=count1, text=f'{row[31]}',
                    values=(f"ViTroxXXL I", f"Scanning Time: {int(row[37]) + handling}", ""))

    tree.bind("<<TreeviewSelect>>", getSelectedRow)

    #tree.pack(side=tk.BOTTOM, fill=tk.X)
    tree.grid(row=5, column=0, columnspan = 6, rowspan = 2, pady=2)

    count += 1
    count1 += 1
    count2 += 1
objDB.closeDB()

root.mainloop()