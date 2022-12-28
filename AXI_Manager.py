import tkinter
import tkinter as tk
from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage
import time
import os

import pyperclip # clipboard Win / Linux: sudo apt-get install xclip
from PIL import Image

from Config import Config
from Styles import Styles
from DBConnect import DBConnect
from Tip import Tip
from ContextualMenu import ContextualMenu
from CheckboxMenu import CheckboxMenu
from NewItem import NewItem
from FormValidation import FormValidation
from AutomaticUpdates import AutomaticUpdates


#startXPosition: int = 170
#startYPosition: int = 85
min_movement: int = -1
#refreshSec: float = 0.01


def animate_image(root: tkinter.Tk, canvas: tkinter.Canvas, xinc: int, yinc: int, imgPath: str = 'board.png') -> None:
    """
        The function moves the picture from the right to the left side.

        :param root: Given object from tkinter.Tk
        :type root: tkinter.Tk
        :param canvas: Given object from tkinter.Canvas
        :type canvas: tkinter.Canvas

        :param xint: Given value of axis x
        :type xinc: int

        :param int: Given value of axis y
        :type yinc: int

        :param imgPath: Given path to .png file
        :type imgPath: str

        :return: animate the picture
        :rtype: None
    """
    startXPosition: int = 170
    startYPosition: int = 85
    refreshSec: float = 0.01
    if os.path.isfile(imgPath):
        img = tk.PhotoImage(file=imgPath)
    else:
        img = tk.PhotoImage(file='img/lackOfPicture/board.png')

    #print("f: animate_image - "+imgPath)

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
        if al == int(startXPosition)/2:
            break

    #root.mainloop()


def resizeImage(path: str) -> None:
    """
    The function resizes an image

    :param path: Given path to file
    :type path: str
    :return: New size of file
    :rtype: None
    """

    basewidth: int = 120
    if os.path.isfile(path):
        if path.endswith('.jpg'):
            convertJpgtoPng = Image.open(r''+path)
            wpercent = (basewidth / float(convertJpgtoPng.size[0]))
            hsize = int((float(convertJpgtoPng.size[1]) * float(wpercent)))
            convertJpgtoPng = convertJpgtoPng.resize((basewidth, hsize), Image.Resampling.NEAREST)
            pathPNG = path.replace(".jpg", ".png")
            convertJpgtoPng.save(r''+pathPNG)

        elif path.endswith('.png'):
            print("f: ewsizeImage - .png")
#print(resizeImage.__doc__)


def switch(var: str) -> int:
    """
    Switch function is a multiway branch statement that provides a way to organize the flow of execution to
    parts of code based on the value of the expression.

    :param var: Given string NONE, YES, NO and LACK
    :type var: str
    :return: Given number from 0 to 3
    :rtype: type int
    """

    match var:
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
#print(switch.__doc__)


def insertButton() -> None:
    """
    The function is responsible for verifying data and inserting it into the database after the button has been pressed.

    :return: invoking the class FormValidation and DBConnect
    :rtype: None
    """

    objFormValidatorItem = FormValidation()
    objFormValidatorItem.validatorItem(objNewItemEx.EI2.get(), objNewItemEx.EI3.get())
    objFormValidatorItem.cleanUpItem(objNewItemEx.EI2, objNewItemEx.EI3)

    objFormValidatorV8103553S2EX = FormValidation()
    objFormValidatorV8103553S2EX.validator(objCheckboxMenuEx0.EI_0.get(), objCheckboxMenuEx0.EI_1.get(),
                                            objCheckboxMenuEx0.CI_2.get(), objCheckboxMenuEx0.CI_3.get(),
                                            objCheckboxMenuEx0.CI_4.get(), objCheckboxMenuEx0.EI_5.get(),
                                            objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount)
    objFormValidatorV8103553S2EX.cleanUp(objCheckboxMenuEx0.EI_0, objCheckboxMenuEx0.EI_1,
                                            objCheckboxMenuEx0.CI_2, objCheckboxMenuEx0.CI_3,
                                            objCheckboxMenuEx0.CI_4, objCheckboxMenuEx0.EI_5)
    objCheckboxMenuEx0.insertFrame.grid_forget()

    objDBConnectV8103553S2EX = DBConnect()
    objDBConnectV8103553S2EX.insert("V810-3553S2EX", objFormValidatorItem.flagInit, objFormValidatorItem.item,
                                    objFormValidatorItem.itemAmount,
                                    objFormValidatorV8103553S2EX.prog, objFormValidatorV8103553S2EX.test,
                                    objFormValidatorV8103553S2EX.linecapa, objFormValidatorV8103553S2EX.epi,
                                    objFormValidatorV8103553S2EX.baan1, objFormValidatorV8103553S2EX.comments,
                                    objFormValidatorV8103553S2EX.uph85, objFormValidatorV8103553S2EX.uph95,
                                    objFormValidatorV8103553S2EX.uph95Time,
                                    objFormValidatorV8103553S2EX.flagValidator)
    objDBConnectV8103553S2EX.closeDB()

    objFormValidatorV8103483S2EX = FormValidation()
    objFormValidatorV8103483S2EX.validator(objCheckboxMenuEx1.EI_0.get(), objCheckboxMenuEx1.EI_1.get(),
                                            objCheckboxMenuEx1.CI_2.get(), objCheckboxMenuEx1.CI_3.get(),
                                            objCheckboxMenuEx1.CI_4.get(), objCheckboxMenuEx1.EI_5.get(),
                                            objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount)
    objFormValidatorV8103483S2EX.cleanUp(objCheckboxMenuEx1.EI_0, objCheckboxMenuEx1.EI_1,
                                            objCheckboxMenuEx1.CI_2, objCheckboxMenuEx1.CI_3,
                                            objCheckboxMenuEx1.CI_4, objCheckboxMenuEx1.EI_5)
    objCheckboxMenuEx1.insertFrame.grid_forget()

    objDBConnectV8103483S2EX = DBConnect()
    objDBConnectV8103483S2EX.insert("V810-3483S2EX", objFormValidatorItem.flagInit, objFormValidatorItem.item,
                                    objFormValidatorItem.itemAmount,
                                    objFormValidatorV8103483S2EX.prog, objFormValidatorV8103483S2EX.test,
                                    objFormValidatorV8103483S2EX.linecapa, objFormValidatorV8103483S2EX.epi,
                                    objFormValidatorV8103483S2EX.baan1, objFormValidatorV8103483S2EX.comments,
                                    objFormValidatorV8103483S2EX.uph85, objFormValidatorV8103483S2EX.uph95,
                                    objFormValidatorV8103483S2EX.uph95Time,
                                    objFormValidatorV8103483S2EX.flagValidator)
    objDBConnectV8103483S2EX.closeDB()

    objFormValidatorV8103163 = FormValidation()
    objFormValidatorV8103163.validator(objCheckboxMenuEx2.EI_0.get(), objCheckboxMenuEx2.EI_1.get(),
                                        objCheckboxMenuEx2.CI_2.get(), objCheckboxMenuEx2.CI_3.get(),
                                        objCheckboxMenuEx2.CI_4.get(), objCheckboxMenuEx2.EI_5.get(),
                                        objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount)
    objFormValidatorV8103163.cleanUp(objCheckboxMenuEx2.EI_0, objCheckboxMenuEx2.EI_1,
                                    objCheckboxMenuEx2.CI_2, objCheckboxMenuEx2.CI_3,
                                    objCheckboxMenuEx2.CI_4, objCheckboxMenuEx2.EI_5)
    objCheckboxMenuEx2.insertFrame.grid_forget()

    objDBConnectV8103163 = DBConnect()
    objDBConnectV8103163.insert("V810-3163", objFormValidatorItem.flagInit, objFormValidatorItem.item,
                                objFormValidatorItem.itemAmount,
                                objFormValidatorV8103163.prog, objFormValidatorV8103163.test,
                                objFormValidatorV8103163.linecapa, objFormValidatorV8103163.epi,
                                objFormValidatorV8103163.baan1, objFormValidatorV8103163.comments,
                                objFormValidatorV8103163.uph85, objFormValidatorV8103163.uph95,
                                objFormValidatorV8103163.uph95Time, objFormValidatorV8103163.flagValidator)
    objDBConnectV8103163.closeDB()

    objFormValidatorV8108120S2 = FormValidation()
    objFormValidatorV8108120S2.validator(objCheckboxMenuXXL0.EI_0.get(), objCheckboxMenuXXL0.EI_1.get(),
                                        objCheckboxMenuXXL0.CI_2.get(), objCheckboxMenuXXL0.CI_3.get(),
                                        objCheckboxMenuXXL0.CI_4.get(), objCheckboxMenuXXL0.EI_5.get(),
                                        objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount)
    objFormValidatorV8108120S2.cleanUp(objCheckboxMenuXXL0.EI_0, objCheckboxMenuXXL0.EI_1,
                                        objCheckboxMenuXXL0.CI_2, objCheckboxMenuXXL0.CI_3,
                                        objCheckboxMenuXXL0.CI_4, objCheckboxMenuXXL0.EI_5)
    objCheckboxMenuXXL0.insertFrame.grid_forget()

    objDBConnectV8108120S2 = DBConnect()
    objDBConnectV8108120S2.insert("V810-8120S2", objFormValidatorItem.flagInit, objFormValidatorItem.item,
                                    objFormValidatorItem.itemAmount,
                                    objFormValidatorV8108120S2.prog, objFormValidatorV8108120S2.test,
                                    objFormValidatorV8108120S2.linecapa, objFormValidatorV8108120S2.epi,
                                    objFormValidatorV8108120S2.baan1, objFormValidatorV8108120S2.comments,
                                    objFormValidatorV8108120S2.uph85, objFormValidatorV8108120S2.uph95,
                                    objFormValidatorV8108120S2.uph95Time,
                                    objFormValidatorV8108120S2.flagValidator)
    objDBConnectV8108120S2.closeDB()

    objFormValidatorV849 = FormValidation()
    objFormValidatorV849.validator(objCheckboxMenu5DX0.EI_0.get(), objCheckboxMenu5DX0.EI_1.get(),
                                    objCheckboxMenu5DX0.CI_2.get(), objCheckboxMenu5DX0.CI_3.get(),
                                    objCheckboxMenu5DX0.CI_4.get(), objCheckboxMenu5DX0.EI_5.get(),
                                    objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount,
                                    objCheckboxMenu5DX0.EI_6.get(), objCheckboxMenu5DX0.EI_7.get(),
                                    objCheckboxMenu5DX0.EI_8.get())
    objFormValidatorV849.cleanUp(objCheckboxMenu5DX0.EI_0, objCheckboxMenu5DX0.EI_1,
                                    objCheckboxMenu5DX0.CI_2, objCheckboxMenu5DX0.CI_3,
                                    objCheckboxMenu5DX0.CI_4, objCheckboxMenu5DX0.EI_5,
                                    objCheckboxMenu5DX0.EI_6, objCheckboxMenu5DX0.EI_7,
                                    objCheckboxMenu5DX0.EI_8)
    objCheckboxMenu5DX0.insertFrame.grid_forget()

    objFormValidatorV817 = FormValidation()
    objFormValidatorV817.validator(objCheckboxMenu5DX1.EI_0.get(), objCheckboxMenu5DX1.EI_1.get(),
                                    objCheckboxMenu5DX1.CI_2.get(), objCheckboxMenu5DX1.CI_3.get(),
                                    objCheckboxMenu5DX1.CI_4.get(), objCheckboxMenu5DX1.EI_5.get(),
                                    objFormValidatorItem.flagInit, objFormValidatorItem.itemAmount,
                                    objCheckboxMenu5DX1.EI_6.get(), objCheckboxMenu5DX1.EI_7.get(),
                                    objCheckboxMenu5DX1.EI_8.get())
    objFormValidatorV817.cleanUp(objCheckboxMenu5DX1.EI_0, objCheckboxMenu5DX1.EI_1,
                                    objCheckboxMenu5DX1.CI_2, objCheckboxMenu5DX1.CI_3,
                                    objCheckboxMenu5DX1.CI_4, objCheckboxMenu5DX1.EI_5,
                                    objCheckboxMenu5DX1.EI_6, objCheckboxMenu5DX1.EI_7,
                                    objCheckboxMenu5DX1.EI_8)
    objCheckboxMenu5DX1.insertFrame.grid_forget()

    objDBConnect5DX = DBConnect()
    objDBConnect5DX.insert("V849_V817", objFormValidatorItem.flagInit, objFormValidatorItem.item,
                            objFormValidatorItem.itemAmount,

                            objFormValidatorV849.prog, objFormValidatorV849.test,
                            objFormValidatorV849.linecapa, objFormValidatorV849.epi,
                            objFormValidatorV849.baan1, objFormValidatorV849.comments,
                            objFormValidatorV849.uph85, objFormValidatorV849.uph95,
                            objFormValidatorV849.uph95Time, objFormValidatorV849.flagValidator,
                            objFormValidatorV849.alignTime, objFormValidatorV849.laserTime,
                            objFormValidatorV849.thicknessTime, objFormValidatorV849.totalTime,

                            objFormValidatorV817.flagValidator,
                            objFormValidatorV817.prog, objFormValidatorV817.test,
                            objFormValidatorV817.linecapa, objFormValidatorV817.epi,
                            objFormValidatorV817.baan1, objFormValidatorV817.comments,
                            objFormValidatorV817.uph85, objFormValidatorV817.uph95,
                            objFormValidatorV817.uph95Time,
                            objFormValidatorV817.alignTime, objFormValidatorV817.laserTime,
                            objFormValidatorV817.thicknessTime, objFormValidatorV817.totalTime)
    objDBConnect5DX.closeDB()
    if objDBConnectV8103553S2EX.flagSucceeded or \
            objDBConnectV8103483S2EX.flagSucceeded or \
            objDBConnectV8103163.flagSucceeded or \
            objDBConnectV8108120S2.flagSucceeded or \
            objDBConnect5DX.flagSucceeded:
        obj_tip_new = Tip(root, objNewItemEx.mainFrameInsert)
        obj_tip_new.animate_non_translucent()
        refresh()


def reset() -> None:
    """
    The function cleanup the form

    :return: cleanup part of form
    :rtype: None
    """
    objNewItemEx.cleanUp()

    objCheckboxMenuEx0.cleanUp()
    objCheckboxMenuEx0.insertFrame.grid_forget()

    objCheckboxMenuEx1.cleanUp()
    objCheckboxMenuEx1.insertFrame.grid_forget()

    objCheckboxMenuEx2.cleanUp()
    objCheckboxMenuEx2.insertFrame.grid_forget()

    objCheckboxMenuXXL0.cleanUp()
    objCheckboxMenuXXL0.insertFrame.grid_forget()

    objCheckboxMenu5DX0.cleanUp()
    objCheckboxMenu5DX0.cleanUp5DX()
    objCheckboxMenu5DX0.insertFrame.grid_forget()

    objCheckboxMenu5DX1.cleanUp()
    objCheckboxMenu5DX1.cleanUp5DX()
    objCheckboxMenu5DX1.insertFrame.grid_forget()


def getSelectedRow(event) -> None:
    """
    Capture the row

    :return: show information of one record from DB
    :rtype: None
    """
    flagAnimation = False
    flagClick = False

    reset()
    for nm in tree.selection():
        content = tree.item(nm, 'values')

        #curItem = tree.focus()
        #print(tree.item(curItem))

        print(content[1])

        machines = ('5DX I', '5DX II', 'ViTrox Ex I', 'ViTrox Ex II', 'ViTrox Ex III', 'ViTrox XXL I')
        if content[1] in machines:
            flagClick = True

        objDB = DBConnect()
        for row in objDB.selectSearchID(content[0]):
            pass
        objDB.closeDB()

        pyperclip.copy(row[1])  # clipboard Win / Linux: sudo apt-get install xclip


        objNewItemEx.EI2.insert(0, f"{row[1]}")
        objNewItemEx.EI3.insert(0, f"{row[3]}")

        if row[54] != None and \
                ((row[52] != None and int(row[52]) > 0) or int(row[49])):
            objCheckboxMenuEx0.EI_0.insert(0, f"{row[54]}")
            objCheckboxMenuEx0.EI_1.insert(0, f"{int(row[52])}")
            objCheckboxMenuEx0.CI_2.current(switch(row[55]))
            objCheckboxMenuEx0.CI_3.current(switch(row[56]))
            objCheckboxMenuEx0.CI_4.current(switch(row[53]))
            objCheckboxMenuEx0.EI_5.insert(0, f"{row[57]}")
            objCheckboxMenuEx0.insertFrame.grid(column=0, row=5 + 1, columnspan=10, sticky='W', padx=10, pady=10)

        if row[45] != None and \
                ((row[43] != None and int(row[43]) > 0) or int(row[40])):
            objCheckboxMenuEx1.EI_0.insert(0, f"{row[45]}")
            objCheckboxMenuEx1.EI_1.insert(0, f"{int(row[43])}")
            objCheckboxMenuEx1.CI_2.current(switch(row[46]))
            objCheckboxMenuEx1.CI_3.current(switch(row[47]))
            objCheckboxMenuEx1.CI_4.current(switch(row[44]))
            objCheckboxMenuEx1.EI_5.insert(0, f"{row[48]}")
            objCheckboxMenuEx1.insertFrame.grid(column=0, row=5 + 2, columnspan=10, sticky='W', padx=10, pady=10)

        if row[27] != None and \
                ((row[15] != None and int(row[15]) > 0) or int(row[12])):
            objCheckboxMenuEx2.EI_0.insert(0, f"{row[27]}")
            objCheckboxMenuEx2.EI_1.insert(0, f"{int(row[15])}")
            objCheckboxMenuEx2.CI_2.current(switch(row[28]))
            objCheckboxMenuEx2.CI_3.current(switch(row[29]))
            objCheckboxMenuEx2.CI_4.current(switch(row[16]))
            objCheckboxMenuEx2.EI_5.insert(0, f"{row[30]}")
            objCheckboxMenuEx2.insertFrame.grid(column=0, row=5 + 3, columnspan=10, sticky='W', padx=10, pady=10)

        if row[31] != None and \
                ((row[37] != None and int(row[37]) > 0) or int(row[39])):
            objCheckboxMenuXXL0.EI_0.insert(0, f"{row[31]}")
            objCheckboxMenuXXL0.EI_1.insert(0, f"{int(row[37])}")
            objCheckboxMenuXXL0.CI_2.current(switch(row[32]))
            objCheckboxMenuXXL0.CI_3.current(switch(row[33]))
            objCheckboxMenuXXL0.CI_4.current(switch(row[38]))
            objCheckboxMenuXXL0.EI_5.insert(0, f"{row[34]}")
            objCheckboxMenuXXL0.insertFrame.grid(column=0, row=5 + 5, columnspan=10, sticky='W', padx=10, pady=10)

        if (row[17] != None and row[17] != '') and \
                ((row[5] != None and int(row[5]) > 0) or int(row[4])):
            objCheckboxMenu5DX0.EI_0.insert(0, f"{row[17]}")
            objCheckboxMenu5DX0.EI_1.insert(0, f"{int(row[10])}")
            objCheckboxMenu5DX0.CI_2.current(switch(row[18]))
            objCheckboxMenu5DX0.CI_3.current(switch(row[19]))
            objCheckboxMenu5DX0.CI_4.current(switch(row[11]))
            objCheckboxMenu5DX0.EI_5.insert(0, f"{row[20]}")
            objCheckboxMenu5DX0.EI_6.insert(0, f"{int(row[7])}")
            objCheckboxMenu5DX0.EI_7.insert(0, f"{int(row[8])}")
            objCheckboxMenu5DX0.EI_8.insert(0, f"{int(row[9])}")
            objCheckboxMenu5DX0.insertFrame.grid(column=0, row=5 + 1, columnspan=10, sticky='W', padx=10, pady=10)

        if (row[22] != None and row[22] != '') and \
                ((row[5] != None and int(row[5]) > 0) or int(row[4])):
            objCheckboxMenu5DX1.EI_0.insert(0, f"{row[22]}")
            objCheckboxMenu5DX1.EI_1.insert(0, f"{int(row[10])}")
            objCheckboxMenu5DX1.CI_2.current(switch(row[23]))
            objCheckboxMenu5DX1.CI_3.current(switch(row[24]))
            objCheckboxMenu5DX1.CI_4.current(switch(row[11]))
            objCheckboxMenu5DX1.EI_5.insert(0, f"{row[25]}")
            objCheckboxMenu5DX1.EI_6.insert(0, f"{int(row[7])}")
            objCheckboxMenu5DX1.EI_7.insert(0, f"{int(row[8])}")
            objCheckboxMenu5DX1.EI_8.insert(0, f"{int(row[9])}")
            objCheckboxMenu5DX1.insertFrame.grid(column=0, row=5 + 2, columnspan=10, sticky='W', padx=10, pady=10)

        LItem.configure(text=f"{row[1]}")
        LItemAmount.configure(text=f"{row[3]}")
        LDateDB.configure(text=f"{row[2]}")
        LQty.configure(text=f"Qty:")
        LDate.configure(text=f"Inserted:")

# ---getSelectedRow 5DX V849---
        if int(len(str(row[17]))) > 4:
            tabControlMain.add(tabMain1, text=" V849 ")
            LV849Prog.configure(text=f"{row[17]}")
            LV849ScanTimeL.configure(text=f"Scan Time:")
            LV849UPH85L.configure(text=f"UPH 85%:")
            LV849UPH95L.configure(text=f"UPH 95%:")
            LV849BaanL.configure(text=f"BaaN:")
            LV849LCL.configure(text=f"LC:")
            LV849EPIL.configure(text=f"EPI:")
            LV849CommentL.configure(text=f"Comment:")
            LV849ScanTime.configure(text=f"{int(row[7])+int(row[8])+int(row[9])+int(row[10])}"
                                         f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s.")
            try:
                LV849UPH85.configure(text=f"{row[4]} ({round(60/int(row[4]), 4)}), "
                                        f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                                        f"Board: {round((3600/int(row[4])), 4)}s.")
            except ZeroDivisionError:
                LV849UPH85.configure(text=f"(0), "
                                          f"Panel: 0 s. "
                                          f"Board: 0 s.")
            try:
                LV849UPH95.configure(text=f"{row[6]} ({round(60/int(row[6]), 4)}), "
                                        f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                                        f"Board: {round((3600/int(row[6])), 4)}s.")
            except ZeroDivisionError:
                LV849UPH95.configure(text=f"(0), "
                                          f"Panel: 0 s. "
                                          f"Board: 0 s.")
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

#---getSelectedRow 5DX V849---
            canvasFrame1 = Label(tabMain1)
            canvasFrame1.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas1 = tk.Canvas(canvasFrame1, width=170, height=170)
            canvas1.configure(bg="#444444")
            canvas1.pack(expand=False)

            if os.path.isfile(objConfig.pathImg5DX1 + row[17] + '.png') == False:
                resizeImage(objConfig.pathImg5DX1 + row[17] + '.jpg')

            if flagAnimation == False:
                tabControlMain.select(tabMain1)
                if flagClick == False:
                    try:
                        #if os.path.isfile('5DX/images/V849/' + row[17] + '.png'):
                        if os.path.isfile(objConfig.pathImg5DX1 + row[17] + '.png'):
                        #if os.path.isfile('Y:/5DX/images/V849/' + row[17] + '.png'):
                            #animate_image(root, canvas1, min_movement, min_movement, '5DX/images/V849/' + row[17] + '.png')
                            animate_image(root, canvas1, min_movement, min_movement, objConfig.pathImg5DX1 + row[17] + '.png')
                            #animate_image(root, canvas1, minMovement, minMovement, 'Y:/5DX/images/V849/' + row[17] + '.png')
                        else:
                            try:
                                #animate_image(root, canvas1, minMovement, minMovement, '5DX/images/V849/' + row[17] + '.png')
                                animate_image(root, canvas1, min_movement, min_movement, objConfig.pathImg5DX1 + row[17] + '.png')
                                #animate_image(root, canvas1, minMovement, minMovement, 'Y:/5DX/images/V849/' + row[17] + '.png')

                            except FileNotFoundError:
                                pass
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard1 = '5DX/images/V849/'+row[17]+'.png'
            imgBoard1 = objConfig.pathImg5DX1+row[17]+'.png'
            #imgBoard1 = 'Y:/5DX/images/V849/'+row[17]+'.png'
            if os.path.isfile(imgBoard1):
                img1 = tk.PhotoImage(file=imgBoard1)
            else:
                #img1 = tk.PhotoImage(file='board.png')
                img1 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas1.create_image(85, 85, image=img1)

        else:
            tabControlMain.hide(tabMain1)

#---The End getSelectedRow 5DX V849---
#---getSelectedRow 5DX V817---

        if int(len(str(row[22]))) > 4:
            tabControlMain.add(tabMain2, text=" V817 ")
            LV817Prog.configure(text=f"{row[22]}")
            LV817ScanTimeL.configure(text=f"Scan Time:")
            LV817UPH85L.configure(text=f"UPH 85%:")
            LV817UPH95L.configure(text=f"UPH 95%:")
            LV817BaanL.configure(text=f"BaaN:")
            LV817LCL.configure(text=f"LC:")
            LV817EPIL.configure(text=f"EPI:")
            LV817CommentL.configure(text=f"Comment:")
            LV817ScanTime.configure(text=f"{int(row[7])+int(row[8])+int(row[9])+int(row[10])}"
                                         f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s.")
            try:
                LV817UPH85.configure(text=f"{row[4]} ({round(60/int(row[4]), 4)}), "
                                          f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                                          f"Board: {round((3600/int(row[4])), 4)}s.")
            except ZeroDivisionError:
                LV817UPH85.configure(text=f"(0), "
                                          f"Panel: 0 s. "
                                          f"Board: 0 s.")

            try:
                LV817UPH95.configure(text=f"{row[6]} ({round(60/int(row[6]), 4)}), "
                                          f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                                          f"Board: {round((3600/int(row[6])), 4)}s.")
            except ZeroDivisionError:
                LV817UPH95.configure(text=f"(0), "
                                          f"Panel: 0 s. "
                                          f"Board: 0 s.")

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

            #if os.path.isfile('5DX/images/V817/' + row[22] + '.png') == False:
            if os.path.isfile(objConfig.pathImg5DX2 + row[22] + '.png') == False:
            #if os.path.isfile('Y:/5DX/images/V817/' + row[22] + '.png') == False:
                #resizeImage('5DX/images/V817/' + row[22] + '.jpg')
                resizeImage(objConfig.pathImg5DX2 + row[22] + '.jpg')
                #resizeImage('Y:/5DX/images/V817/' + row[22] + '.jpg')

            if flagAnimation == False:
                tabControlMain.select(tabMain2)
                if flagClick == False:
                    try:
                        #if os.path.isfile('5DX/images/V817/' + row[22] + '.png'):
                        if os.path.isfile(objConfig.pathImg5DX2 + row[22] + '.png'):
                        #if os.path.isfile('Y:/5DX/images/V817/' + row[22] + '.png'):
                            #animate_image(root, canvas2, minMovement, minMovement, '5DX/images/V817/' + row[22] + '.png')
                            animate_image(root, canvas2, min_movement, min_movement, objConfig.pathImg5DX2 + row[22] + '.png')
                            #animate_image(root, canvas2, minMovement, minMovement, 'Y:/5DX/images/V817/' + row[22] + '.png')
                        else:
                            try:
                                #animate_image(root, canvas2, minMovement, minMovement, '5DX/images/V817/' + row[22] + '.png')
                                animate_image(root, canvas2, min_movement, min_movement, objConfig.pathImg5DX2 + row[22] + '.png')
                                #animate_image(root, canvas2, minMovement, minMovement, 'Y:/5DX/images/V817/' + row[22] + '.png')

                            except FileNotFoundError:
                                pass
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard2 = '5DX/images/V817/'+row[22]+'.png'
            imgBoard2 = objConfig.pathImg5DX2+row[22]+'.png'
            #imgBoard2 = 'Y:/5DX/images/V817/'+row[22]+'.png'
            if os.path.isfile(imgBoard2):
                img2 = tk.PhotoImage(file=imgBoard2)
            else:
                #img2 = tk.PhotoImage(file='board.png')
                img2 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas2.create_image(85, 85, image=img2)

        else:
            tabControlMain.hide(tabMain2)
#---The End getSelectedRow 5DX V817---
#---getSelectedRow V810-3163--
        #if len(str(row[27])) > 4:
        if row[27] != None and \
                ((int(row[15]) != 0 or int(row[14]) != 0) or int(row[12])):
            tabControlMain.add(tabMain3, text=" V810-3163 ")
            LV8103163Prog.configure(text=f"{row[27]}")
            LV8103163ScanTimeL.configure(text=f"Scan Time:")
            LV8103163UPH85L.configure(text=f"UPH 85%:")
            LV8103163UPH95L.configure(text=f"UPH 95%:")
            LV8103163BaanL.configure(text=f"BaaN:")
            LV8103163LCL.configure(text=f"LC:")
            LV8103163EPIL.configure(text=f"EPI:")
            LV8103163CommentL.configure(text=f"Comment:")
            LV8103163ScanTime.configure(text=f"{int(row[15])} + 15 in/out = {int(row[15]+15)}s.")
            try:
                LV8103163UPH85.configure(text=f"{row[12]} ({round(60/int(row[12]), 4)}), "
                                              f"Panel: {round((3600/int(row[12]) * int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[12])), 4)}s.")
            except ZeroDivisionError:
                LV8103163UPH85.configure(text=f"(0), "
                                              f"Panel: 0s. "
                                              f"Board: 0s.")
            try:
                LV8103163UPH95.configure(text=f"{row[14]} ({round(60/int(row[14]), 4)}), "
                                              f"Panel: {round((3600/int(row[14])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[14])), 4)}s.")
            except ZeroDivisionError:
                LV8103163UPH95.configure(text=f"(0), "
                                              f"Panel: 0s. "
                                              f"Board: 0s.")
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

            LV8103163Comment.configure(text=f"{row[30]}")

            canvasFrame3 = Label(tabMain3)
            canvasFrame3.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas3 = tk.Canvas(canvasFrame3, width=170, height=170)
            canvas3.configure(bg="#444444")
            canvas3.pack(expand=False)

            if flagAnimation == False:
                tabControlMain.select(tabMain3)
                if flagClick == False:
                    try:
                        #animate_image(root, canvas3, minMovement, minMovement, 'X:/images/V810-3163/' + row[27] + '.png')
                        #animate_image(root, canvas3, minMovement, minMovement, 'images/V810-3163/' + row[27] + '.png')
                        animate_image(root, canvas3, min_movement, min_movement, objConfig.pathImgV8103163 + row[27] + '.png')
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard3 = 'images/V810-3163/' + row[27] + '.png'
            imgBoard3 = objConfig.pathImgV8103163 + row[27] + '.png'
            #imgBoard3 = 'X:/images/V810-3163/' + row[27] + '.png'
            if os.path.isfile(imgBoard3):
                img3 = tk.PhotoImage(file=imgBoard3)
            else:
                #img3 = tk.PhotoImage(file='board.png')
                img3 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas3.create_image(85, 85, image=img3)

        else:
            tabControlMain.hide(tabMain3)

#---The End getSelectedRow V810-3163---

#---getSelectedRow V810-V3483S2EX---
        #if row[45] != None and (int(row[41]) != 0 or int(row[40]) != 0):
        if row[45] != None and \
                ((row[43] != None and int(row[43]) > 0) or int(row[40])):
            tabControlMain.add(tabMain4, text=" V810-3483S2EX ")
            LV8103483S2EXProg.configure(text=f"{row[45]}")
            LV8103483S2EXScanTimeL.configure(text=f"Scan Time:")
            LV8103483S2EXUPH85L.configure(text=f"UPH 85%:")
            LV8103483S2EXUPH95L.configure(text=f"UPH 95%:")
            LV8103483S2EXBaanL.configure(text=f"BaaN:")
            LV8103483S2EXLCL.configure(text=f"LC:")
            LV8103483S2EXEPIL.configure(text=f"EPI:")
            LV8103483S2EXCommentL.configure(text=f"Comment:")
            LV8103483S2EXScanTime.configure(text=f"{int(row[43])} + 15 in/out = {int(row[43]+15)}s.")
            try:
                LV8103483S2EXUPH85.configure(text=f"{row[40]} ({round(60/int(row[40]), 4)}), "
                                              f"Panel: {round((3600/int(row[40])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[40])), 4)}s.")
            except ZeroDivisionError:
                LV8103483S2EXUPH85.configure(text=f"(0), "
                                              f"Panel: 0 s. "
                                              f"Board: 0 s.")

            try:
                LV8103483S2EXUPH95.configure(text=f"{row[42]} ({round(60/int(row[42]), 4)}), "
                                              f"Panel: {round((3600/int(row[42])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[42])), 4)}s.")
            except ZeroDivisionError:
                LV8103483S2EXUPH95.configure(text=f"(0), "
                                                f"Panel: 0 s. "
                                                f"Board: 0 s.")
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
                #animate_image(root, canvas4, minMovement, minMovement, 'images/V810-3483S2EX/' + row[45] + '.png')
                if flagClick == False:
                    try:
                        #animate_image(root, canvas4, minMovement, minMovement, 'images/V810-3483S2EX/' + row[45] + '.png')
                        animate_image(root, canvas4, min_movement, min_movement, objConfig.pathImgV8103483S2EX + row[45] + '.png')
                        #animate_image(root, canvas4, minMovement, minMovement, 'X:/images/V810-3483S2EX/' + row[45] + '.png')
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard4 = 'images/V810-3483S2EX/' + row[45] + '.png'
            imgBoard4 = objConfig.pathImgV8103483S2EX + row[45] + '.png'
            #imgBoard4 = 'X:/images/V810-3483S2EX/' + row[45] + '.png'
            if os.path.isfile(imgBoard4):
                img4 = tk.PhotoImage(file=imgBoard4)
            else:
                #img4 = tk.PhotoImage(file='board.png')
                img4 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas4.create_image(85, 85, image=img4)

        else:
            tabControlMain.hide(tabMain4)
#--- The End getSelectedRow V810-3483S2EX ---

#--- getSelectedRow V810-3553S2EX ---
        #if (len(str(row[54])) > 0 and row[54] != None) and (int(row[50]) != 0 or int(row[49]) != 0):
        if row[54] != None and \
                ((row[52] != None and int(row[52]) > 0) or int(row[49])):
            tabControlMain.add(tabMain5, text=" V810-3553S2EX ")
            LV8103553S2EXProg.configure(text=f"{row[54]}")
            LV8103553S2EXScanTimeL.configure(text=f"Scan Time: ")
            LV8103553S2EXUPH85L.configure(text=f"UPH 85%:")
            LV8103553S2EXUPH95L.configure(text=f"UPH 95%:")
            LV8103553S2EXBaanL.configure(text=f"BaaN:")
            LV8103553S2EXLCL.configure(text=f"LC:")
            LV8103553S2EXEPIL.configure(text=f"EPI:")
            LV8103553S2EXCommentL.configure(text=f"Comment:")
            LV8103553S2EXScanTime.configure(text=f"{int(row[52])} + 15 in/out = {int(row[52]+15)}s.")
            try:
                LV8103553S2EXUPH85.configure(text=f"{row[49]} ({round(60/int(row[49]), 4)}), "
                                              f"Panel: {round((3600/int(row[49])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[49])), 4)}s.")
            except ZeroDivisionError:
                LV8103553S2EXUPH85.configure(text=f"(0), "
                                                  f"Panel: 0 s. "
                                                  f"Board: 0 s.")
            try:
                LV8103553S2EXUPH95.configure(text=f"{row[51]} ({round(60/int(row[51]), 4)}), "
                                              f"Panel: {round((3600/int(row[51])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[51])), 4)}s.")
            except ZeroDivisionError:
                LV8103553S2EXUPH95.configure(text=f"(0), "
                                                  f"Panel: 0 s. "
                                                  f"Board: 0 s.")

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
                #animate_image(root, canvas5, minMovement, minMovement, 'images/V810-3553S2EX/' + row[54] + '.png')
                if flagClick == False:
                    try:
                        #animate_image(root, canvas5, minMovement, minMovement, 'images/V810-3553S2EX/' + row[54] + '.png')
                        animate_image(root, canvas5, min_movement, min_movement, objConfig.pathImgV8103553S2EX + row[54] + '.png')
                        #animate_image(root, canvas5, minMovement, minMovement, 'X:/images/V810-3553S2EX/' + row[54] + '.png')
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard5 = 'images/V810-3553S2EX/' + row[54] + '.png'
            imgBoard5 = objConfig.pathImgV8103553S2EX + row[54] + '.png'
            #imgBoard5 = 'X:/images/V810-3553S2EX/' + row[54] + '.png'
            if os.path.isfile(imgBoard5):
                img5 = tk.PhotoImage(file=imgBoard5)
            else:
                #img5 = tk.PhotoImage(file='board.png')
                img5 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas5.create_image(85, 85, image=img5)

        else:
            tabControlMain.hide(tabMain5)
#--- The End getSelectedRow V810-3553S2EX ---

#--- getSelectedRow V810-8120S2 ---
        #if row[31] != None and (int(row[37] != 0) or int(row[39]) != 0):
        if row[31] != None and \
                ((row[37] != None and int(row[37]) > 0) or int(row[39])):
            tabControlMain.add(tabMain6, text=" V810-8120S2 ")
            LV8108120S2Prog.configure(text=f"{row[31]}")
            LV8108120S2ScanTimeL.configure(text=f"Scan Time:")
            LV8108120S2UPH85L.configure(text=f"UPH 85%:")
            LV8108120S2UPH95L.configure(text=f"UPH 95%:")
            LV8108120S2BaanL.configure(text=f"BaaN:")
            LV8108120S2LCL.configure(text=f"LC:")
            LV8108120S2EPIL.configure(text=f"EPI:")
            LV8108120S2CommentL.configure(text=f"Comment:")
            LV8108120S2ScanTime.configure(text=f"{int(row[37])} + 15 in/out = {int(row[37] + 15)}s.")
            try:
                LV8108120S2UPH85.configure(text=f"{row[39]} ({round(60/int(row[39]), 4)}), "
                                              f"Panel: {round((3600/int(row[39])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[39])), 4)}s.")
            except ZeroDivisionError:
                LV8108120S2UPH85.configure(text=f"(0), "
                                                f"Panel: 0 s. "
                                                f"Board: 0 s.")
            try:
                LV8108120S2UPH95.configure(text=f"{row[36]} ({round(60/int(row[36]), 4)}), "
                                              f"Panel: {round((3600/int(row[36])*int(row[3])))}s. "
                                              f"Board: {round((3600/int(row[36])), 4)}s.")
            except ZeroDivisionError:
                LV8108120S2UPH95.configure(text=f"(0), "
                                                f"Panel: 0 s. "
                                                f"Board: 0 s.")

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
                #animate_image(root, canvas6, minMovement, minMovement, 'images/V810-8120S2/' + row[31] + '.png')
                if flagClick == False:
                    try:
                        #animate_image(root, canvas6, minMovement, minMovement, 'images/V810-8120S2/' + row[31] + '.png')
                        animate_image(root, canvas6, min_movement, min_movement, objConfig.pathImgV8108120S2 + row[31] + '.png')
                        #animate_image(root, canvas6, minMovement, minMovement, 'X:/images/V810-8120S2/' + row[31] + '.png')
                    #except _tkinter.TclError:
                    except tk.TclError:
                        pass

                flagAnimation = True

            #imgBoard6 = 'images/V810-8120S2/' + row[31] + '.png'
            imgBoard6 = objConfig.pathImgV8108120S2 + row[31] + '.png'
            #imgBoard6 = 'X:/images/V810-8120S2/' + row[31] + '.png'
            if os.path.isfile(imgBoard6):
                img6 = tk.PhotoImage(file=imgBoard6)
            else:
                img6 = tk.PhotoImage(file=objConfig.pathImgDefault)
            canvas6.create_image(85, 85, image=img6)

        else:
            tabControlMain.hide(tabMain6)
#--- The End getSelectedRow V810-8120S2 ---

        if flagClick == True:
            flagClick = False
            if content[1] == '5DX I':
                tabControlMain.select(tabMain1)
            elif content[1] == '5DX II':
                tabControlMain.select(tabMain2)
            elif content[1] == 'ViTrox Ex I':
                tabControlMain.select(tabMain3)
            elif content[1] == 'ViTrox Ex II':
                tabControlMain.select(tabMain4)
            elif content[1] == 'ViTrox Ex III':
                tabControlMain.select(tabMain5)
            elif content[1] == 'ViTrox XXL I':
                tabControlMain.select(tabMain6)

        root.mainloop()


    #refresh()
def search() -> None:
    """
    The function is looking for the recipe by the phrase

    :return: records from DB according to phrase
    :rtype: None
    """
    tree.selection_clear()
    tree.selection_remove(tree.focus())
    for record in tree.get_children():
        content = tree.item(record, 'values')
        #if content[1] != ESearch.get():
        if content[1].find(ESearch.get()) >= 0:
            pass
            #print(content[1].find(ESearch.get()))
        else:
            tree.delete(record)
def refresh() -> None:
    """
    The function returns the table to the default shape. Show all record from DB.

    :return: Show all records in table from DB
    :rtype: None
    """
    tree.selection_clear()
    tree.selection_remove(tree.focus())
    ESearch.delete(0, END)
    for record in tree.get_children():
        tree.delete(record)

    objDB = DBConnect()

#---Create striped row tags---
    tree.tag_configure('DX', background="#222222")
    tree.tag_configure('V', background="#333333")
    tree.tag_configure('one', background="#111111")
    tree.tag_configure('baan', background="#111111", foreground="#EB0E0E")
    tree.tag_configure('baan0', foreground="#EB0E0E")
    #tree.tag_configure('baan0', foreground="#B03045")
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
        #if len(str(row[27])) > 4: # !!!!!!!!!!!!!!!!!!!!!! it is different than other
        #if row[27] != None and (int(row[15]) != 0 or int(row[14]) != 0):
        if row[27] != None and \
                ((int(row[15]) != 0 or int(row[14]) != 0) or int(row[12])):
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTrox Ex I", f"85%: {row[12]}, 95%: {row[14]}", "", f"{row[16]}",
                                f"{row[28]}", f"{row[29]}"), tags=('V'))
        count1 += 4
        #if row[45] != None and (int(row[41]) != 0 or int(row[40]) != 0):
        if row[45] != None and \
                ((row[43] != None and int(row[43]) > 0) or int(row[40])):
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTrox Ex II", f"85%: {row[40]}, 95%: {row[42]}", "", f"{row[44]}",
                                f"{row[46]}", f"{row[47]}"), tags=('V'))
        count1 += 4
        #if row[54] != None and (int(row[50]) != 0 or int(row[49]) != 0):
        if row[54] != None and \
                ((row[52] != None and int(row[52]) > 0) or int(row[49])):
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTrox Ex III", f"85%: {row[49]}, 95%: {row[51]}", "", f"{row[53]}",
                                f"{row[55]}", f"{row[56]}"), tags=('V'))
        count1 += 5
        #if row[31] != None and (int(row[37]) != 0 or int(row[39]) != 0):
        if row[31] != None and \
                ((row[37] != None and int(row[37]) > 0) or int(row[39])):
            tree.insert(folder1, index='end', iid=count1, text=f'',
                        values=(f'{row[0]}', f"ViTrox XXL I", f"85%: {row[39]}, 95%: {row[36]}", "", f"{row[38]}",
                                f"{row[32]}", f"{row[33]}"), tags=('V'))

        tree.bind("<<TreeviewSelect>>", getSelectedRow)

        tree.grid(row=1, column=0, columnspan=3, pady=2)
        count += 1
        count1 += 1
        count2 += 1

    objDB.closeDB()
# ---Scrollbar--------------
    vsb = ttk.Scrollbar(tab1, orient="vertical", command=tree.yview)
    vsb.place(x=objConfig.scrollX, y=objConfig.scrollY, height=objConfig.scrollHeight)
    tree.configure(yscrollcommand=vsb.set)
# ---The End of Scrollbar---


def automaticInsert() -> None:
    """
    The function fulfills the form with data from a selected new recipe.

    :return: Fulfills the entry with data
    :rtype: None
    """
    msgBox = tk.messagebox.askquestion(f"Automatic adding",
                                    "In the \"Add\" tab you have a new record. Do you want to upload this now?")
    if msgBox == 'yes':
        reset()
        tabControl.select(tab2)
        flagSelectedRecored = False
        objAutomaticUpdates = AutomaticUpdates()
        newItem = varNewRecord.get()
        if newItem in objAutomaticUpdates.bildGrid():
            itemName = objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('recipe').replace('_', '/')
            objNewItemEx.EI2.insert(0, f"{itemName}")
            objNewItemEx.EI3.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('boardQty')}")
            if objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('device') == 'V810-3553S2EX':
                objCheckboxMenuEx0.insertFrame.grid(column=0, row=5 + 1, columnspan=10, sticky='W', padx=10, pady=10)
                objCheckboxMenuEx0.EI_0.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('recipe')}")
                objCheckboxMenuEx0.EI_1.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('cycleTime')}")
                flagSelectedRecored = True
            if objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('device') == 'V810-3483S2EX':
                objCheckboxMenuEx1.insertFrame.grid(column=0, row=5 + 2, columnspan=10, sticky='W', padx=10, pady=10)
                objCheckboxMenuEx1.EI_0.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('recipe')}")
                objCheckboxMenuEx1.EI_1.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('cycleTime')}")
                flagSelectedRecored = True
            if objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('device') == 'V810-3163':
                objCheckboxMenuEx2.insertFrame.grid(column=0, row=5 + 3, columnspan=10, sticky='W', padx=10, pady=10)
                objCheckboxMenuEx2.EI_0.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('recipe')}")
                objCheckboxMenuEx2.EI_1.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('cycleTime')}")
                flagSelectedRecored = True
            if objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('device') == 'V810-8120S2':
                objCheckboxMenuXXL0.insertFrame.grid(column=0, row=5 + 5, columnspan=10, sticky='W', padx=10, pady=10)
                objCheckboxMenuXXL0.EI_0.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('recipe')}")
                objCheckboxMenuXXL0.EI_1.insert(0, f"{objAutomaticUpdates.dicRecipe.get(varNewRecord.get()).get('cycleTime')}")
                flagSelectedRecored = True

        if flagSelectedRecored is True:
            objAutomaticUpdates.updateDic(varNewRecord.get())
            addFrame.pack_forget()
            for widget in addFrame.winfo_children():
                widget.destroy()


def tabSelected(event) -> None:
    """
    The function show list of not yet added records to DB.

    :return: Show list of not yet added recipe
    :rtype: None
    """
    objAutomaticUpdates = AutomaticUpdates()

    if event.widget.tab(event.widget.select(), "text") == " --- Add --- ":

        addFrame.pack(expand=1, fill="both", padx=10, pady=10)
        objAutomaticUpdates.bildGrid()

        for record in range(len(objAutomaticUpdates.dicRecipe)):
            radioBox = ttk.Radiobutton(addFrame, text=f"{objAutomaticUpdates.dicRecipe.get(record).get('device')} - "
                                          f"{objAutomaticUpdates.dicRecipe.get(record).get('recipe')} "
                                          f"    [ {objAutomaticUpdates.dicRecipe.get(record).get('boardQty')} ] - "
                                          f"Cycle Time: {objAutomaticUpdates.dicRecipe.get(record).get('cycleTime')} s.",
                               style="AutomaticInsert.TRadiobutton",
                               variable=varNewRecord,
                               value=int(record),
                               command=automaticInsert)
            radioBox.grid(row=int(record), column=0, sticky=W)
        radioBox.invoke()

if __name__ == "__main__":
    root = tk.Tk()
    objConfig = Config()
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws-int(objConfig.screenWidth))
    y = (hs-int(objConfig.screenHeight))
    windowPosition = f'{int(objConfig.screenWidth)}x{int(objConfig.screenHeight)}+{int(x)}+{int(y)}'
    root.title(objConfig.title)
    root.geometry(windowPosition)
    #root.resizable(0, 0)
    #root.iconbitmap(objConfig.ico) # Icon for Win
    photo = PhotoImage(file=objConfig.ico)# Icon for Linux
    root.iconphoto(False, photo)# Incon for Linux

    root.configure(background=objConfig.bgColor)

    #--- Main View ---

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

    LV849Prog = Label(tabMain1, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV849Prog.configure(font=("Arial", 10))
    LV849Prog.grid(row=0, column=0, columnspan=6, sticky=W)

    LV849ScanTimeL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849ScanTimeL.configure(font=("Arial", 10))
    LV849ScanTimeL.grid(row=1, column=0, sticky=E)
    LV849ScanTime = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849ScanTime.configure(font=("Arial", 10))
    LV849ScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV849UPH85L = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849UPH85L.configure(font=("Arial", 10))
    LV849UPH85L.grid(row=2, column=0, sticky=E)
    LV849UPH85 = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849UPH85.configure(font=("Arial", 10))
    LV849UPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV849UPH95L = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849UPH95L.configure(font=("Arial", 10))
    LV849UPH95L.grid(row=3, column=0, sticky=E)
    LV849UPH95 = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849UPH95.configure(font=("Arial", 10))
    LV849UPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV849BaanL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849BaanL.configure(font=("Arial", 10))
    LV849BaanL.grid(row=4, column=0, sticky=E)
    LV849Baan = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849Baan.configure(font=("Arial", 10))
    LV849Baan.grid(row=4, column=1, sticky=W)

    LV849LCL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849LCL.configure(font=("Arial", 10))
    LV849LCL.grid(row=4, column=2, sticky=E)
    LV849LC = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849LC.configure(font=("Arial", 10))
    LV849LC.grid(row=4, column=3, sticky=W)

    LV849EPIL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849EPIL.configure(font=("Arial", 10))
    LV849EPIL.grid(row=4, column=4, sticky=E)
    LV849EPI = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849EPI.configure(font=("Arial", 10))
    LV849EPI.grid(row=4, column=5, sticky=W)

    LV849CommentL = Label(tabMain1, text=f"", bg="#444444", fg="#666666", pady="1")
    LV849CommentL.configure(font=("Arial", 10))
    LV849CommentL.grid(row=5, column=0, sticky=E)
    LV849Comment = Label(tabMain1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV849Comment.configure(font=("Arial", 10, "italic"))
    LV849Comment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabMain2 = ttk.Frame(tabControlMain)
    tabControlMain.add(tabMain2, text=" V817 ")

    LV817Prog = Label(tabMain2, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV817Prog.configure(font=("Arial", 10))
    LV817Prog.grid(row=0, column=0, columnspan=6, sticky=W)

    LV817ScanTimeL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817ScanTimeL.configure(font=("Arial", 10))
    LV817ScanTimeL.grid(row=1, column=0, sticky=E)
    LV817ScanTime = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817ScanTime.configure(font=("Arial", 10))
    LV817ScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV817UPH85L = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817UPH85L.configure(font=("Arial", 10))
    LV817UPH85L.grid(row=2, column=0, sticky=E)
    LV817UPH85 = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817UPH85.configure(font=("Arial", 10))
    LV817UPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV817UPH95L = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817UPH95L.configure(font=("Arial", 10))
    LV817UPH95L.grid(row=3, column=0, sticky=E)
    LV817UPH95 = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817UPH95.configure(font=("Arial", 10))
    LV817UPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV817BaanL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817BaanL.configure(font=("Arial", 10))
    LV817BaanL.grid(row=4, column=0, sticky=E)
    LV817Baan = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817Baan.configure(font=("Arial", 10))
    LV817Baan.grid(row=4, column=1, sticky=W)

    LV817LCL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817LCL.configure(font=("Arial", 10))
    LV817LCL.grid(row=4, column=2, sticky=E)
    LV817LC = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817LC.configure(font=("Arial", 10))
    LV817LC.grid(row=4, column=3, sticky=W)

    LV817EPIL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817EPIL.configure(font=("Arial", 10))
    LV817EPIL.grid(row=4, column=4, sticky=E)
    LV817EPI = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817EPI.configure(font=("Arial", 10))
    LV817EPI.grid(row=4, column=5, sticky=W)

    LV817CommentL = Label(tabMain2, text=f"", bg="#444444", fg="#666666", pady="1")
    LV817CommentL.configure(font=("Arial", 10))
    LV817CommentL.grid(row=5, column=0, sticky=E)
    LV817Comment = Label(tabMain2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV817Comment.configure(font=("Arial", 10, "italic"))
    LV817Comment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabMain3 = ttk.Frame(tabControlMain)
    tabControlMain.add(tabMain3, text=" V810-3163 ")

    LV8103163Prog = Label(tabMain3, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV8103163Prog.configure(font=("Arial", 10))
    LV8103163Prog.grid(row=0, column=0, columnspan=6, sticky=W)

    LV8103163ScanTimeL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163ScanTimeL.configure(font=("Arial", 10))
    LV8103163ScanTimeL.grid(row=1, column=0, sticky=E)
    LV8103163ScanTime = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163ScanTime.configure(font=("Arial", 10))
    LV8103163ScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV8103163UPH85L = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163UPH85L.configure(font=("Arial", 10))
    LV8103163UPH85L.grid(row=2, column=0, sticky=E)
    LV8103163UPH85 = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163UPH85.configure(font=("Arial", 10))
    LV8103163UPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV8103163UPH95L = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163UPH95L.configure(font=("Arial", 10))
    LV8103163UPH95L.grid(row=3, column=0, sticky=E)
    LV8103163UPH95 = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163UPH95.configure(font=("Arial", 10))
    LV8103163UPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV8103163BaanL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163BaanL.configure(font=("Arial", 10))
    LV8103163BaanL.grid(row=4, column=0, sticky=E)
    LV8103163Baan = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163Baan.configure(font=("Arial", 10))
    LV8103163Baan.grid(row=4, column=1, sticky=W)

    LV8103163LCL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163LCL.configure(font=("Arial", 10))
    LV8103163LCL.grid(row=4, column=2, sticky=E)
    LV8103163LC = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163LC.configure(font=("Arial", 10))
    LV8103163LC.grid(row=4, column=3, sticky=W)

    LV8103163EPIL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163EPIL.configure(font=("Arial", 10))
    LV8103163EPIL.grid(row=4, column=4, sticky=E)
    LV8103163EPI = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163EPI.configure(font=("Arial", 10))
    LV8103163EPI.grid(row=4, column=5, sticky=W)

    LV8103163CommentL = Label(tabMain3, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103163CommentL.configure(font=("Arial", 10))
    LV8103163CommentL.grid(row=5, column=0, sticky=E)
    LV8103163Comment = Label(tabMain3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103163Comment.configure(font=("Arial", 10, "italic"))
    LV8103163Comment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabMain4 = ttk.Frame(tabControlMain)
    tabControlMain.add(tabMain4, text=" V810-3483S2EX ")

    LV8103483S2EXProg = Label(tabMain4, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV8103483S2EXProg.configure(font=("Arial", 10))
    LV8103483S2EXProg.grid(row=0, column=0, columnspan=6, sticky=W)

    LV8103483S2EXScanTimeL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXScanTimeL.configure(font=("Arial", 10))
    LV8103483S2EXScanTimeL.grid(row=1, column=0, sticky=E)
    LV8103483S2EXScanTime = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXScanTime.configure(font=("Arial", 10))
    LV8103483S2EXScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV8103483S2EXUPH85L = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXUPH85L.configure(font=("Arial", 10))
    LV8103483S2EXUPH85L.grid(row=2, column=0, sticky=E)
    LV8103483S2EXUPH85 = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXUPH85.configure(font=("Arial", 10))
    LV8103483S2EXUPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV8103483S2EXUPH95L = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXUPH95L.configure(font=("Arial", 10))
    LV8103483S2EXUPH95L.grid(row=3, column=0, sticky=E)
    LV8103483S2EXUPH95 = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXUPH95.configure(font=("Arial", 10))
    LV8103483S2EXUPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV8103483S2EXBaanL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXBaanL.configure(font=("Arial", 10))
    LV8103483S2EXBaanL.grid(row=4, column=0, sticky=E)
    LV8103483S2EXBaan = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXBaan.configure(font=("Arial", 10))
    LV8103483S2EXBaan.grid(row=4, column=1, sticky=W)

    LV8103483S2EXLCL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXLCL.configure(font=("Arial", 10))
    LV8103483S2EXLCL.grid(row=4, column=2, sticky=E)
    LV8103483S2EXLC = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXLC.configure(font=("Arial", 10))
    LV8103483S2EXLC.grid(row=4, column=3, sticky=W)

    LV8103483S2EXEPIL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXEPIL.configure(font=("Arial", 10))
    LV8103483S2EXEPIL.grid(row=4, column=4, sticky=E)
    LV8103483S2EXEPI = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXEPI.configure(font=("Arial", 10))
    LV8103483S2EXEPI.grid(row=4, column=5, sticky=W)

    LV8103483S2EXCommentL = Label(tabMain4, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103483S2EXCommentL.configure(font=("Arial", 10))
    LV8103483S2EXCommentL.grid(row=5, column=0, sticky=E)
    LV8103483S2EXComment = Label(tabMain4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103483S2EXComment.configure(font=("Arial", 10, "italic"))
    LV8103483S2EXComment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabMain5 = ttk.Frame(tabControlMain)
    tabControlMain.add(tabMain5, text=" V810-3483S2EX ")

    LV8103553S2EXProg = Label(tabMain5, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV8103553S2EXProg.configure(font=("Arial", 10))
    LV8103553S2EXProg.grid(row=0, column=0, columnspan=6, sticky=W)

    LV8103553S2EXScanTimeL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXScanTimeL.configure(font=("Arial", 10))
    LV8103553S2EXScanTimeL.grid(row=1, column=0, sticky=E)
    LV8103553S2EXScanTime = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXScanTime.configure(font=("Arial", 10))
    LV8103553S2EXScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV8103553S2EXUPH85L = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXUPH85L.configure(font=("Arial", 10))
    LV8103553S2EXUPH85L.grid(row=2, column=0, sticky=E)
    LV8103553S2EXUPH85 = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXUPH85.configure(font=("Arial", 10))
    LV8103553S2EXUPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV8103553S2EXUPH95L = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXUPH95L.configure(font=("Arial", 10))
    LV8103553S2EXUPH95L.grid(row=3, column=0, sticky=E)
    LV8103553S2EXUPH95 = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXUPH95.configure(font=("Arial", 10))
    LV8103553S2EXUPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV8103553S2EXBaanL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXBaanL.configure(font=("Arial", 10))
    LV8103553S2EXBaanL.grid(row=4, column=0, sticky=E)
    LV8103553S2EXBaan = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXBaan.configure(font=("Arial", 10))
    LV8103553S2EXBaan.grid(row=4, column=1, sticky=W)

    LV8103553S2EXLCL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXLCL.configure(font=("Arial", 10))
    LV8103553S2EXLCL.grid(row=4, column=2, sticky=E)
    LV8103553S2EXLC = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXLC.configure(font=("Arial", 10))
    LV8103553S2EXLC.grid(row=4, column=3, sticky=W)

    LV8103553S2EXEPIL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXEPIL.configure(font=("Arial", 10))
    LV8103553S2EXEPIL.grid(row=4, column=4, sticky=E)
    LV8103553S2EXEPI = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXEPI.configure(font=("Arial", 10))
    LV8103553S2EXEPI.grid(row=4, column=5, sticky=W)

    LV8103553S2EXCommentL = Label(tabMain5, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8103553S2EXCommentL.configure(font=("Arial", 10))
    LV8103553S2EXCommentL.grid(row=5, column=0, sticky=E)
    LV8103553S2EXComment = Label(tabMain5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8103553S2EXComment.configure(font=("Arial", 10, "italic"))
    LV8103553S2EXComment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabMain6 = ttk.Frame(tabControlMain)
    tabControlMain.add(tabMain6, text=" V810-8120S2 ")

    LV8108120S2Prog = Label(tabMain6, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    LV8108120S2Prog.configure(font=("Arial", 10))
    LV8108120S2Prog.grid(row=0, column=0, columnspan=6, sticky=W)

    LV8108120S2ScanTimeL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2ScanTimeL.configure(font=("Arial", 10))
    LV8108120S2ScanTimeL.grid(row=1, column=0, sticky=E)
    LV8108120S2ScanTime = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2ScanTime.configure(font=("Arial", 10))
    LV8108120S2ScanTime.grid(row=1, column=1, columnspan=5, sticky=W)

    LV8108120S2UPH85L = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2UPH85L.configure(font=("Arial", 10))
    LV8108120S2UPH85L.grid(row=2, column=0, sticky=E)
    LV8108120S2UPH85 = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2UPH85.configure(font=("Arial", 10))
    LV8108120S2UPH85.grid(row=2, column=1, columnspan=5, sticky=W)
    LV8108120S2UPH95L = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2UPH95L.configure(font=("Arial", 10))
    LV8108120S2UPH95L.grid(row=3, column=0, sticky=E)
    LV8108120S2UPH95 = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2UPH95.configure(font=("Arial", 10))
    LV8108120S2UPH95.grid(row=3, column=1, columnspan=5, sticky=W)

    LV8108120S2BaanL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2BaanL.configure(font=("Arial", 10))
    LV8108120S2BaanL.grid(row=4, column=0, sticky=E)
    LV8108120S2Baan = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2Baan.configure(font=("Arial", 10))
    LV8108120S2Baan.grid(row=4, column=1, sticky=W)

    LV8108120S2LCL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2LCL.configure(font=("Arial", 10))
    LV8108120S2LCL.grid(row=4, column=2, sticky=E)
    LV8108120S2LC = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2LC.configure(font=("Arial", 10))
    LV8108120S2LC.grid(row=4, column=3, sticky=W)

    LV8108120S2EPIL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2EPIL.configure(font=("Arial", 10))
    LV8108120S2EPIL.grid(row=4, column=4, sticky=E)
    LV8108120S2EPI = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2EPI.configure(font=("Arial", 10))
    LV8108120S2EPI.grid(row=4, column=5, sticky=W)

    LV8108120S2CommentL = Label(tabMain6, text=f"", bg="#444444", fg="#666666", pady="1")
    LV8108120S2CommentL.configure(font=("Arial", 10))
    LV8108120S2CommentL.grid(row=5, column=0, sticky=E)
    LV8108120S2Comment = Label(tabMain6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    LV8108120S2Comment.configure(font=("Arial", 10))
    LV8108120S2Comment.grid(row=5, column=1, columnspan=5, sticky=W)

    tabControlMain.grid(row=1, column=0, columnspan=5, sticky=W)

    #------------------- The End Main View ----------------------------

    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text=" --- Main --- ")
    tabControl.pack(expand=1, fill="both", padx=10, pady=10)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text=" --- New --- ")
    tabControl.pack(expand=1, fill="both", padx=10, pady=10)
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab3, text=" --- Add --- ")
    tabControl.pack(expand=1, fill="both", padx=10, pady=10)

    tabControl.bind("<<NotebookTabChanged>>", tabSelected)

    addFrame = ttk.LabelFrame(tab3, text=" New Items: ")
    #addFrame.pack(expand=1, fill="both", padx=10, pady=10)
    #addFrame.pack_Forget()
    varNewRecord = IntVar()


    objStyles = Styles(root)

    #--- INSERT ---

    objNewItemEx = NewItem(tab2, root)
    objNewItemEx.mainFrameInsert(" Insert Main ")

    objNewItemEx.checkboxTitle(" ViTrox Ex ", 4)
    objCheckboxMenuEx0 = CheckboxMenu(tab2, root, objNewItemEx.checkboxFrame, " Insert ViTrox V810 Ex III ( V810-3553S2EX ) ")
    objCheckboxMenuEx0.checkboxMenu("V810-3553S2EX", 1)

    objCheckboxMenuEx1 = CheckboxMenu(tab2, root, objNewItemEx.checkboxFrame, " Insert ViTrox V810 Ex II ( V810-3483S2EX ) ")
    objCheckboxMenuEx1.checkboxMenu("V810-3483S2EX", 2)

    objCheckboxMenuEx2 = CheckboxMenu(tab2, root, objNewItemEx.checkboxFrame, " Insert ViTrox V810 Ex I ( V810-3163 ) ")
    objCheckboxMenuEx2.checkboxMenu("V810-3163", 3)

    objNewItemXXL = NewItem(tab2, root)
    objNewItemXXL.checkboxTitle(" ViTrox XXL ", 5)

    objCheckboxMenuXXL0 = CheckboxMenu(tab2, root, objNewItemXXL.checkboxFrame, " Insert ViTrox V810 XXL I ( V810-8120S2 ) ")
    objCheckboxMenuXXL0.checkboxMenu("V810-8120S2", 1)

    objNewItem5DX = NewItem(tab2, root)
    objNewItem5DX.checkboxTitle(" 5DX ", 6)

    objCheckboxMenu5DX0 = CheckboxMenu(tab2, root, objNewItem5DX.checkboxFrame, " Insert 5DX I ( V849 ) ")
    objCheckboxMenu5DX0.checkboxMenu("V849", 1)
    objCheckboxMenu5DX0.alignmentTime()

    objCheckboxMenu5DX1 = CheckboxMenu(tab2, root, objNewItem5DX.checkboxFrame, " Insert 5DX II ( V817 ) ")
    objCheckboxMenu5DX1.checkboxMenu("V817", 2)
    objCheckboxMenu5DX1.alignmentTime()

    BI1 = ttk.Button(objNewItemEx.mainFrameInsert, text="Insert", width=35, command=insertButton, cursor="hand2")
    BI1.grid(row=1, column=0, columnspan=2, pady=2)
    BI2 = ttk.Button(objNewItemEx.mainFrameInsert, text="Reset", width=15, command=reset, cursor="hand2")
    BI2.grid(row=1, column=2, columnspan=2, pady=2)
    #--- The End INSERT ---


    #--- Automatic Upadate ---

    #objAutomaticUpdates = AutomaticUpdates()
    #varNewRecord = IntVar()

    #for record in range(len(objAutomaticUpdates.bildGrid())):
    #    radioBox = ttk.Radiobutton(tab3, text=f"{objAutomaticUpdates.bildGrid().get(record).get('device')} - "
    #                                        f"{objAutomaticUpdates.bildGrid().get(record).get('recipe')} "
    #                                        f"    [ {objAutomaticUpdates.bildGrid().get(record).get('boardQty')} ] - "
    #                                        f"Cycle Time: {objAutomaticUpdates.bildGrid().get(record).get('cycleTime')} s.",
    #                                    style="AutomaticInsert.TRadiobutton",
    #                                    variable=varNewRecord,
    #                                    value=int(record),
    #                                    command=automaticInsert)
    #    radioBox.grid(row=int(record), column=0, sticky=W)
    #radioBox.invoke()

    #--- The End of Automatic Update ---

    #--- Search ---
    objCMSearch = ContextualMenu(root)
    #ESearch = Entry(tab1, relief="solid", borderwidth=1, width=40, bg="#212121", fg="#FFFFFF")
    ESearch = Entry(tab1, relief="solid", textvariable=objCMSearch.captureEntry,
                    borderwidth=1, width=40, bg="#212121", fg="#FFFFFF")
    ESearch.config(font=("Arial", 10), highlightbackground="#000000", highlightcolor="#33FFBE")
    ESearch.grid(row=0, column=0, pady=1)
    #ESearch.bind("<Button-3>", doPopupSearch)
    ESearch.bind("<Button-3>", objCMSearch.doPopup)
    objCMSearch.setEntry(ESearch)
    BSearch = ttk.Button(tab1, text="Search", width=10, command=search, cursor="hand2")
    BSearch.grid(row=0, column=1, pady=1)
    BSearchR = ttk.Button(tab1, text="Refresh", width=10, command=refresh, cursor="exchange")
    BSearchR.grid(row=0, column=2, pady=1)
    #--- The End Search ---

    tree = ttk.Treeview(tab1)

    tree["columns"] = ("one", "two", "three", "Four", "Five", "Six", "Seven")
    tree.column("#0", width=40, minwidth=40, stretch=tk.NO)
    tree.column("one", width=35, minwidth=35, stretch=tk.NO)
    tree.column("two", width=250, minwidth=190, stretch=tk.NO)
    tree.column("three", width=140, minwidth=130, stretch=tk.NO)
    tree.column("Four", width=35, minwidth=30, stretch=tk.NO)
    tree.column("Five", width=40, minwidth=30, stretch=tk.NO)
    tree.column("Six", width=40, minwidth=30, stretch=tk.NO)
    tree.column("Seven", width=40, minwidth=30, stretch=tk.NO)

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