import _tkinter
from DBConnect import DBConnect
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import pyperclip
import os

tab = []
startXPosition = 170
startYPosition = 85
minMovement = -1
refreshSec = 0.01

def animateImage(root, canvas, xinc, yinc, imgPath = 'board.png'):
    #img = tk.PhotoImage(file='board.png')
    if os.path.isfile(imgPath):
        img = tk.PhotoImage(file=imgPath)
    else:
        img = tk.PhotoImage(file='board.png')



    print(imgPath)

    imageB = canvas.create_image(startXPosition, startYPosition, image=img)

    while True:
        canvas.move(imageB, xinc, 0)
        root.update()
        time.sleep(refreshSec)
        imgPos = canvas.coords(imageB)
        # unpack array to variables
        #al, bl, ar, br = ball_pos
        al, bl = imgPos
        if al < abs(xinc):
            xinc = -xinc
        if bl < abs(yinc):
            yinc = -yinc
        if al == 170/2:
            break

    #root.mainloop()
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
    flagAnimation = False

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
    #print(content[0])
    #print(type(int(content[0])))

    #if int(content[0]) > 0:
        for row in objDB.selectSearchID(content[0]):
            # E1.insert(0, f"{content[0]}")
            tab.append(row[0])
            tab.append(row[2])
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

        pyperclip.copy(E2.get()) #clipboard

        objDB.closeDB()

        LItem.configure(text=f"{row[1]}")
        LItemAmount.configure(text=f"{row[3]}")
        LDateDB.configure(text=f"{row[2]}")
        LQty.configure(text=f"Qty:")
        LDate.configure(text=f"Inserted:")

        if int(len(str(row[17]))) > 4:
            tabControlMain.add(tabMain1, text=" V849 ")
            LV849Prog.configure(text=f"{row[17]}")
            LV849UPH85L.configure(text=f"UPH 85%:")
            LV849UPH95L.configure(text=f"UPH 95%:")
            LV849BaanL.configure(text=f"BaaN:")
            LV849LCL.configure(text=f"LC:")
            LV849EPIL.configure(text=f"EPI:")
            LV849CommentL.configure(text=f"Comment:")
            LV849ScanTime.configure(text=f"Scan Time: {int(row[7])+int(row[8])+int(row[9])+int(row[10])}"
                                         f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s.")
            LV849UPH85.configure(text=f"{row[4]} ({round(60/int(row[4]), 4)}), "
                                      f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                                      f"Board: {round((3600/int(row[4])), 4)}s."
                                 )
            LV849UPH95.configure(text=f"{row[6]} ({round(60/int(row[6]), 4)}), "
                                      f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                                      f"Board: {round((3600/int(row[6])), 4)}s."
                                 )
            if str(row[11]) == 'YES':
                LV849Baan.configure(text=f"{row[11]}", fg="#AAAAAA")
            else:
                LV849Baan.configure(text=f"{row[11]}", fg="#D44339")
            if str(row[18]) == 'YES':
                LV849LC.configure(text=f"{row[18]}", fg="#AAAAAA")
            else:
                LV849LC.configure(text=f"{row[18]}", fg="#D44339")
            if str(row[19]) == 'YES':
                LV849EPI.configure(text=f"{row[19]}", fg="#AAAAAA")
            else:
                LV849EPI.configure(text=f"{row[19]}", fg="#D44339")

            LV849Comment.configure(text=f"{row[20]}")


            canvasFrame1 = Label(tabMain1)
            canvasFrame1.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas1 = tk.Canvas(canvasFrame1, width=170, height=170)
            canvas1.configure(bg="#444444")
            canvas1.pack(expand=False)
            if flagAnimation == False:
                tabControlMain.select(tabMain1)
                #animateImage(root, canvas1, minMovement, minMovement, 'images/V849/' + row[17] + '.png')
                try:
                    animateImage(root, canvas1, minMovement, minMovement, 'X:/images/V849/' + row[17] + '.png')
                except _tkinter.TclError:
                    pass

                flagAnimation = True

            #imgBoard1 = 'images/V849/'+row[17]+'.png'
            imgBoard1 = 'X:/images/V849/'+row[17]+'.png'
            if os.path.isfile(imgBoard1):
                img1 = tk.PhotoImage(file=imgBoard1)
            else:
                img1 = tk.PhotoImage(file='board.png')
            canvas1.create_image(85, 85, image=img1)

        else:
            tabControlMain.hide(tabMain1)

        if int(len(str(row[22]))) > 4:
            tabControlMain.add(tabMain2, text=" V817 ")
            LV817Prog.configure(text=f"{row[22]}")
            LV817UPH85L.configure(text=f"UPH 85%:")
            LV817UPH95L.configure(text=f"UPH 95%:")
            LV817BaanL.configure(text=f"BaaN:")
            LV817LCL.configure(text=f"LC:")
            LV817EPIL.configure(text=f"EPI:")
            LV817CommentL.configure(text=f"Comment:")
            LV817ScanTime.configure(text=f"Scan Time: {int(row[7])+int(row[8])+int(row[9])+int(row[10])}"
                                         f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s.")
            LV817UPH85.configure(text=f"{row[4]} ({round(60/int(row[4]), 4)}), "
                                          f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                                          f"Board: {round((3600/int(row[4])), 4)}s."
                                     )
            LV817UPH95.configure(text=f"{row[6]} ({round(60/int(row[6]), 4)}), "
                                          f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                                          f"Board: {round((3600/int(row[6])), 4)}s."
                                     )
            if str(row[11]) == 'YES':
                LV817Baan.configure(text=f"{row[11]}", fg="#AAAAAA")
            else:
                LV817Baan.configure(text=f"{row[11]}", fg="#D44339")
            if str(row[23]) == 'YES':
                LV817LC.configure(text=f"{row[23]}", fg="#AAAAAA")
            else:
                LV817LC.configure(text=f"{row[23]}", fg="#D44339")
            if str(row[24]) == 'YES':
                LV817EPI.configure(text=f"{row[24]}", fg="#AAAAAA")
            else:
                LV817EPI.configure(text=f"{row[24]}", fg="#D44339")

            LV817Comment.configure(text=f"{row[25]}")

            canvasFrame2 = Label(tabMain2)
            canvasFrame2.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas2 = tk.Canvas(canvasFrame2, width=170, height=170)
            canvas2.configure(bg="#444444")
            canvas2.pack(expand=False)
            if flagAnimation == False:
                tabControlMain.select(tabMain2)
                #animateImage(root, canvas2, minMovement, minMovement, 'images/V817/' + row[22] + '.png')
                try:
                    animateImage(root, canvas2, minMovement, minMovement, 'X:/images/V817/' + row[22] + '.png')
                except _tkinter.TclError:
                    pass
                flagAnimation = True
            #imgBoard2 = 'images/V817/' + row[22] + '.png'
            imgBoard2 = 'X:/images/V817/' + row[22] + '.png'
            if os.path.isfile(imgBoard2):
                img2 = tk.PhotoImage(file=imgBoard2)
            else:
                img2 = tk.PhotoImage(file='board.png')
            canvas2.create_image(85, 85, image=img2)

        else:
            tabControlMain.hide(tabMain2)

        if len(str(row[27])) > 4:
            tabControlMain.add(tabMain3, text=" V810-3163 ")
            LV8103163Prog.configure(text=f"{row[27]}")
            LV8103163UPH85L.configure(text=f"UPH 85%:")
            LV8103163UPH95L.configure(text=f"UPH 95%:")
            LV8103163BaanL.configure(text=f"BaaN:")
            LV8103163LCL.configure(text=f"LC:")
            LV8103163EPIL.configure(text=f"EPI:")
            LV8103163CommentL.configure(text=f"Comment:")
            LV8103163ScanTime.configure(text=f"Scan Time: {int(row[15])} + 15 in/out = {int(row[15]+15)}s.")
            LV8103163UPH85.configure(text=f"{row[12]} ({round(60/int(row[12]), 4)}), "
                                              f"Panel: {round((3600/int(row[12]) * int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[12])), 4)}s."
                                         )
            LV8103163UPH95.configure(text=f"{row[14]} ({round(60/int(row[14]), 4)}), "
                                              f"Panel: {round((3600/int(row[14])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[14])), 4)}s."
                                         )
            if str(row[16]) == 'YES':
                LV8103163Baan.configure(text=f"{row[16]}", fg="#AAAAAA")
            else:
                LV8103163Baan.configure(text=f"{row[16]}", fg="#D44339")
            if str(row[28]) == 'YES':
                LV8103163LC.configure(text=f"{row[28]}", fg="#AAAAAA")
            else:
                LV8103163LC.configure(text=f"{row[28]}", fg="#D44339")
            if str(row[29]) == 'YES':
                LV8103163EPI.configure(text=f"{row[29]}", fg="#AAAAAA")
            else:
                LV8103163EPI.configure(text=f"{row[29]}", fg="#D44339")

            LV8103483S2EXComment.configure(text=f"{row[30]}")

            canvasFrame3 = Label(tabMain3)
            canvasFrame3.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas3 = tk.Canvas(canvasFrame3, width=170, height=170)
            canvas3.configure(bg="#444444")
            canvas3.pack(expand=False)

            if flagAnimation == False:
                tabControlMain.select(tabMain3)
                #animateImage(root, canvas3, minMovement, minMovement, 'images/V810-3163/' + row[27] + '.png')
                try:
                    animateImage(root, canvas3, minMovement, minMovement, 'X:/images/V810-3163/' + row[27] + '.png')
                except _tkinter.TclError:
                    pass
                flagAnimation = True
            #imgBoard3 = 'images/V810-3163/' + row[27] + '.png'
            imgBoard3 = 'X:/images/V810-3163/' + row[27] + '.png'
            if os.path.isfile(imgBoard3):
                img3 = tk.PhotoImage(file=imgBoard3)
            else:
                img3 = tk.PhotoImage(file='board.png')
            canvas3.create_image(85, 85, image=img3)

        else:
            tabControlMain.hide(tabMain3)

        if row[45] != None and int(row[41]) != 0:
            tabControlMain.add(tabMain4, text=" V810-3483S2EX ")
            LV8103483S2EXProg.configure(text=f"{row[45]}")
            LV8103483S2EXUPH85L.configure(text=f"UPH 85%:")
            LV8103483S2EXUPH95L.configure(text=f"UPH 95%:")
            LV8103483S2EXBaanL.configure(text=f"BaaN:")
            LV8103483S2EXLCL.configure(text=f"LC:")
            LV8103483S2EXEPIL.configure(text=f"EPI:")
            LV8103483S2EXCommentL.configure(text=f"Comment:")
            LV8103483S2EXScanTime.configure(text=f"Scan Time: {int(row[43])} + 15 in/out = {int(row[43]+15)}s.")
            LV8103483S2EXUPH85.configure(text=f"{row[40]} ({round(60/int(row[40]), 4)}), "
                                              f"Panel: {round((3600/int(row[40])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[40])), 4)}s."
                                         )
            LV8103483S2EXUPH95.configure(text=f"{row[42]} ({round(60/int(row[42]), 4)}), "
                                              f"Panel: {round((3600/int(row[42])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[42])), 4)}s."
                                         )
            if str(row[44]) == 'YES':
                LV8103483S2EXBaan.configure(text=f"{row[44]}", fg="#AAAAAA")
            else:
                LV8103483S2EXBaan.configure(text=f"{row[44]}", fg="#D44339")
            if str(row[46]) == 'YES':
                LV8103483S2EXLC.configure(text=f"{row[46]}", fg="#AAAAAA")
            else:
                LV8103483S2EXLC.configure(text=f"{row[46]}", fg="#D44339")
            if str(row[47]) == 'YES':
                LV8103483S2EXEPI.configure(text=f"{row[47]}", fg="#AAAAAA")
            else:
                LV8103483S2EXEPI.configure(text=f"{row[47]}", fg="#D44339")

            LV8103483S2EXComment.configure(text=f"{row[48]}")

            canvasFrame4 = Label(tabMain4)
            canvasFrame4.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas4 = tk.Canvas(canvasFrame4, width=170, height=170)
            canvas4.configure(bg="#444444")
            canvas4.pack(expand=False)

            if flagAnimation == False:
                tabControlMain.select(tabMain4)
                #animateImage(root, canvas4, minMovement, minMovement, 'images/V810-3483S2EX/' + row[45] + '.png')
                try:
                    animateImage(root, canvas4, minMovement, minMovement, 'X:/images/V810-3483S2EX/' + row[45] + '.png')
                except _tkinter.TclError:
                    pass
                flagAnimation = True
            #imgBoard4 = 'images/V810-3483S2EX/' + row[45] + '.png'
            imgBoard4 = 'X:/images/V810-3483S2EX/' + row[45] + '.png'
            if os.path.isfile(imgBoard4):
                img4 = tk.PhotoImage(file=imgBoard4)
            else:
                img4 = tk.PhotoImage(file='board.png')
            canvas4.create_image(85, 85, image=img4)

        else:
            tabControlMain.hide(tabMain4)

        if len(str(row[54])) > 0 and row[54] != None:
            tabControlMain.add(tabMain5, text=" V810-3553S2EX ")
            LV8103553S2EXProg.configure(text=f"{row[54]}")
            LV8103553S2EXUPH85L.configure(text=f"UPH 85%:")
            LV8103553S2EXUPH95L.configure(text=f"UPH 95%:")
            LV8103553S2EXBaanL.configure(text=f"BaaN:")
            LV8103553S2EXLCL.configure(text=f"LC:")
            LV8103553S2EXEPIL.configure(text=f"EPI:")
            LV8103553S2EXCommentL.configure(text=f"Comment:")
            LV8103553S2EXScanTime.configure(text=f"Scan Time: {int(row[52])} + 15 in/out = {int(row[52]+15)}s.")
            LV8103553S2EXUPH85.configure(text=f"{row[49]} ({round(60/int(row[49]), 4)}), "
                                              f"Panel: {round((3600/int(row[49])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[49])), 4)}s."
                                         )
            LV8103553S2EXUPH95.configure(text=f"{row[51]} ({round(60/int(row[51]), 4)}), "
                                              f"Panel: {round((3600/int(row[51])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[51])), 4)}s."
                                         )
            if str(row[53]) == 'YES':
                LV8103553S2EXBaan.configure(text=f"{row[53]}", fg="#AAAAAA")
            else:
                LV8103553S2EXBaan.configure(text=f"{row[53]}", fg="#D44339")
            if str(row[55]) == 'YES':
                LV8103553S2EXLC.configure(text=f"{row[55]}", fg="#AAAAAA")
            else:
                LV8103553S2EXLC.configure(text=f"{row[55]}", fg="#D44339")
            if str(row[56]) == 'YES':
                LV8103553S2EXEPI.configure(text=f"{row[56]}", fg="#AAAAAA")
            else:
                LV8103553S2EXEPI.configure(text=f"{row[56]}", fg="#D44339")

            LV8103553S2EXComment.configure(text=f"{row[57]}")

            canvasFrame5 = Label(tabMain5)
            canvasFrame5.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas5 = tk.Canvas(canvasFrame5, width=170, height=170)
            canvas5.configure(bg="#444444")
            canvas5.pack(expand=False)


            if flagAnimation == False:
                tabControlMain.select(tabMain5)
                #animateImage(root, canvas5, minMovement, minMovement, 'images/V810-3553S2EX/' + row[54] + '.png')
                try:
                    animateImage(root, canvas5, minMovement, minMovement, 'X:/images/V810-3553S2EX/' + row[54] + '.png')
                except _tkinter.TclError:
                    pass
                flagAnimation = True
            #imgBoard5 = 'images/V810-3553S2EX/' + row[54] + '.png'
            imgBoard5 = 'X:/images/V810-3553S2EX/' + row[54] + '.png'
            if os.path.isfile(imgBoard5):
                img5 = tk.PhotoImage(file=imgBoard5)
            else:
                img5 = tk.PhotoImage(file='board.png')
            canvas5.create_image(85, 85, image=img5)

        else:
            tabControlMain.hide(tabMain5)

        if row[31] != None and int(row[37] != 0):
            tabControlMain.add(tabMain6, text=" V810-8120S2 ")
            LV8108120S2Prog.configure(text=f"{row[31]}")
            LV8108120S2UPH85L.configure(text=f"UPH 85%:")
            LV8108120S2UPH95L.configure(text=f"UPH 95%:")
            LV8108120S2BaanL.configure(text=f"BaaN:")
            LV8108120S2LCL.configure(text=f"LC:")
            LV8108120S2EPIL.configure(text=f"EPI:")
            LV8108120S2CommentL.configure(text=f"Comment:")
            LV8108120S2ScanTime.configure(text=f"Scan Time: {int(row[37])} + 15 in/out = {int(row[37] + 15)}s.")
            LV8108120S2UPH85.configure(text=f"{row[39]} ({round(60/int(row[39]), 4)}), "
                                              f"Panel: {round((3600/int(row[39])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[39])), 4)}s."
                                         )
            LV8108120S2UPH95.configure(text=f"{row[36]} ({round(60/int(row[36]), 4)}), "
                                              f"Panel: {round((3600/int(row[36])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[36])), 4)}s."
                                         )

            if str(row[38]) == 'YES':
                LV8108120S2Baan.configure(text=f"{row[38]}", fg="#AAAAAA")
            else:
                LV8108120S2Baan.configure(text=f"{row[38]}", fg="#D44339")
            if str(row[32]) == 'YES':
                LV8108120S2LC.configure(text=f"{row[32]}", fg="#AAAAAA")
            else:
                LV8108120S2LC.configure(text=f"{row[32]}", fg="#D44339")
            if str(row[33]) == 'YES':
                LV8108120S2EPI.configure(text=f"{row[33]}", fg="#AAAAAA")
            else:
                LV8108120S2EPI.configure(text=f"{row[33]}", fg="#D44339")

            LV8108120S2Comment.configure(text=f"{row[34]}")

            canvasFrame6 = Label(tabMain6)
            canvasFrame6.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas6 = tk.Canvas(canvasFrame6, width=170, height=170)
            canvas6.configure(bg="#444444")
            canvas6.pack(expand=False)

            if flagAnimation == False:
                tabControlMain.select(tabMain6)
                #animateImage(root, canvas6, minMovement, minMovement, 'images/V810-8120S2/' + row[31] + '.png')
                try:
                    animateImage(root, canvas6, minMovement, minMovement, 'X:/images/V810-8120S2/' + row[31] + '.png')
                except _tkinter.TclError:
                    pass
                flagAnimation = True
            #imgBoard6 = 'images/V810-8120S2/' + row[31] + '.png'
            imgBoard6 = 'X:/images/V810-8120S2/' + row[31] + '.png'
            if os.path.isfile(imgBoard6):
                img6 = tk.PhotoImage(file=imgBoard6)
            else:
                img6 = tk.PhotoImage(file='board.png')
            canvas6.create_image(85, 85, image=img6)

        else:
            tabControlMain.hide(tabMain6)

        root.mainloop()
def updateDisplay():
    if int(tab[0]) >= 0:
        objDB = DBConnect()
        objDB.update(tab[0], E2.get(), E3.get(), E4.get(), E5.get(), LCViTroxIV.get(), EPIViTroxIV.get(),
                    BAANViTroxIV.get(), E6.get())
        objDB.closeDB()
        #tree.delete(1)
        #selected_item = tree.selection()[0]
        #tree.item(selected_item, text=E2.get(), values=("foo", "bar")) #<-- in values I have to download data from DB
        refresh()
def insertData():
    objDB = DBConnect()
    objDB.insert(EI2.get(), EI3.get(), EI4.get(), EI5.get(), LCViTroxIVInsert.get(), EPIViTroxIVInsert.get(),
                 BAANViTroxIVInsert.get(), EI6.get())
    objDB.closeDB()

    EI2.delete(0, END)
    EI3.delete(0, END)
    EI4.delete(0, END)
    EI5.delete(0, END)
    EI6.delete(0, END)
    LCViTroxIVInsert.current(0)
    EPIViTroxIVInsert.current(0)
    BAANViTroxIVInsert.current(0)

    refresh()
def search():
    tree.selection_clear()
    tree.selection_remove(tree.focus())
    for record in tree.get_children():
        content = tree.item(record, 'values')
        #if content[1] != ESearch.get():
        if content[1].find(ESearch.get()) >= 0:
            print(content[1].find(ESearch.get()))
        else:
            tree.delete(record)
def refresh():
    tree.selection_clear()
    tree.selection_remove(tree.focus())
    ESearch.delete(0, END)
    for record in tree.get_children():
        tree.delete(record)

    objDB = DBConnect()
    #objDB.closeDB()

#---Create striped row tags---
    tree.tag_configure('DX', background="#222222")
    tree.tag_configure('V', background="#333333")
    tree.tag_configure('one', background="#111111")
    tree.tag_configure('baan', background="#111111", foreground="#EB0E0E")
    tree.tag_configure('baan0', foreground="#EB0E0E")
#---The End Create striped row---

    count = 1
    count1 = 1
    count2 = 0

    for row in objDB.selectAll():
        if count % 2 == 0:
            if (row[11] != 'YES' and row[11] != 'NONE' and row[11] != None and (row[11] == 'NO' or row[11] == 'LACK')) or \
                    (row[16] != 'YES' and row[16] != 'NONE' and row[16] != None and (row[16] == 'NO' or row[16] == 'LACK')) or \
                    (row[38] != 'YES' and row[38] != 'NONE' and row[38] != None and (row[38] == 'NO' or row[38] == 'LACK')) or \
                    (row[44] != 'YES' and row[44] != 'NONE' and row[44] != None and (row[44] == 'NO' or row[44] == 'LACK')) or \
                    (row[53] != 'YES' and row[53] != 'NONE' and row[53] != None and (row[53] == 'NO' or row[53] == 'LACK')):
                folder1 = tree.insert(parent='', index=count, iid=count1, text=f'box',
                                    values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}'), tag=('baan'))
            else:
                folder1 = tree.insert(parent='', index=count, iid=count1, text=f'box',
                                    values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}'), tag=('one'))
        else:
            if (row[11] != 'YES' and row[11] != 'NONE' and row[11] != None and (row[11] == 'NO' or row[11] == 'LACK')) or \
                    (row[16] != 'YES' and row[16] != 'NONE' and row[16] != None and (row[16] == 'NO' or row[16] == 'LACK')) or \
                    (row[38] != 'YES' and row[38] != 'NONE' and row[38] != None and (row[38] == 'NO' or row[38] == 'LACK')) or \
                    (row[44] != 'YES' and row[44] != 'NONE' and row[44] != None and (row[44] == 'NO' or row[44] == 'LACK')) or \
                    (row[53] != 'YES' and row[53] != 'NONE' and row[53] != None and (row[53] == 'NO' or row[53] == 'LACK')):
                folder1 = tree.insert(parent='', index=count, iid=count1, text=f'box',
                                    values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}'), tag=('baan0'))
            else:
                folder1 = tree.insert(parent='', index=count, iid=count1, text=f'box',
                                    values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}'))
        count1 += 1
        if int(len(str(row[17]))) > 4:
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f'5DX I', f"85%: {row[4]}, 95%: {row[6]}", "", f"{row[11]}",
                                f"{row[18]}", f"{row[19]}"), tags=('DX'))
        count1 += 2
        if int(len(str(row[22]))) > 4:
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"5DX II", f"85%: {row[4]}, 95%: {row[6]}", "", f"{row[11]}",
                                f"{row[23]}", f"{row[24]}"), tags=('DX'))
        count1 += 3
        if len(str(row[27])) > 4:
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTroxEx I", f"85%: {row[12]}, 95%: {row[14]}", "", f"{row[16]}",
                                f"{row[28]}", f"{row[29]}"), tags=('V'))
        count1 += 4
        if row[45] != None and int(row[41]) != 0:
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTroxEx II", f"85%: {row[40]}, 95%: {row[42]}", "", f"{row[44]}",
                                f"{row[46]}", f"{row[47]}"), tags=('V'))
        count1 += 4
        if row[54] != None:
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTroxEx III", f"85%: {row[49]}, 95%: {row[51]}", "", f"{row[53]}",
                                f"{row[55]}", f"{row[56]}"), tags=('V'))
        count1 += 5
        if row[31] != None and int(row[37] != 0):
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTroxXXL I", f"85%: {row[39]}, 95%: {row[36]}", "", f"{row[38]}",
                                f"{row[32]}", f"{row[33]}"), tags=('V'))

        tree.bind("<<TreeviewSelect>>", getSelectedRow)

        tree.grid(row=1, column=0, columnspan=3, pady=2)
        count += 1
        count1 += 1
        count2 += 1

    objDB.closeDB()
# ---Scrollbar--------------
    vsb = ttk.Scrollbar(tab1, orient="vertical", command=tree.yview)
    vsb.place(x=535, y=29, height=273)
    tree.configure(yscrollcommand=vsb.set)
# ---The End of Scrollbar---
def getSelectedTab(event):
    print("click")
    if tabMain1:
        print("1")
        canvasFrame1 = Label(tabMain1)
        canvasFrame1.grid(row=0, column=6, rowspan=6, sticky=W)
        canvas1 = tk.Canvas(canvasFrame1, width=170, height=170)
        canvas1.configure(bg="#444444")
        canvas1.pack(expand=False)

        animateImage(root, canvas1, minMovement, minMovement, 'images/V849/board.png')

def doPopupSearch(event):
    try:
        contextSearchMenu.tk_popup(event.x_root, event.y_root)
    finally:
        contextSearchMenu.grab_release()

def doPopupInsert(event):
    try:
        contextInsertMenu.tk_popup(event.x_root, event.y_root)
    finally:
        contextInsertMenu.grab_release()

def doPopupInsertName(event):
    try:
        contextInsertNameMenu.tk_popup(event.x_root, event.y_root)
    finally:
        contextInsertNameMenu.grab_release()

def doPopupUpdate(event):
    try:
        contextUpdateMenu.tk_popup(event.x_root, event.y_root)
    finally:
        contextUpdateMenu.grab_release()

def doPopupUpdateName(event):
    try:
        contextUpdateNameMenu.tk_popup(event.x_root, event.y_root)
    finally:
        contextUpdateNameMenu.grab_release()

def contextCopyESearch():
    pyperclip.copy(ESearch.get())
def contextPasteESearch():
    ESearch.insert(tk.END, pyperclip.paste())

def contextCopyEI2():
    pyperclip.copy(EI2.get())
def contextPasteEI2():
    EI2.insert(tk.END, pyperclip.paste())

def contextCopyEI4():
    pyperclip.copy(EI4.get())
def contextPasteEI4():
    EI4.insert(tk.END, pyperclip.paste())

def contextCopyE2():
    pyperclip.copy(E2.get())
def contextPasteE2():
    E2.insert(tk.END, pyperclip.paste())

def contextCopyE4():
    pyperclip.copy(E4.get())
def contextPasteE4():
    E4.insert(tk.END, pyperclip.paste())

#def delete():
   # Get selected item to Delete
#   selected_item = tree.selection()[0]
#   tree.delete(selected_item)

root = tk.Tk()
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws-660)
y = (hs-650)
windowPosition = f'660x550+{int(x)}+{int(y)}'
root.title('AXI - Manager')
root.geometry(windowPosition)
#root.resizable(0, 0)
root.configure(background='#000000')

#---contex menu - right click menu---
contextSearchMenu = Menu(root, tearoff=0)
contextSearchMenu.add_command(label="Copy", command=contextCopyESearch)
contextSearchMenu.add_command(label="Paste", command=contextPasteESearch)

contextInsertMenu = Menu(root, tearoff=0)
contextInsertMenu.add_command(label="Copy", command=contextCopyEI2)
contextInsertMenu.add_command(label="Paste", command=contextPasteEI2)

contextInsertNameMenu = Menu(root, tearoff=0)
contextInsertNameMenu.add_command(label="Copy", command=contextCopyEI4)
contextInsertNameMenu.add_command(label="Paste", command=contextPasteEI4)

contextUpdateMenu = Menu(root, tearoff=0)
contextUpdateMenu.add_command(label="Copy", command=contextCopyE2)
contextUpdateMenu.add_command(label="Paste", command=contextPasteE2)

contextUpdateNameMenu = Menu(root, tearoff=0)
contextUpdateNameMenu.add_command(label="Copy", command=contextCopyE4)
contextUpdateNameMenu.add_command(label="Paste", command=contextPasteE4)
#---The End contex menu - right click nemu---


#-------------- Main View ----------------------------------------------------------------------------------------------
mainFrameView = ttk.LabelFrame(root, text=" Main View ")
mainFrameView.pack(expand=1, fill="both", padx=10, pady=10)

LItem = Label(mainFrameView, text=f"", bg="#333333", fg="#999999", pady="1")
LItem.config(font=("Arial", 12, 'bold'))
LItem.grid(row=0, column=0, sticky=W)
LItemAmount = Label(mainFrameView, text=f"", bg="#333333", fg="#999999", pady="1")
LItemAmount.config(font=("Arial", 12, 'bold'))
LItemAmount.grid(row=0, column=2, sticky=W)
LQty = Label(mainFrameView, text=f"", bg="#333333", fg="#555555", pady="2")
LQty.config(font=("Arial", 10))
LQty.grid(row=0, column=1, sticky=E)
LDate = Label(mainFrameView, text=f"", bg="#333333", fg="#555555", pady="2")
LDate.config(font=("Arial", 10))
LDate.grid(row=0, column=3, sticky=W)
LDateDB = Label(mainFrameView, text=f"", bg="#333333", fg="#999999", pady="2")
LDateDB.config(font=("Arial", 10))
LDateDB.grid(row=0, column=4, sticky=W)

tabControlMain = ttk.Notebook(mainFrameView)

tabMain1 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain1, text=" V849 ")
#tabControlMain.bind('<Button-1>', getSelectedTab)

LV849Prog = Label(tabMain1, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV849Prog.configure(font=("Arial", 10))
LV849Prog.grid(row=0, column=0, sticky=W)

LV849ScanTime = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849ScanTime.configure(font=("Arial", 10))
LV849ScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV849UPH85L = Label(tabMain1, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV849UPH85L = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849UPH85L.configure(font=("Arial", 10))
LV849UPH85L.grid(row=1, column=0, sticky=E)
LV849UPH85 = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849UPH85.configure(font=("Arial", 10))
LV849UPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV849UPH95L = Label(tabMain1, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV849UPH95L = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849UPH95L.configure(font=("Arial", 10))
LV849UPH95L.grid(row=2, column=0, sticky=E)
LV849UPH95 = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849UPH95.configure(font=("Arial", 10))
LV849UPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV849BaanL = Label(tabMain1, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV849BaanL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849BaanL.configure(font=("Arial", 10))
LV849BaanL.grid(row=3, column=0, sticky=E)
LV849Baan = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849Baan.configure(font=("Arial", 10))
LV849Baan.grid(row=3, column=1, sticky=W)

#LV849LCL = Label(tabMain1, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV849LCL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849LCL.configure(font=("Arial", 10))
LV849LCL.grid(row=3, column=2, sticky=E)
LV849LC = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849LC.configure(font=("Arial", 10))
LV849LC.grid(row=3, column=3, sticky=W)

#LV849EPIL = Label(tabMain1, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV849EPIL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849EPIL.configure(font=("Arial", 10))
LV849EPIL.grid(row=3, column=4, sticky=E)
LV849EPI = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849EPI.configure(font=("Arial", 10))
LV849EPI.grid(row=3, column=5, sticky=W)

#LV849CommentL = Label(tabMain1, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV849CommentL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
LV849CommentL.configure(font=("Arial", 10))
LV849CommentL.grid(row=4, column=0, sticky=E)
LV849Comment = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV849Comment.configure(font=("Arial", 10))
LV849Comment.grid(row=4, column=1, columnspan=5, sticky=W)

tabMain2 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain2, text=" V817 ")

LV817Prog = Label(tabMain2, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV817Prog.configure(font=("Arial", 10))
LV817Prog.grid(row=0, column=0, sticky=W)
LV817ScanTime = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817ScanTime.configure(font=("Arial", 10))
LV817ScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV817UPH85L = Label(tabMain2, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV817UPH85L = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817UPH85L.configure(font=("Arial", 10))
LV817UPH85L.grid(row=1, column=0, sticky=E)
LV817UPH85 = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817UPH85.configure(font=("Arial", 10))
LV817UPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV817UPH95L = Label(tabMain2, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV817UPH95L = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817UPH95L.configure(font=("Arial", 10))
LV817UPH95L.grid(row=2, column=0, sticky=E)
LV817UPH95 = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817UPH95.configure(font=("Arial", 10))
LV817UPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV817BaanL = Label(tabMain2, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV817BaanL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817BaanL.configure(font=("Arial", 10))
LV817BaanL.grid(row=3, column=0, sticky=E)
LV817Baan = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817Baan.configure(font=("Arial", 10))
LV817Baan.grid(row=3, column=1, sticky=W)

#LV817LCL = Label(tabMain2, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV817LCL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817LCL.configure(font=("Arial", 10))
LV817LCL.grid(row=3, column=2, sticky=E)
LV817LC = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817LC.configure(font=("Arial", 10))
LV817LC.grid(row=3, column=3, sticky=W)

#LV817EPIL = Label(tabMain2, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV817EPIL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817EPIL.configure(font=("Arial", 10))
LV817EPIL.grid(row=3, column=4, sticky=E)
LV817EPI = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817EPI.configure(font=("Arial", 10))
LV817EPI.grid(row=3, column=5, sticky=W)

#LV817CommentL = Label(tabMain2, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV817CommentL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
LV817CommentL.configure(font=("Arial", 10))
LV817CommentL.grid(row=4, column=0, sticky=E)
LV817Comment = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV817Comment.configure(font=("Arial", 10))
LV817Comment.grid(row=4, column=1, columnspan=5, sticky=W)

tabMain3 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain3, text=" V810-3163 ")

LV8103163Prog = Label(tabMain3, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV8103163Prog.configure(font=("Arial", 10))
LV8103163Prog.grid(row=0, column=0, sticky=W)

LV8103163ScanTime = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163ScanTime.configure(font=("Arial", 10))
LV8103163ScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV8103163UPH85L = Label(tabMain3, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV8103163UPH85L = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163UPH85L.configure(font=("Arial", 10))
LV8103163UPH85L.grid(row=1, column=0, sticky=E)
LV8103163UPH85 = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163UPH85.configure(font=("Arial", 10))
LV8103163UPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV8103163UPH95L = Label(tabMain3, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV8103163UPH95L = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163UPH95L.configure(font=("Arial", 10))
LV8103163UPH95L.grid(row=2, column=0, sticky=E)
LV8103163UPH95 = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163UPH95.configure(font=("Arial", 10))
LV8103163UPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV8103163BaanL = Label(tabMain3, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV8103163BaanL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163BaanL.configure(font=("Arial", 10))
LV8103163BaanL.grid(row=3, column=0, sticky=E)
LV8103163Baan = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163Baan.configure(font=("Arial", 10))
LV8103163Baan.grid(row=3, column=1, sticky=W)

#LV8103163LCL = Label(tabMain3, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV8103163LCL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163LCL.configure(font=("Arial", 10))
LV8103163LCL.grid(row=3, column=2, sticky=E)
LV8103163LC = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163LC.configure(font=("Arial", 10))
LV8103163LC.grid(row=3, column=3, sticky=W)

#LV8103163EPIL = Label(tabMain3, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV8103163EPIL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163EPIL.configure(font=("Arial", 10))
LV8103163EPIL.grid(row=3, column=4, sticky=E)
LV8103163EPI = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163EPI.configure(font=("Arial", 10))
LV8103163EPI.grid(row=3, column=5, sticky=W)

#LV8103163CommentL = Label(tabMain3, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV8103163CommentL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103163CommentL.configure(font=("Arial", 10))
LV8103163CommentL.grid(row=4, column=0, sticky=E)
LV8103163Comment = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103163Comment.configure(font=("Arial", 10))
LV8103163Comment.grid(row=4, column=1, columnspan=5, sticky=W)

tabMain4 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain4, text=" V810-3483S2EX ")

LV8103483S2EXProg = Label(tabMain4, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV8103483S2EXProg.configure(font=("Arial", 10))
LV8103483S2EXProg.grid(row=0, column=0, sticky=W)

LV8103483S2EXScanTime = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXScanTime.configure(font=("Arial", 10))
LV8103483S2EXScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV8103483S2EXUPH85L = Label(tabMain4, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXUPH85L = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXUPH85L.configure(font=("Arial", 10))
LV8103483S2EXUPH85L.grid(row=1, column=0, sticky=E)
LV8103483S2EXUPH85 = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXUPH85.configure(font=("Arial", 10))
LV8103483S2EXUPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV8103483S2EXUPH95L = Label(tabMain4, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXUPH95L = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXUPH95L.configure(font=("Arial", 10))
LV8103483S2EXUPH95L.grid(row=2, column=0, sticky=E)
LV8103483S2EXUPH95 = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXUPH95.configure(font=("Arial", 10))
LV8103483S2EXUPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV8103483S2EXBaanL = Label(tabMain4, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXBaanL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXBaanL.configure(font=("Arial", 10))
LV8103483S2EXBaanL.grid(row=3, column=0, sticky=E)
LV8103483S2EXBaan = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXBaan.configure(font=("Arial", 10))
LV8103483S2EXBaan.grid(row=3, column=1, sticky=W)

#LV8103483S2EXLCL = Label(tabMain4, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXLCL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXLCL.configure(font=("Arial", 10))
LV8103483S2EXLCL.grid(row=3, column=2, sticky=E)
LV8103483S2EXLC = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXLC.configure(font=("Arial", 10))
LV8103483S2EXLC.grid(row=3, column=3, sticky=W)

#LV8103483S2EXEPIL = Label(tabMain4, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXEPIL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXEPIL.configure(font=("Arial", 10))
LV8103483S2EXEPIL.grid(row=3, column=4, sticky=E)
LV8103483S2EXEPI = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXEPI.configure(font=("Arial", 10))
LV8103483S2EXEPI.grid(row=3, column=5, sticky=W)

#LV8103483S2EXCommentL = Label(tabMain4, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXCommentL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103483S2EXCommentL.configure(font=("Arial", 10))
LV8103483S2EXCommentL.grid(row=4, column=0, sticky=E)
LV8103483S2EXComment = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103483S2EXComment.configure(font=("Arial", 10))
LV8103483S2EXComment.grid(row=4, column=1, columnspan=5, sticky=W)


tabMain5 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain5, text=" V810-3483S2EX ")

LV8103553S2EXProg = Label(tabMain5, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV8103553S2EXProg.configure(font=("Arial", 10))
LV8103553S2EXProg.grid(row=0, column=0, sticky=W)

LV8103553S2EXScanTime = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXScanTime.configure(font=("Arial", 10))
LV8103553S2EXScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV8103553S2EXUPH85L = Label(tabMain5, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXUPH85L = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXUPH85L.configure(font=("Arial", 10))
LV8103553S2EXUPH85L.grid(row=1, column=0, sticky=E)
LV8103553S2EXUPH85 = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXUPH85.configure(font=("Arial", 10))
LV8103553S2EXUPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV8103553S2EXUPH95L = Label(tabMain5, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXUPH95L = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXUPH95L.configure(font=("Arial", 10))
LV8103553S2EXUPH95L.grid(row=2, column=0, sticky=E)
LV8103553S2EXUPH95 = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXUPH95.configure(font=("Arial", 10))
LV8103553S2EXUPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV8103553S2EXBaanL = Label(tabMain5, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXBaanL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXBaanL.configure(font=("Arial", 10))
LV8103553S2EXBaanL.grid(row=3, column=0, sticky=E)
LV8103553S2EXBaan = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXBaan.configure(font=("Arial", 10))
LV8103553S2EXBaan.grid(row=3, column=1, sticky=W)

#LV8103553S2EXLCL = Label(tabMain5, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXLCL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXLCL.configure(font=("Arial", 10))
LV8103553S2EXLCL.grid(row=3, column=2, sticky=E)
LV8103553S2EXLC = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXLC.configure(font=("Arial", 10))
LV8103553S2EXLC.grid(row=3, column=3, sticky=W)

#LV8103553S2EXEPIL = Label(tabMain5, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXEPIL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXEPIL.configure(font=("Arial", 10))
LV8103553S2EXEPIL.grid(row=3, column=4, sticky=E)
LV8103553S2EXEPI = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXEPI.configure(font=("Arial", 10))
LV8103553S2EXEPI.grid(row=3, column=5, sticky=W)

#LV8103553S2EXCommentL = Label(tabMain5, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXCommentL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
LV8103553S2EXCommentL.configure(font=("Arial", 10))
LV8103553S2EXCommentL.grid(row=4, column=0, sticky=E)
LV8103553S2EXComment = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8103553S2EXComment.configure(font=("Arial", 10))
LV8103553S2EXComment.grid(row=4, column=1, columnspan=5, sticky=W)


tabMain6 = ttk.Frame(tabControlMain)
tabControlMain.add(tabMain6, text=" V810-8120S2 ")

LV8108120S2Prog = Label(tabMain6, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
LV8108120S2Prog.configure(font=("Arial", 10))
LV8108120S2Prog.grid(row=0, column=0, sticky=W)

LV8108120S2ScanTime = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2ScanTime.configure(font=("Arial", 10))
LV8108120S2ScanTime.grid(row=0, column=1, columnspan=5, sticky=E)

#LV8108120S2UPH85L = Label(tabMain6, text=f"UPH 85%:", bg="#444444", fg="#666666", pady="1")
LV8108120S2UPH85L = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2UPH85L.configure(font=("Arial", 10))
LV8108120S2UPH85L.grid(row=1, column=0, sticky=E)
LV8108120S2UPH85 = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2UPH85.configure(font=("Arial", 10))
LV8108120S2UPH85.grid(row=1, column=1, columnspan=5, sticky=W)
#LV8108120S2UPH95L = Label(tabMain6, text=f"UPH 95%:", bg="#444444", fg="#666666", pady="1")
LV8108120S2UPH95L = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2UPH95L.configure(font=("Arial", 10))
LV8108120S2UPH95L.grid(row=2, column=0, sticky=E)
LV8108120S2UPH95 = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2UPH95.configure(font=("Arial", 10))
LV8108120S2UPH95.grid(row=2, column=1, columnspan=5, sticky=W)

#LV8108120S2BaanL = Label(tabMain6, text=f"BaaN:", bg="#444444", fg="#666666", pady="1")
LV8108120S2BaanL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2BaanL.configure(font=("Arial", 10))
LV8108120S2BaanL.grid(row=3, column=0, sticky=E)
LV8108120S2Baan = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2Baan.configure(font=("Arial", 10))
LV8108120S2Baan.grid(row=3, column=1, sticky=W)

#LV8108120S2LCL = Label(tabMain6, text=f"LC:", bg="#444444", fg="#666666", pady="1")
LV8108120S2LCL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2LCL.configure(font=("Arial", 10))
LV8108120S2LCL.grid(row=3, column=2, sticky=E)
LV8108120S2LC = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2LC.configure(font=("Arial", 10))
LV8108120S2LC.grid(row=3, column=3, sticky=W)

#LV8108120S2EPIL = Label(tabMain6, text=f"EPI:", bg="#444444", fg="#666666", pady="1")
LV8108120S2EPIL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2EPIL.configure(font=("Arial", 10))
LV8108120S2EPIL.grid(row=3, column=4, sticky=E)
LV8108120S2EPI = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2EPI.configure(font=("Arial", 10))
LV8108120S2EPI.grid(row=3, column=5, sticky=W)

#LV8108120S2CommentL = Label(tabMain6, text=f"Comment:", bg="#444444", fg="#666666", pady="1")
LV8108120S2CommentL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
LV8108120S2CommentL.configure(font=("Arial", 10))
LV8108120S2CommentL.grid(row=4, column=0, sticky=E)
LV8108120S2Comment = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
LV8108120S2Comment.configure(font=("Arial", 10))
LV8108120S2Comment.grid(row=4, column=1, columnspan=5, sticky=W)

tabControlMain.grid(row=1, column=0, columnspan=5, sticky=W)

#tabControlMain.bind('<Button-1>', getSelectedTab)
        #LItemImageBoard = Label(mainFrameView, image = imageBoard)
        #LItemImageBoard.grid(row=0, column=1, sticky=W)
#------------------- The End Main View ----------------------------

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text=" Main ")
tabControl.pack(expand=1, fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text=" New ")
tabControl.pack(expand=1, fill="both", padx=10, pady=10)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text=" Update ")
tabControl.pack(expand=1, fill="both", padx=10, pady=10)

style = ttk.Style()
style.theme_create('style_class',
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

                       'TButton':{
                           'configure':{
                                'background': '#302928',
                                'foreground': '#FFFFFF',
                                'anchor': N,
                                'font': ("Arial", 12, 'bold')
                           }
                       }
                   }
                   )
style.theme_use('style_class')

#---Notebook Style---
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background='#555555', borderwidth=0)
noteStyler.configure("TNotebook.Tab", background='#555555', foreground='#FFFFFF', lightcolor='#FFFFFF', borderwidth=1)
noteStyler.configure("TFrame", background='#444444', foreground='#FFFFFF', borderwidth=1)
style.configure("TCombobox", fieldbackground="#333333", background="#302928", borderwidth=0)
root.option_add("*TCombobox*Listbox*Background", "#302928")
root.option_add("*TCombobox*Listbox*Foreground", "#AAAAAA")

style.configure("Treeview", background="#000000", foreground="#FFFFFF", rowheight=25, filedbackground="#777777")
style.map('Treeview', background=[('selected', '#170D47')])
#---The End Style---
#---UPDATE---

mainFrame = ttk.LabelFrame(tab3, text=" Update Main ")
mainFrame.grid(column=0, row=0, columnspan=10, sticky='W', padx=10, pady=10)

L1 = Label(mainFrame, text="ID:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L1.config(font=("Arial", 10))
L2 = Label(mainFrame, text="Item:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L2.config(font=("Arial", 10))
L3 = Label(mainFrame, text="Qty:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L3.config(font=("Arial", 10))

#---Update ViTrox V810-3553S2EX---

updateFrameVIV = ttk.LabelFrame(tab3, text=" Update ViTrox V810 Ex III ( V810-3553S2EX ) ")
updateFrameVIV.grid(column=0, row=1, columnspan=10, sticky='W', padx=10, pady=10)

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
L9 = Label(updateFrameVIV, text="Comments:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
L9.config(font=("Arial", 10))

L1.grid(row=0, column=0, sticky=W)
L2.grid(row=1, column=0, sticky=W)
L3.grid(row=1, column=2, sticky=W)
L4.grid(row=0, column=0, sticky=W)
L5.grid(row=0, column=2, sticky=W)
L6.grid(row=1, column=0, sticky=W)
L7.grid(row=1, column=2, sticky=W)
L8.grid(row=2, column=0, sticky=W)
L9.grid(row=2, column=2, sticky=W)

E1 = Entry(mainFrame, relief="solid", borderwidth=1, width=10, bg="#302928", fg="#FFFFFF")
E1.config(font=("Arial", 10))
E1.grid(row=0, column=1, pady=1, sticky=W)
E2 = Entry(mainFrame, relief="solid", borderwidth=1, width=35, bg="#302928", fg="#FFFFFF")
E2.config(font=("Arial", 10))
E2.grid(row=1, column=1, pady=1)
E2.bind("<Button-3>", doPopupUpdate)
E3 = Entry(mainFrame, relief="solid", borderwidth=1, width=10, bg="#302928", fg="#FFFFFF")
E3.config(font=("Arial", 10))
E3.grid(row=1, column=5, pady=1)
E4 = Entry(updateFrameVIV, relief="solid", borderwidth=1, width=35, bg="#302928", fg="#FFFFFF")
E4.config(font=("Arial", 10))
E4.grid(row=0, column=1, pady=1)
E4.bind("<Button-3>", doPopupUpdateName)
E5 = Entry(updateFrameVIV, relief="solid", borderwidth=1, bg="#302928", fg="#FFFFFF")
E5.config(font=("Arial", 10))
E5.grid(row=0, column=3, pady=1)
E6 = Entry(updateFrameVIV, relief="solid", borderwidth=1, bg="#302928", fg="#FFFFFF")
E6.config(font=("Arial", 10))
E6.grid(row=2, column=3, pady=1)

LC = tk.StringVar
LCViTroxIV = ttk.Combobox(updateFrameVIV, width=37, textvariable=LC, state='readonly')
LCViTroxIV['values'] = ("NONE","YES","NO","LACK")
LCViTroxIV.grid(row=1, column=1, pady=1, sticky=W)
LCViTroxIV.current(0)
EPI = tk.StringVar
EPIViTroxIV = ttk.Combobox(updateFrameVIV, width=20, textvariable=EPI, state='readonly')
EPIViTroxIV['values'] = ("NONE","YES","NO","LACK")
EPIViTroxIV.grid(row=1, column=3, pady=1, sticky=W)
EPIViTroxIV.current(0)
BAAN = tk.StringVar
BAANViTroxIV = ttk.Combobox(updateFrameVIV, width=37, textvariable=BAAN, state='readonly')
BAANViTroxIV['values'] = ("NONE","YES","NO","LACK")
BAANViTroxIV.grid(row=2, column=1, pady=1, sticky=W)
BAANViTroxIV.current(0)

B1 = ttk.Button(updateFrameVIV, text="Update", width=50, command=updateDisplay, cursor="hand2")
B1.grid(row=3, column=0, columnspan = 4, pady=2)
#---The End of the UPDATE section---





#tabControl = ttk.Notebook(root)
#tab1 = ttk.Frame(tabControl)
#tabControl.add(tab1, text=" Main ")
#tabControl.pack(expand=1, fill="both")
#tab2 = ttk.Frame(tabControl)
#tabControl.add(tab2, text=" New ")
#tabControl.pack(expand=1, fill="both", padx=10, pady=10)
#tab3 = ttk.Frame(tabControl)
#tabControl.add(tab3, text=" Update ")
#tabControl.pack(expand=1, fill="both", padx=10, pady=10)







#---INSERT---
mainFrameInsert = ttk.LabelFrame(tab2, text=" Insert Main ")
mainFrameInsert.grid(column=0, row=2, columnspan=10, sticky='W', padx=10, pady=10)

#tab2 = ttk.Frame(tabControl)




#---INSERT V810-3553S2EX---
insertFrameVIV = ttk.LabelFrame(tab2, text=" Insert ViTrox V810 Ex III ( V810-3553S2EX ) ")
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
LI9 = Label(insertFrameVIV, text="Comments:", width=12, borderwidth=1, relief="solid", bg="#302928", fg="#555555", pady="1")
LI9.config(font=("Arial", 10))

#LI1.grid(row=0, column=0, sticky=W)
LI2.grid(row=0, column=0, sticky=W)
LI3.grid(row=0, column=2, sticky=W)
LI4.grid(row=0, column=0, sticky=W)
LI5.grid(row=0, column=2, sticky=W)
LI6.grid(row=1, column=0, sticky=W)
LI7.grid(row=1, column=2, sticky=W)
LI8.grid(row=2, column=0, sticky=W)
LI9.grid(row=2, column=2, sticky=W)

#EI1 = Entry(mainFrameInsert, relief="solid", borderwidth=0, bg="#302928", fg="#FFFFFF")
#EI1.config(font=("Arial", 10))
#EI1.grid(row=0, column=1, pady=0)
EI2 = Entry(mainFrameInsert, relief="solid", borderwidth=1, width=35, bg="#302928", fg="#FFFFFF")
EI2.config(font=("Arial", 10))
EI2.grid(row=0, column=1, pady=1)
EI2.bind("<Button-3>", doPopupInsert)
EI3 = Entry(mainFrameInsert, relief="solid", borderwidth=1, width=10, bg="#302928", fg="#FFFFFF")
EI3.config(font=("Arial", 10))
EI3.grid(row=0, column=3, pady=1, stick=W)

EI4 = Entry(insertFrameVIV, relief="solid", borderwidth=1, width=35, bg="#302928", fg="#FFFFFF")
EI4.config(font=("Arial", 10))
EI4.grid(row=0, column=1, pady=1)
EI4.bind("<Button-3>", doPopupInsertName)
EI5 = Entry(insertFrameVIV, relief="solid", borderwidth=1, bg="#302928", fg="#FFFFFF")
EI5.config(font=("Arial", 10))
EI5.grid(row=0, column=3, pady=1, sticky=W)
EI6 = Entry(insertFrameVIV, relief="solid", borderwidth=1, bg="#302928", fg="#FFFFFF")
EI6.config(font=("Arial", 10))
EI6.grid(row=2, column=3, pady=1)
#E6 = Entry(root, bd=0)
#E6.grid(row=1, column=5, pady=2)

LCInsert = tk.StringVar
LCViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=37, textvariable=LCInsert, state='readonly')
LCViTroxIVInsert['values'] = ("NONE", "YES", "NO", "LACK")
LCViTroxIVInsert.grid(row=1, column=1, pady=1, sticky=W)
LCViTroxIVInsert.current(0)
EPIInsert = tk.StringVar
EPIViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=20, textvariable=EPIInsert, state='readonly')
EPIViTroxIVInsert['values'] = ("NONE", "YES", "NO", "LACK")
EPIViTroxIVInsert.grid(row=1, column=3, pady=1, sticky=W)
EPIViTroxIVInsert.current(0)
BAANInsert = tk.StringVar
BAANViTroxIVInsert = ttk.Combobox(insertFrameVIV, width=37, textvariable=BAANInsert, state='readonly')
BAANViTroxIVInsert['values'] = ("NONE", "YES", "NO", "LACK")
BAANViTroxIVInsert.grid(row=2, column=1, pady=1, sticky=W)
BAANViTroxIVInsert.current(0)
#---The End INSERT V810-3553S2EX---
BI1 = ttk.Button(insertFrameVIV, text="Insert", width=50, command=insertData, cursor="hand2")
BI1.grid(row=3, column=0, columnspan=4, pady=2)
#---The End INSERT---

#-----------------Search-------------------
ESearch = Entry(tab1, relief="solid", borderwidth=1, width=40, bg="#302928", fg="#FFFFFF")
ESearch.config(font=("Arial", 10))
ESearch.grid(row=0, column=0, pady=1)
ESearch.bind("<Button-3>", doPopupSearch)
BSearch = ttk.Button(tab1, text="Search", width=10, command=search, cursor="hand2")
BSearch.grid(row=0, column=1, pady=1)
BSearchR = ttk.Button(tab1, text="Refresh", width=10, command=refresh, cursor="exchange")
BSearchR.grid(row=0, column=2, pady=1)
#----------------The End Search------------

tree = ttk.Treeview(tab1)

tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
tree.column("#0", width=40, minwidth=40, stretch=tk.NO)
tree.column("one", width=35, minwidth=35, stretch=tk.NO)
tree.column("two", width=190, minwidth=190, stretch=tk.NO)
tree.column("three", width=130, minwidth=130, stretch=tk.NO)
tree.column("Four", width=30, minwidth=30, stretch=tk.NO)
tree.column("Five", width=35, minwidth=30, stretch=tk.NO)
tree.column("Six", width=35, minwidth=30, stretch=tk.NO)
tree.column("Seven", width=35, minwidth=30, stretch=tk.NO)

tree.heading("#0", text="Box", anchor=tk.W)
tree.heading("one", text="ID", anchor=tk.W)
tree.heading("two", text="Item", anchor=tk.W)
tree.heading("three", text="Date / Time", anchor=tk.W)
tree.heading("Four", text="Qty", anchor=tk.W)
tree.heading("Five", text="BaaN", anchor=tk.W)
tree.heading("Six", text="LC", anchor=tk.W)
tree.heading("Seven", text="EPI", anchor=tk.W)

refresh()

root.mainloop()