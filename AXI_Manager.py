import tkinter
import tkinter as tk
from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage, Button, StringVar, Scrollbar
import time
import os

import pyperclip  # clipboard Win / Linux: sudo apt-get install xclip
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
from ComparisonView import ComparisonView
from RemoveRecord import RemoveRecord
from Animation import Animation
from Search import Search
from Scrollbar import Scrollbar
from Refresh import Refresh


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


# print(switch.__doc__)


def insert_button() -> None:
    """
    The function is responsible for verifying data and inserting it into the database after the button has been pressed.

    :return: invoking the class FormValidation and DBConnect
    :rtype: None
    """

    obj_form_validator_item = FormValidation()
    obj_form_validator_item.validator_item(
        obj_new_item_ex.entry_item.get(), obj_new_item_ex.entry_qty.get()
    )
    obj_form_validator_item.clean_up_item(obj_new_item_ex.entry_item, obj_new_item_ex.entry_qty)

    obj_form_validator_v8103553_s2_ex = FormValidation()
    obj_form_validator_v8103553_s2_ex.validator(
        obj_checkbox_menu_ex_3163.EI_0.get(),
        obj_checkbox_menu_ex_3163.EI_1.get(),
        obj_checkbox_menu_ex_3163.CI_2.get(),
        obj_checkbox_menu_ex_3163.CI_3.get(),
        obj_checkbox_menu_ex_3163.CI_4.get(),
        obj_checkbox_menu_ex_3163.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
    )
    obj_form_validator_v8103553_s2_ex.clean_up(
        obj_checkbox_menu_ex_3163.EI_0,
        obj_checkbox_menu_ex_3163.EI_1,
        obj_checkbox_menu_ex_3163.CI_2,
        obj_checkbox_menu_ex_3163.CI_3,
        obj_checkbox_menu_ex_3163.CI_4,
        obj_checkbox_menu_ex_3163.EI_5,
    )
    obj_checkbox_menu_ex_3163.insertFrame.grid_forget()

    obj_db_connect_v8103553_s2_ex = DBConnect()
    obj_db_connect_v8103553_s2_ex.insert(
        "V810-3553S2EX",
        obj_form_validator_item.flagInit,
        obj_form_validator_item.item,
        obj_form_validator_item.itemAmount,
        obj_form_validator_v8103553_s2_ex.prog,
        obj_form_validator_v8103553_s2_ex.test_time,
        obj_form_validator_v8103553_s2_ex.line_capa,
        obj_form_validator_v8103553_s2_ex.epi,
        obj_form_validator_v8103553_s2_ex.baan_status,
        obj_form_validator_v8103553_s2_ex.comments,
        obj_form_validator_v8103553_s2_ex.uph85,
        obj_form_validator_v8103553_s2_ex.uph95,
        obj_form_validator_v8103553_s2_ex.uph95Time,
        obj_form_validator_v8103553_s2_ex.flag_validator,
    )
    obj_db_connect_v8103553_s2_ex.closeDB()

    obj_form_validator_v8103483_s2_ex = FormValidation()
    obj_form_validator_v8103483_s2_ex.validator(
        obj_checkbox_menu_ex_3483s2.EI_0.get(),
        obj_checkbox_menu_ex_3483s2.EI_1.get(),
        obj_checkbox_menu_ex_3483s2.CI_2.get(),
        obj_checkbox_menu_ex_3483s2.CI_3.get(),
        obj_checkbox_menu_ex_3483s2.CI_4.get(),
        obj_checkbox_menu_ex_3483s2.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
    )
    obj_form_validator_v8103483_s2_ex.clean_up(
        obj_checkbox_menu_ex_3483s2.EI_0,
        obj_checkbox_menu_ex_3483s2.EI_1,
        obj_checkbox_menu_ex_3483s2.CI_2,
        obj_checkbox_menu_ex_3483s2.CI_3,
        obj_checkbox_menu_ex_3483s2.CI_4,
        obj_checkbox_menu_ex_3483s2.EI_5,
    )
    obj_checkbox_menu_ex_3483s2.insertFrame.grid_forget()

    obj_db_connect_v8103483_s2_ex = DBConnect()
    obj_db_connect_v8103483_s2_ex.insert(
        "V810-3483S2EX",
        obj_form_validator_item.flagInit,
        obj_form_validator_item.item,
        obj_form_validator_item.itemAmount,
        obj_form_validator_v8103483_s2_ex.prog,
        obj_form_validator_v8103483_s2_ex.test_time,
        obj_form_validator_v8103483_s2_ex.line_capa,
        obj_form_validator_v8103483_s2_ex.epi,
        obj_form_validator_v8103483_s2_ex.baan_status,
        obj_form_validator_v8103483_s2_ex.comments,
        obj_form_validator_v8103483_s2_ex.uph85,
        obj_form_validator_v8103483_s2_ex.uph95,
        obj_form_validator_v8103483_s2_ex.uph95Time,
        obj_form_validator_v8103483_s2_ex.flag_validator,
    )
    obj_db_connect_v8103483_s2_ex.closeDB()

    obj_form_validator_v8103163 = FormValidation()
    obj_form_validator_v8103163.validator(
        obj_checkbox_menu_ex_3553s2.EI_0.get(),
        obj_checkbox_menu_ex_3553s2.EI_1.get(),
        obj_checkbox_menu_ex_3553s2.CI_2.get(),
        obj_checkbox_menu_ex_3553s2.CI_3.get(),
        obj_checkbox_menu_ex_3553s2.CI_4.get(),
        obj_checkbox_menu_ex_3553s2.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
    )

    obj_form_validator_v8103163.clean_up(
        obj_checkbox_menu_ex_3553s2.EI_0,
        obj_checkbox_menu_ex_3553s2.EI_1,
        obj_checkbox_menu_ex_3553s2.CI_2,
        obj_checkbox_menu_ex_3553s2.CI_3,
        obj_checkbox_menu_ex_3553s2.CI_4,
        obj_checkbox_menu_ex_3553s2.EI_5,
    )
    obj_checkbox_menu_ex_3553s2.insertFrame.grid_forget()

    obj_db_connect_v8103163 = DBConnect()
    obj_db_connect_v8103163.insert(
        "V810-3163",
        obj_form_validator_item.flagInit,
        obj_form_validator_item.item,
        obj_form_validator_item.itemAmount,
        obj_form_validator_v8103163.prog,
        obj_form_validator_v8103163.test_time,
        obj_form_validator_v8103163.line_capa,
        obj_form_validator_v8103163.epi,
        obj_form_validator_v8103163.baan_status,
        obj_form_validator_v8103163.comments,
        obj_form_validator_v8103163.uph85,
        obj_form_validator_v8103163.uph95,
        obj_form_validator_v8103163.uph95Time,
        obj_form_validator_v8103163.flag_validator,
    )
    obj_db_connect_v8103163.closeDB()

    obj_form_validator_v8108120_s2 = FormValidation()
    obj_form_validator_v8108120_s2.validator(
        obj_checkbox_menu_xxl_8120s2.EI_0.get(),
        obj_checkbox_menu_xxl_8120s2.EI_1.get(),
        obj_checkbox_menu_xxl_8120s2.CI_2.get(),
        obj_checkbox_menu_xxl_8120s2.CI_3.get(),
        obj_checkbox_menu_xxl_8120s2.CI_4.get(),
        obj_checkbox_menu_xxl_8120s2.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
    )
    obj_form_validator_v8108120_s2.clean_up(
        obj_checkbox_menu_xxl_8120s2.EI_0,
        obj_checkbox_menu_xxl_8120s2.EI_1,
        obj_checkbox_menu_xxl_8120s2.CI_2,
        obj_checkbox_menu_xxl_8120s2.CI_3,
        obj_checkbox_menu_xxl_8120s2.CI_4,
        obj_checkbox_menu_xxl_8120s2.EI_5,
    )
    obj_checkbox_menu_xxl_8120s2.insertFrame.grid_forget()

    obj_db_connect_v8108120_s2 = DBConnect()
    obj_db_connect_v8108120_s2.insert(
        "V810-8120S2",
        obj_form_validator_item.flagInit,
        obj_form_validator_item.item,
        obj_form_validator_item.itemAmount,
        obj_form_validator_v8108120_s2.prog,
        obj_form_validator_v8108120_s2.test_time,
        obj_form_validator_v8108120_s2.line_capa,
        obj_form_validator_v8108120_s2.epi,
        obj_form_validator_v8108120_s2.baan_status,
        obj_form_validator_v8108120_s2.comments,
        obj_form_validator_v8108120_s2.uph85,
        obj_form_validator_v8108120_s2.uph95,
        obj_form_validator_v8108120_s2.uph95Time,
        obj_form_validator_v8108120_s2.flag_validator,
    )
    obj_db_connect_v8108120_s2.closeDB()

    obj_form_validator_v849 = FormValidation()
    obj_form_validator_v849.validator(
        obj_checkbox_menu_5dx_v849.EI_0.get(),
        obj_checkbox_menu_5dx_v849.EI_1.get(),
        obj_checkbox_menu_5dx_v849.CI_2.get(),
        obj_checkbox_menu_5dx_v849.CI_3.get(),
        obj_checkbox_menu_5dx_v849.CI_4.get(),
        obj_checkbox_menu_5dx_v849.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
        obj_checkbox_menu_5dx_v849.EI_6.get(),
        obj_checkbox_menu_5dx_v849.EI_7.get(),
        obj_checkbox_menu_5dx_v849.EI_8.get(),
    )
    obj_form_validator_v849.clean_up(
        obj_checkbox_menu_5dx_v849.EI_0,
        obj_checkbox_menu_5dx_v849.EI_1,
        obj_checkbox_menu_5dx_v849.CI_2,
        obj_checkbox_menu_5dx_v849.CI_3,
        obj_checkbox_menu_5dx_v849.CI_4,
        obj_checkbox_menu_5dx_v849.EI_5,
        obj_checkbox_menu_5dx_v849.EI_6,
        obj_checkbox_menu_5dx_v849.EI_7,
        obj_checkbox_menu_5dx_v849.EI_8,
    )
    obj_checkbox_menu_5dx_v849.insertFrame.grid_forget()

    obj_form_validator_v817 = FormValidation()
    obj_form_validator_v817.validator(
        obj_checkbox_menu_5dx_v817.EI_0.get(),
        obj_checkbox_menu_5dx_v817.EI_1.get(),
        obj_checkbox_menu_5dx_v817.CI_2.get(),
        obj_checkbox_menu_5dx_v817.CI_3.get(),
        obj_checkbox_menu_5dx_v817.CI_4.get(),
        obj_checkbox_menu_5dx_v817.EI_5.get(),
        obj_form_validator_item.flagInit,
        obj_form_validator_item.itemAmount,
        obj_checkbox_menu_5dx_v817.EI_6.get(),
        obj_checkbox_menu_5dx_v817.EI_7.get(),
        obj_checkbox_menu_5dx_v817.EI_8.get(),
    )
    obj_form_validator_v817.clean_up(
        obj_checkbox_menu_5dx_v817.EI_0,
        obj_checkbox_menu_5dx_v817.EI_1,
        obj_checkbox_menu_5dx_v817.CI_2,
        obj_checkbox_menu_5dx_v817.CI_3,
        obj_checkbox_menu_5dx_v817.CI_4,
        obj_checkbox_menu_5dx_v817.EI_5,
        obj_checkbox_menu_5dx_v817.EI_6,
        obj_checkbox_menu_5dx_v817.EI_7,
        obj_checkbox_menu_5dx_v817.EI_8,
    )
    obj_checkbox_menu_5dx_v817.insertFrame.grid_forget()

    obj_db_connect_5dx = DBConnect()
    obj_db_connect_5dx.insert(
        "V849_V817",
        obj_form_validator_item.flagInit,
        obj_form_validator_item.item,
        obj_form_validator_item.itemAmount,
        obj_form_validator_v849.prog,
        obj_form_validator_v849.test_time,
        obj_form_validator_v849.line_capa,
        obj_form_validator_v849.epi,
        obj_form_validator_v849.baan_status,
        obj_form_validator_v849.comments,
        obj_form_validator_v849.uph85,
        obj_form_validator_v849.uph95,
        obj_form_validator_v849.uph95Time,
        obj_form_validator_v849.flag_validator,
        obj_form_validator_v849.alignTime,
        obj_form_validator_v849.laserTime,
        obj_form_validator_v849.thicknessTime,
        obj_form_validator_v849.totalTime,
        obj_form_validator_v817.flag_validator,
        obj_form_validator_v817.prog,
        obj_form_validator_v817.test_time,
        obj_form_validator_v817.line_capa,
        obj_form_validator_v817.epi,
        obj_form_validator_v817.baan_status,
        obj_form_validator_v817.comments,
        obj_form_validator_v817.uph85,
        obj_form_validator_v817.uph95,
        obj_form_validator_v817.uph95Time,
        obj_form_validator_v817.alignTime,
        obj_form_validator_v817.laserTime,
        obj_form_validator_v817.thicknessTime,
        obj_form_validator_v817.totalTime,
    )
    obj_db_connect_5dx.closeDB()
    if (
        obj_db_connect_v8103553_s2_ex.flagSucceeded
        or obj_db_connect_v8103483_s2_ex.flagSucceeded
        or obj_db_connect_v8103163.flagSucceeded
        or obj_db_connect_v8108120_s2.flagSucceeded
        or obj_db_connect_5dx.flagSucceeded
    ):
        obj_tip_new = Tip(root, obj_new_item_ex.main_frame)
        # obj_tip_new.animate_non_translucent()
        obj_tip_new.animate_translucent()
        refresh()


def reset() -> None:
    """
    The function cleanup the form

    :return: cleanup part of form
    :rtype: None
    """
    obj_new_item_ex.clean_up()

    obj_checkbox_menu_ex_3163.cleanUp()
    obj_checkbox_menu_ex_3163.insertFrame.grid_forget()

    obj_checkbox_menu_ex_3483s2.cleanUp()
    obj_checkbox_menu_ex_3483s2.insertFrame.grid_forget()

    obj_checkbox_menu_ex_3553s2.cleanUp()
    obj_checkbox_menu_ex_3553s2.insertFrame.grid_forget()

    obj_checkbox_menu_xxl_8120s2.cleanUp()
    obj_checkbox_menu_xxl_8120s2.insertFrame.grid_forget()

    obj_checkbox_menu_5dx_v849.cleanUp()
    obj_checkbox_menu_5dx_v849.cleanUp5DX()
    obj_checkbox_menu_5dx_v849.insertFrame.grid_forget()

    obj_checkbox_menu_5dx_v817.cleanUp()
    obj_checkbox_menu_5dx_v817.cleanUp5DX()
    obj_checkbox_menu_5dx_v817.insertFrame.grid_forget()


def get_selected_row(event) -> None:
    """
    Capture the row

    :return: show information of one record from DB
    :rtype: None
    """
    flag_animation: bool = False
    flag_click: bool = False

    reset()

    for nm in tree.selection():
        content = tree.item(nm, "values")

        if content[1] in obj_config.machines:
            flag_click = True

        obj_db = DBConnect()
        for row in obj_db.selectSearchID(content[0]):
            pass
        obj_db.closeDB()

        pyperclip.copy(row[1])  # clipboard Win / Linux: sudo apt-get install xclip

        obj_new_item_ex.entry_item.insert(0, f"{row[1]}")
        obj_new_item_ex.entry_qty.insert(0, f"{row[3]}")

        obj_tree = ContextualMenu(root, str(row[0]), False, False, True)
        tree.bind("<Button-3>", obj_tree.do_popup)
        root.bind("<Button-1>", obj_tree.release_contextual_menu)
        if RemoveRecord.flag is True:
            refresh()
            RemoveRecord.flag = False

        if row[54] is not None and ((row[52] is not None and int(row[52]) > 0) or int(row[49])):
            obj_checkbox_menu_ex_3163.EI_0.insert(0, f"{row[54]}")
            obj_checkbox_menu_ex_3163.EI_1.insert(0, f"{int(row[52])}")
            obj_checkbox_menu_ex_3163.CI_2.current(switch(row[55]))
            obj_checkbox_menu_ex_3163.CI_3.current(switch(row[56]))
            obj_checkbox_menu_ex_3163.CI_4.current(switch(row[53]))
            obj_checkbox_menu_ex_3163.EI_5.insert(0, f"{row[57]}")
            obj_checkbox_menu_ex_3163.insertFrame.grid(
                column=0, row=5 + 1, columnspan=10, sticky="W", padx=10, pady=10
            )

        if row[45] is not None and ((row[43] is not None and int(row[43]) > 0) or int(row[40])):
            obj_checkbox_menu_ex_3483s2.EI_0.insert(0, f"{row[45]}")
            obj_checkbox_menu_ex_3483s2.EI_1.insert(0, f"{int(row[43])}")
            obj_checkbox_menu_ex_3483s2.CI_2.current(switch(row[46]))
            obj_checkbox_menu_ex_3483s2.CI_3.current(switch(row[47]))
            obj_checkbox_menu_ex_3483s2.CI_4.current(switch(row[44]))
            obj_checkbox_menu_ex_3483s2.EI_5.insert(0, f"{row[48]}")
            obj_checkbox_menu_ex_3483s2.insertFrame.grid(
                column=0, row=5 + 2, columnspan=10, sticky="W", padx=10, pady=10
            )

        if row[27] is not None and ((row[15] is not None and int(row[15]) > 0) or int(row[12])):
            obj_checkbox_menu_ex_3553s2.EI_0.insert(0, f"{row[27]}")
            obj_checkbox_menu_ex_3553s2.EI_1.insert(0, f"{int(row[15])}")
            obj_checkbox_menu_ex_3553s2.CI_2.current(switch(row[28]))
            obj_checkbox_menu_ex_3553s2.CI_3.current(switch(row[29]))
            obj_checkbox_menu_ex_3553s2.CI_4.current(switch(row[16]))
            obj_checkbox_menu_ex_3553s2.EI_5.insert(0, f"{row[30]}")
            obj_checkbox_menu_ex_3553s2.insertFrame.grid(
                column=0, row=5 + 3, columnspan=10, sticky="W", padx=10, pady=10
            )

        if row[31] is not None and ((row[37] is not None and int(row[37]) > 0) or int(row[39])):
            obj_checkbox_menu_xxl_8120s2.EI_0.insert(0, f"{row[31]}")
            obj_checkbox_menu_xxl_8120s2.EI_1.insert(0, f"{int(row[37])}")
            obj_checkbox_menu_xxl_8120s2.CI_2.current(switch(row[32]))
            obj_checkbox_menu_xxl_8120s2.CI_3.current(switch(row[33]))
            obj_checkbox_menu_xxl_8120s2.CI_4.current(switch(row[38]))
            obj_checkbox_menu_xxl_8120s2.EI_5.insert(0, f"{row[34]}")
            obj_checkbox_menu_xxl_8120s2.insertFrame.grid(
                column=0, row=5 + 5, columnspan=10, sticky="W", padx=10, pady=10
            )

        if (row[17] is not None and row[17] != "") and (
            (row[5] is not None and int(row[5]) > 0) or int(row[4])
        ):
            obj_checkbox_menu_5dx_v849.EI_0.insert(0, f"{row[17]}")
            obj_checkbox_menu_5dx_v849.EI_1.insert(0, f"{int(row[10])}")
            obj_checkbox_menu_5dx_v849.CI_2.current(switch(row[18]))
            obj_checkbox_menu_5dx_v849.CI_3.current(switch(row[19]))
            obj_checkbox_menu_5dx_v849.CI_4.current(switch(row[11]))
            obj_checkbox_menu_5dx_v849.EI_5.insert(0, f"{row[20]}")
            obj_checkbox_menu_5dx_v849.EI_6.insert(0, f"{int(row[7])}")
            obj_checkbox_menu_5dx_v849.EI_7.insert(0, f"{int(row[8])}")
            obj_checkbox_menu_5dx_v849.EI_8.insert(0, f"{int(row[9])}")
            obj_checkbox_menu_5dx_v849.insertFrame.grid(
                column=0, row=5 + 1, columnspan=10, sticky="W", padx=10, pady=10
            )

        if (row[22] is not None and row[22] != "") and (
            (row[5] is not None and int(row[5]) > 0) or int(row[4])
        ):
            obj_checkbox_menu_5dx_v817.EI_0.insert(0, f"{row[22]}")
            obj_checkbox_menu_5dx_v817.EI_1.insert(0, f"{int(row[10])}")
            obj_checkbox_menu_5dx_v817.CI_2.current(switch(row[23]))
            obj_checkbox_menu_5dx_v817.CI_3.current(switch(row[24]))
            obj_checkbox_menu_5dx_v817.CI_4.current(switch(row[11]))
            obj_checkbox_menu_5dx_v817.EI_5.insert(0, f"{row[25]}")
            obj_checkbox_menu_5dx_v817.EI_6.insert(0, f"{int(row[7])}")
            obj_checkbox_menu_5dx_v817.EI_7.insert(0, f"{int(row[8])}")
            obj_checkbox_menu_5dx_v817.EI_8.insert(0, f"{int(row[9])}")
            obj_checkbox_menu_5dx_v817.insertFrame.grid(
                column=0, row=5 + 2, columnspan=10, sticky="W", padx=10, pady=10
            )

        obj_item = ContextualMenu(root, content[0], False, False, True)
        l_item.configure(text=f"{row[1]}")
        l_item.configure(text=f"{row[1]}")
        l_item.bind("<Button-3>", obj_item.do_popup)
        root.bind("<Button-1>", obj_item.release_contextual_menu)
        l_item_amount.configure(text=f"{row[3]}")
        l_date_db.configure(text=f"{row[2]}")
        l_qty.configure(text=f"Qty:")
        l_date.configure(text=f"Inserted:")

        # ---get_selected_row 5DX V849---
        if int(len(str(row[17]))) > 4:
            tab_control_main.add(tab_main1, text=" V849 ")
            l_v849_prog.configure(text=f"{row[17]}")
            l_v849_scan_time_l.configure(text=f"Scan Time:")
            l_v849_uph85_l.configure(text=f"UPH 85%:")
            l_v849_uph95_l.configure(text=f"UPH 95%:")
            l_v849_baan_l.configure(text=f"BaaN:")
            l_v849_lc_l.configure(text=f"LC:")
            l_v849_epi_l.configure(text=f"EPI:")
            l_v849_comment_l.configure(text=f"Comment:")
            l_v849_scan_time.configure(
                text=f"{int(row[7]) + int(row[8]) + int(row[9]) + int(row[10])}"
                f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s."
            )
            try:
                l_v849_uph_85.configure(
                    text=f"{row[4]} ({round(60 / int(row[4]), 4)}), "
                    f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[4])), 4)}s."
                )
            except ZeroDivisionError:
                l_v849_uph_85.configure(text=f"(0), " f"Panel: 0 s. " f"Board: 0 s.")
            try:
                l_v849_uph_95.configure(
                    text=f"{row[6]} ({round(60 / int(row[6]), 4)}), "
                    f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[6])), 4)}s."
                )
            except ZeroDivisionError:
                l_v849_uph_95.configure(text=f"(0), " f"Panel: 0 s. " f"Board: 0 s.")
            if str(row[11]) == "YES":
                l_v849_baan.configure(text=f"{row[11]}", fg="#AAAAAA")
            else:
                l_v849_baan.configure(text=f"{row[11]}", fg="#D44339")
            if str(row[18]) == "YES":
                l_V849_lc.configure(text=f"{row[18]}", fg="#AAAAAA")
            else:
                l_V849_lc.configure(text=f"{row[18]}", fg="#D44339")
            if str(row[19]) == "YES":
                l_v849_epi.configure(text=f"{row[19]}", fg="#AAAAAA")
            else:
                l_v849_epi.configure(text=f"{row[19]}", fg="#D44339")

            l_v849_comment.configure(text=f"{row[20]}")

            # ---get_selected_row 5DX V849---
            canvas_frame1 = Label(tab_main1)
            canvas_frame1.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas1 = tk.Canvas(canvas_frame1, width=170, height=170)
            canvas1.configure(bg="#444444")
            canvas1.pack(expand=False)

            if os.path.isfile(obj_config.pathImg5DX1 + row[17] + ".png") is False:
                # resize_image(obj_config.pathImg5DX1 + row[17] + ".jpg")
                Animation.resize_image(obj_config.pathImg5DX1 + row[17] + ".jpg")

            if flag_animation is False:
                tab_control_main.select(tab_main1)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImg5DX1 + row[17] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas1,
                                                          obj_config.pathImg5DX1 + row[17] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True

            img_board1 = obj_config.pathImg5DX1 + row[17] + ".png"

            if os.path.isfile(img_board1):
                img1 = tk.PhotoImage(file=img_board1)
            else:
                img1 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas1.create_image(85, 85, image=img1)

        else:
            tab_control_main.hide(tab_main1)

        # ---The End get_selected_row 5DX V849---
        # ---get_selected_row 5DX V817---

        if int(len(str(row[22]))) > 4:
            tab_control_main.add(tab_main2, text=" V817 ")
            l_v817_prog.configure(text=f"{row[22]}")
            l_v817_scan_time_l.configure(text=f"Scan Time:")
            l_v817_uph85_l.configure(text=f"UPH 85%:")
            l_v817_uph95_l.configure(text=f"UPH 95%:")
            l_v817_baan_l.configure(text=f"BaaN:")
            l_v817_lc_l.configure(text=f"LC:")
            l_v817_epi_l.configure(text=f"EPI:")
            l_v817_comment_l.configure(text=f"Comment:")
            l_v817_scan_time.configure(
                text=f"{int(row[7]) + int(row[8]) + int(row[9]) + int(row[10])}"
                f" + 15 in/out = {int(row[7])+int(row[8])+int(row[9])+int(row[10])+15}s."
            )
            try:
                l_v817_uph85.configure(
                    text=f"{row[4]} ({round(60 / int(row[4]), 4)}), "
                    f"Panel: {round((3600/int(row[4])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[4])), 4)}s."
                )
            except ZeroDivisionError:
                l_v817_uph85.configure(text=f"(0), " f"Panel: 0 s. " f"Board: 0 s.")

            try:
                l_v817_uph95.configure(
                    text=f"{row[6]} ({round(60 / int(row[6]), 4)}), "
                    f"Panel: {round((3600/int(row[6])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[6])), 4)}s."
                )
            except ZeroDivisionError:
                l_v817_uph95.configure(text=f"(0), " f"Panel: 0 s. " f"Board: 0 s.")

            if str(row[11]) == "YES":
                l_v817_baan.configure(text=f"{row[11]}", fg="#AAAAAA")
            else:
                l_v817_baan.configure(text=f"{row[11]}", fg="#D44339")
            if str(row[23]) == "YES":
                l_v817_lc.configure(text=f"{row[23]}", fg="#AAAAAA")
            else:
                l_v817_lc.configure(text=f"{row[23]}", fg="#D44339")
            if str(row[24]) == "YES":
                l_v817_epi.configure(text=f"{row[24]}", fg="#AAAAAA")
            else:
                l_v817_epi.configure(text=f"{row[24]}", fg="#D44339")

            l_v817_comment.configure(text=f"{row[25]}")

            canvas_frame2 = Label(tab_main2)
            canvas_frame2.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas2 = tk.Canvas(canvas_frame2, width=170, height=170)
            canvas2.configure(bg="#444444")
            canvas2.pack(expand=False)

            if os.path.isfile(obj_config.pathImg5DX2 + row[22] + ".png") is False:
                # resize_image(obj_config.pathImg5DX2 + row[22] + ".jpg")
                Animation.resize_image(obj_config.pathImg5DX2 + row[22] + ".jpg")

            if flag_animation is False:
                tab_control_main.select(tab_main2)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImg5DX2 + row[22] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas2,
                                                          obj_config.pathImg5DX2 + row[22] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True

            img_board2 = obj_config.pathImg5DX2 + row[22] + ".png"
            if os.path.isfile(img_board2):
                img2 = tk.PhotoImage(file=img_board2)
            else:
                img2 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas2.create_image(85, 85, image=img2)

        else:
            tab_control_main.hide(tab_main2)
        # ---The End get_selected_row 5DX V817---
        # ---get_selected_row V810-3163--
        # if len(str(row[27])) > 4:
        if row[27] is not None and (
            (int(row[15]) != 0 or int(row[14]) != 0) or int(row[12])
        ):
            tab_control_main.add(tab_main3, text=" V810-3163 ")
            l_v8103163_prog.configure(text=f"{row[27]}")
            l_v8103163_scan_time_l.configure(text=f"Scan Time:")
            l_v8103163_uph85_l.configure(text=f"UPH 85%:")
            l_v8103163_uph95_l.configure(text=f"UPH 95%:")
            l_v8103163_baan_l.configure(text=f"BaaN:")
            l_v8103163_lc_l.configure(text=f"LC:")
            l_v8103163_epi_l.configure(text=f"EPI:")
            l_v8103163_comment_l.configure(text=f"Comment:")
            l_v8103163_scan_time.configure(
                text=f"{int(row[15])} + 15 in/out = {int(row[15] + 15)}s."
            )
            try:
                l_v8103163_uph85.configure(
                    text=f"{row[12]} ({round(60 / int(row[12]), 4)}), "
                    f"Panel: {round((3600/int(row[12]) * int(row[3])))}s. "
                    f"Board: {round((3600/int(row[12])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103163_uph85.configure(text=f"(0), " f"Panel: 0s. " f"Board: 0s.")
            try:
                l_v8103163_uph95.configure(
                    text=f"{row[14]} ({round(60 / int(row[14]), 4)}), "
                    f"Panel: {round((3600/int(row[14])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[14])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103163_uph95.configure(text=f"(0), " f"Panel: 0s. " f"Board: 0s.")
            if str(row[16]) == "YES":
                l_v8103163_baan.configure(text=f"{row[16]}", fg="#AAAAAA")
            else:
                l_v8103163_baan.configure(text=f"{row[16]}", fg="#D44339")
            if str(row[28]) == "YES":
                l_v8103163_lc.configure(text=f"{row[28]}", fg="#AAAAAA")
            else:
                l_v8103163_lc.configure(text=f"{row[28]}", fg="#D44339")
            if str(row[29]) == "YES":
                l_v8103163_epi.configure(text=f"{row[29]}", fg="#AAAAAA")
            else:
                l_v8103163_epi.configure(text=f"{row[29]}", fg="#D44339")

            l_v8103163_comment.configure(text=f"{row[30]}")

            canvas_frame3 = Label(tab_main3)
            canvas_frame3.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas3 = tk.Canvas(canvas_frame3, width=170, height=170)
            canvas3.configure(bg="#444444")
            canvas3.pack(expand=False)

            if flag_animation is False:
                tab_control_main.select(tab_main3)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImgV8103163 + row[27] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas3,
                                                          obj_config.pathImgV8103163 + row[27] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True

            img_board3 = obj_config.pathImgV8103163 + row[27] + ".png"
            if os.path.isfile(img_board3):
                img3 = tk.PhotoImage(file=img_board3)
            else:
                img3 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas3.create_image(85, 85, image=img3)

        else:
            tab_control_main.hide(tab_main3)

        # ---The End get_selected_row V810-3163---

        # ---get_selected_row V810-V3483S2EX---
        if row[45] is not None and ((row[43] is not None and int(row[43]) > 0) or int(row[40])):
            tab_control_main.add(tab_main4, text=" V810-3483S2EX ")
            l_v8103483s2ex_prog.configure(text=f"{row[45]}")
            l_v8103483s2ex_scan_time_l.configure(text=f"Scan Time:")
            l_v8103483s2ex_uph85_l.configure(text=f"UPH 85%:")
            l_v8103483s2ex_uph95_l.configure(text=f"UPH 95%:")
            L_v8103483s2_ex_baan_l.configure(text=f"BaaN:")
            l_v8103483s2ex_lc_l.configure(text=f"LC:")
            l_v8103483s2ex_epi_l.configure(text=f"EPI:")
            l_v8103483s2ex_comment_l.configure(text=f"Comment:")
            l_v8103483s2ex_scan_time.configure(
                text=f"{int(row[43])} + 15 in/out = {int(row[43] + 15)}s."
            )
            try:
                l_v8103483s2ex_uph85.configure(
                    text=f"{row[40]} ({round(60 / int(row[40]), 4)}), "
                    f"Panel: {round((3600/int(row[40])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[40])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103483s2ex_uph85.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )

            try:
                l_v8103483s2ex_uph95.configure(
                    text=f"{row[42]} ({round(60 / int(row[42]), 4)}), "
                    f"Panel: {round((3600/int(row[42])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[42])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103483s2ex_uph95.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )
            if str(row[44]) == "YES":
                l_v8103483s2ex_baan.configure(text=f"{row[44]}", fg="#AAAAAA")
            else:
                l_v8103483s2ex_baan.configure(text=f"{row[44]}", fg="#D44339")
            if str(row[46]) == "YES":
                l_v8103483s2ex_lc.configure(text=f"{row[46]}", fg="#AAAAAA")
            else:
                l_v8103483s2ex_lc.configure(text=f"{row[46]}", fg="#D44339")
            if str(row[47]) == "YES":
                l_v8103483s2ex_epi.configure(text=f"{row[47]}", fg="#AAAAAA")
            else:
                l_v8103483s2ex_epi.configure(text=f"{row[47]}", fg="#D44339")

            l_v8103483s2ex_comment.configure(text=f"{row[48]}")

            canvas_frame4 = Label(tab_main4)
            canvas_frame4.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas4 = tk.Canvas(canvas_frame4, width=170, height=170)
            canvas4.configure(bg="#444444")
            canvas4.pack(expand=False)

            if flag_animation is False:
                tab_control_main.select(tab_main4)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImgV8103483S2EX + row[45] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas4,
                                                          obj_config.pathImgV8103483S2EX + row[45] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True

            img_board4 = obj_config.pathImgV8103483S2EX + row[45] + ".png"
            if os.path.isfile(img_board4):
                img4 = tk.PhotoImage(file=img_board4)
            else:
                img4 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas4.create_image(85, 85, image=img4)

        else:
            tab_control_main.hide(tab_main4)
        # --- The End get_selected_row V810-3483S2EX ---

        # --- get_selected_row V810-3553S2EX ---

        if row[54] is not None and ((row[52] is not None and int(row[52]) > 0) or int(row[49])):
            tab_control_main.add(tab_main5, text=" V810-3553S2EX ")
            l_v8103553s2ex_prog.configure(text=f"{row[54]}")
            l_v8103553s2ex_scan_time_l.configure(text=f"Scan Time: ")
            l_v8103553s2ex_uph85_l.configure(text=f"UPH 85%:")
            l_v8103553s2ex_uph95_l.configure(text=f"UPH 95%:")
            l_v8103553s2ex_baan_l.configure(text=f"BaaN:")
            l_v8103553s2ex_lc_l.configure(text=f"LC:")
            l_v8103553s2ex_epi_l.configure(text=f"EPI:")
            l_v8103553s2ex_comment_l.configure(text=f"Comment:")
            l_v8103553s2ex_scan_time.configure(
                text=f"{int(row[52])} + 15 in/out = {int(row[52] + 15)}s."
            )
            try:
                l_v8103553s2ex_uph85.configure(
                    text=f"{row[49]} ({round(60 / int(row[49]), 4)}), "
                    f"Panel: {round((3600/int(row[49])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[49])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103553s2ex_uph85.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )
            try:
                l_v8103553s2ex_uph95.configure(
                    text=f"{row[51]} ({round(60 / int(row[51]), 4)}), "
                    f"Panel: {round((3600/int(row[51])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[51])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8103553s2ex_uph95.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )

            if str(row[53]) == "YES":
                l_v8103553s2ex_baan.configure(text=f"{row[53]}", fg="#AAAAAA")
            else:
                l_v8103553s2ex_baan.configure(text=f"{row[53]}", fg="#D44339")
            if str(row[55]) == "YES":
                l_v8103553s2ex_lc.configure(text=f"{row[55]}", fg="#AAAAAA")
            else:
                l_v8103553s2ex_lc.configure(text=f"{row[55]}", fg="#D44339")
            if str(row[56]) == "YES":
                l_v8103553s2ex_epi.configure(text=f"{row[56]}", fg="#AAAAAA")
            else:
                l_v8103553s2ex_epi.configure(text=f"{row[56]}", fg="#D44339")

            l_v8103553s2ex_comment.configure(text=f"{row[57]}")

            canvas_frame5 = Label(tab_main5)
            canvas_frame5.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas5 = tk.Canvas(canvas_frame5, width=170, height=170)
            canvas5.configure(bg="#444444")
            canvas5.pack(expand=False)

            if flag_animation is False:
                tab_control_main.select(tab_main5)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImgV8103553S2EX + row[54] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas5,
                                                          obj_config.pathImgV8103553S2EX + row[54] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True

            img_board5 = obj_config.pathImgV8103553S2EX + row[54] + ".png"
            if os.path.isfile(img_board5):
                img5 = tk.PhotoImage(file=img_board5)
            else:
                img5 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas5.create_image(85, 85, image=img5)

        else:
            tab_control_main.hide(tab_main5)
        # --- The End get_selected_row V810-3553S2EX ---

        # --- get_selected_row V810-8120S2 ---
        if row[31] is not None and ((row[37] is not None and int(row[37]) > 0) or int(row[39])):
            tab_control_main.add(tab_main6, text=" V810-8120S2 ")
            l_v8108120s2_prog.configure(text=f"{row[31]}")
            l_v8108120s2_scan_time_l.configure(text=f"Scan Time:")
            l_v8108120s2_uph85_l.configure(text=f"UPH 85%:")
            l_v8108120s2_uph95_l.configure(text=f"UPH 95%:")
            l_v8108120s2_baan_l.configure(text=f"BaaN:")
            l_v8108120s2lc_l.configure(text=f"LC:")
            l_v8108120s2epi_l.configure(text=f"EPI:")
            l_v8108120s2comment_l.configure(text=f"Comment:")
            l_v8108120s2_scan_time.configure(
                text=f"{int(row[37])} + 15 in/out = {int(row[37] + 15)}s."
            )
            try:
                l_v8108120s2_uph85.configure(
                    text=f"{row[39]} ({round(60 / int(row[39]), 4)}), "
                    f"Panel: {round((3600/int(row[39])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[39])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8108120s2_uph85.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )
            try:
                l_v8108120s2uph95.configure(
                    text=f"{row[36]} ({round(60 / int(row[36]), 4)}), "
                    f"Panel: {round((3600/int(row[36])*int(row[3])))}s. "
                    f"Board: {round((3600/int(row[36])), 4)}s."
                )
            except ZeroDivisionError:
                l_v8108120s2uph95.configure(
                    text=f"(0), " f"Panel: 0 s. " f"Board: 0 s."
                )

            if str(row[38]) == "YES":
                l_v8108120s2_baan.configure(text=f"{row[38]}", fg="#AAAAAA")
            else:
                l_v8108120s2_baan.configure(text=f"{row[38]}", fg="#D44339")
            if str(row[32]) == "YES":
                l_v8108120s2_lc.configure(text=f"{row[32]}", fg="#AAAAAA")
            else:
                l_v8108120s2_lc.configure(text=f"{row[32]}", fg="#D44339")
            if str(row[33]) == "YES":
                l_v8108120s2_epi.configure(text=f"{row[33]}", fg="#AAAAAA")
            else:
                l_v8108120s2_epi.configure(text=f"{row[33]}", fg="#D44339")

            l_v8108120s2_comment.configure(text=f"{row[34]}")

            canvas_frame6 = Label(tab_main6)
            canvas_frame6.grid(row=0, column=6, rowspan=6, sticky=W)
            canvas6 = tk.Canvas(canvas_frame6, width=170, height=170)
            canvas6.configure(bg="#444444")
            canvas6.pack(expand=False)

            if flag_animation is False:
                tab_control_main.select(tab_main6)
                if flag_click is False:
                    try:
                        if os.path.isfile(obj_config.pathImgV8108120S2 + row[31] + ".png"):
                            try:
                                obj_animation = Animation(root,
                                                          canvas6,
                                                          obj_config.pathImgV8108120S2 + row[31] + ".png")
                                obj_animation.move_image()
                            except FileNotFoundError:
                                pass
                    except tk.TclError:
                        pass

                flag_animation = True
            img_board6 = obj_config.pathImgV8108120S2 + row[31] + ".png"
            if os.path.isfile(img_board6):
                img6 = tk.PhotoImage(file=img_board6)
            else:
                img6 = tk.PhotoImage(file=obj_config.pathImgDefault)
            canvas6.create_image(85, 85, image=img6)

        else:
            tab_control_main.hide(tab_main6)
        # --- The End get_selected_row V810-8120S2 ---

        if flag_click is True:
            flag_click = False
            if content[1] == "5DX I":
                tab_control_main.select(tab_main1)
            elif content[1] == "5DX II":
                tab_control_main.select(tab_main2)
            elif content[1] == "ViTrox Ex I":
                tab_control_main.select(tab_main3)
            elif content[1] == "ViTrox Ex II":
                tab_control_main.select(tab_main4)
            elif content[1] == "ViTrox Ex III":
                tab_control_main.select(tab_main5)
            elif content[1] == "ViTrox XXL I":
                tab_control_main.select(tab_main6)

        root.mainloop()


def refresh() -> None:
    """
    The function returns the table to the default shape. Show all record from DB.

    :return: Show all records in table from DB
    :rtype: None
    """
    tree.selection_clear()
    tree.selection_remove(tree.focus())
    e_search.delete(0, END)
    for record in tree.get_children():
        tree.delete(record)


    # ---Create striped row tags---
    tree.tag_configure("DX", background="#222222")
    tree.tag_configure("V", background="#333333")
    tree.tag_configure("one", background="#111111")
    tree.tag_configure("baanGrey", background="#111111", foreground="#EB0E0E")  # red font
    tree.tag_configure("baanDark", foreground="#EB0E0E")
    tree.tag_configure("lcGrey", background="#111111", foreground="#FF8000")  # green font
    tree.tag_configure("lcDark", foreground="#FF8000")
    # ---The End Create striped row---

    main_index = 1
    sub_index = 1
    obj_db = DBConnect()
    obj_refresh = Refresh()
    for row in obj_db.selectAll():
        if main_index % 2 == 0:
            # row[11] 5DX_BAAN1, row[16] VITROX_BAAN1, row[38] VITROXII_BAAN1,
            # row[44] VITROXIII_BAAN1, row[53] VITROXIV_BAAN1
            if obj_refresh.foreign_app_status(row[11], row[16], row[38], row[44], row[53]):
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=sub_index,
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    tag="baanGrey",
                )
            # row[18] 5DXI_LINECAPA, row[23] 5DXII_LINECAPA, row[28] VITROXI_LINECAPA,
            # row[32] VITROXII_LINECAPA, row[46] VITROXIII_LINECAPA, row[55] VITROXIV_LINECAPA
            elif obj_refresh.foreign_app_status(row[18], row[23], row[28], row[32], row[46], row[55]):
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=sub_index,
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    tag="lcGrey",
                )
            else:
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=sub_index,
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    tag="one",
                )
        else:
            # row[11] 5DX_BAAN1, row[16] VITROX_BAAN1, row[38] VITROXII_BAAN1,
            # row[44] VITROXIII_BAAN1, row[53] VITROXIV_BAAN1
            if obj_refresh.foreign_app_status(row[11], row[16], row[38], row[44], row[53]):
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=sub_index,
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    tag="baanDark",
                )
            # row[18] 5DXI_LINECAPA, row[23] 5DXII_LINECAPA, row[28] VITROXI_LINECAPA,
            # row[32] VITROXII_LINECAPA, row[46] VITROXIII_LINECAPA, row[55] VITROXIV_LINECAPA
            elif obj_refresh.foreign_app_status(row[18], row[23], row[28], row[32], row[46], row[55]):
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=sub_index,
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    tag="lcDark",
                )
            else:
                folder1 = tree.insert(
                    parent="",
                    index=main_index,
                    iid=str(sub_index),
                    text=f" ",
                    values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                )

        sub_index += 1
        if int(len(str(row[17]))) > 4:
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[0]}",
                    f"85%: {row[4]}, 95%: {row[6]}",
                    "",
                    f"{row[11]}",
                    f"{row[18]}",
                    f"{row[19]}",
                ),
                tags="DX",
            )
        sub_index += 2
        if int(len(str(row[22]))) > 4:
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[1]}",
                    f"85%: {row[4]}, 95%: {row[6]}",
                    "",
                    f"{row[11]}",
                    f"{row[23]}",
                    f"{row[24]}",
                ),
                tags="DX",
            )
        sub_index += 3

        if row[27] is not None and (
            (int(row[15]) != 0 or int(row[14]) != 0) or int(row[12])
        ):
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[2]}",
                    f"85%: {row[12]}, 95%: {row[14]}",
                    "",
                    f"{row[16]}",
                    f"{row[28]}",
                    f"{row[29]}",
                ),
                tags="V",
            )
        sub_index += 4

        if row[45] is not None and (
            (row[43] is not None and int(row[43]) > 0) or int(row[40])
        ):
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[3]}",
                    f"85%: {row[40]}, 95%: {row[42]}",
                    "",
                    f"{row[44]}",
                    f"{row[46]}",
                    f"{row[47]}",
                ),
                tags="V",
            )
        sub_index += 4

        if row[54] is not None and (
            (row[52] is not None and int(row[52]) > 0) or int(row[49])
        ):
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[4]}",
                    f"85%: {row[49]}, 95%: {row[51]}",
                    "",
                    f"{row[53]}",
                    f"{row[55]}",
                    f"{row[56]}",
                ),
                tags="V",
            )
        sub_index += 5

        if row[31] is not None and (
            (row[37] is not None and int(row[37]) > 0) or int(row[39])
        ):
            tree.insert(
                folder1,
                index="end",
                iid=str(sub_index),
                text=f"",
                values=(
                    f"{row[0]}",
                    f"{obj_config.machines[5]}",
                    f"85%: {row[39]}, 95%: {row[36]}",
                    "",
                    f"{row[38]}",
                    f"{row[32]}",
                    f"{row[33]}",
                ),
                tags="V",
            )

        tree.bind("<<TreeviewSelect>>", get_selected_row)

        tree.grid(row=1, column=0, columnspan=3, pady=2)
        main_index += 1
        sub_index += 1

    obj_db.closeDB()
# ---Scrollbar--------------
    obj_scrollbar = Scrollbar(tab1, tree)
    obj_scrollbar.tree_scrollbar()

    # vsb = ttk.Scrollbar(tab1, orient="vertical", command=tree.yview)
    # vsb.place(
    #     x=obj_config.scrollX, y=obj_config.scrollY, height=obj_config.scrollHeight
    # )
    # tree.configure(yscrollcommand=vsb.set)
# ---The End of Scrollbar---


def automatic_insert() -> None:
    """
    The function fulfills the form with data from a selected new recipe.

    :return: Fulfills the entry with data
    :rtype: None
    """
    msg_box = tk.messagebox.askquestion(
        f"Automatic adding",
        'In the "Add" tab you have a new record. Do you want to upload this now?',
    )
    if msg_box == "yes":
        reset()
        tab_control.select(tab2)
        flag_selected_record = False
        obj_automatic_updates = AutomaticUpdates()
        new_item = var_new_record.get()
        if new_item in obj_automatic_updates.bildGrid():
            item_name = (
                obj_automatic_updates.dicRecipe.get(var_new_record.get())
                .get("recipe")
                .replace("_", "/")
            )
            obj_new_item_ex.entry_item.insert(0, f"{item_name}")
            obj_new_item_ex.entry_qty.insert(
                0,
                f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('boardQty')}",
            )
            if (
                obj_automatic_updates.dicRecipe.get(var_new_record.get()).get("device")
                == "V810-3553S2EX"
            ):
                obj_checkbox_menu_ex_3163.insertFrame.grid(
                    column=0, row=5 + 1, columnspan=10, sticky="W", padx=10, pady=10
                )
                obj_checkbox_menu_ex_3163.EI_0.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('recipe')}",
                )
                obj_checkbox_menu_ex_3163.EI_1.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('cycleTime')}",
                )
                flag_selected_record = True
            if (
                obj_automatic_updates.dicRecipe.get(var_new_record.get()).get("device")
                == "V810-3483S2EX"
            ):
                obj_checkbox_menu_ex_3483s2.insertFrame.grid(
                    column=0, row=5 + 2, columnspan=10, sticky="W", padx=10, pady=10
                )
                obj_checkbox_menu_ex_3483s2.EI_0.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('recipe')}",
                )
                obj_checkbox_menu_ex_3483s2.EI_1.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('cycleTime')}",
                )
                flag_selected_record = True
            if (
                obj_automatic_updates.dicRecipe.get(var_new_record.get()).get("device")
                == "V810-3163"
            ):
                obj_checkbox_menu_ex_3553s2.insertFrame.grid(
                    column=0, row=5 + 3, columnspan=10, sticky="W", padx=10, pady=10
                )
                obj_checkbox_menu_ex_3553s2.EI_0.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('recipe')}",
                )
                obj_checkbox_menu_ex_3553s2.EI_1.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('cycleTime')}",
                )
                flag_selected_record = True
            if (
                obj_automatic_updates.dicRecipe.get(var_new_record.get()).get("device")
                == "V810-8120S2"
            ):
                obj_checkbox_menu_xxl_8120s2.insertFrame.grid(
                    column=0, row=5 + 5, columnspan=10, sticky="W", padx=10, pady=10
                )
                obj_checkbox_menu_xxl_8120s2.EI_0.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('recipe')}",
                )
                obj_checkbox_menu_xxl_8120s2.EI_1.insert(
                    0,
                    f"{obj_automatic_updates.dicRecipe.get(var_new_record.get()).get('cycleTime')}",
                )
                flag_selected_record = True

        if flag_selected_record is True:
            obj_automatic_updates.updateDic(var_new_record.get())
            add_frame.pack_forget()
            for widget in add_frame.winfo_children():
                widget.destroy()


def tab_selected(event) -> None:
    """
    The function show list of not yet added records to DB.

    :return: Show list of not yet added recipe
    :rtype: None
    """
    obj_automatic_updates = AutomaticUpdates()

    if event.widget.tab(event.widget.select(), "text") == " --- Add --- ":
        add_frame.pack(expand=1, fill="both", padx=10, pady=10)
        obj_automatic_updates.bildGrid()

        for record in range(len(obj_automatic_updates.dicRecipe)):
            radio_box = ttk.Radiobutton(
                add_frame,
                text=f"{obj_automatic_updates.dicRecipe.get(record).get('device')} - "
                f"{obj_automatic_updates.dicRecipe.get(record).get('recipe')} "
                f"    [ {obj_automatic_updates.dicRecipe.get(record).get('boardQty')} ] - "
                f"Cycle Time: {obj_automatic_updates.dicRecipe.get(record).get('cycleTime')} s.",
                style="AutomaticInsert.TRadiobutton",
                variable=var_new_record,
                value=int(record),
                command=automatic_insert,
            )
            radio_box.grid(row=int(record), column=0, sticky=W)
        radio_box.invoke()


def tab_selected_comparison(event) -> None:
    """
    The function remove unnecessary tabs.

    :return: Show only selected tabs
    :rtype: None
     """
    if event.widget.tab(event.widget.select(), "text") == " V810-3163 ":
        db_to_v810.hide(tab_3483S2EX_to_db)
        db_to_v810.hide(tab_db_to_3483S2EX)
        db_to_v810.hide(tab_3553S2EX_to_db)
        db_to_v810.hide(tab_db_to_3553S2EX)
        db_to_v810.hide(tab_8120S2_to_db)
        db_to_v810.hide(tab_db_to_8120S2)

        if event.widget.tab(event.widget.select(), "text") != "[3163] V810 to DB":
            db_to_v810.add(tab_3163_to_db, text="[3163] V810 to DB")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

            db_to_v810.add(tab_db_to_3163, text="[3163] DB to V810")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

    if event.widget.tab(event.widget.select(), "text") == " V810-3483S2EX ":
        db_to_v810.hide(tab_3163_to_db)
        db_to_v810.hide(tab_db_to_3163)
        db_to_v810.hide(tab_3553S2EX_to_db)
        db_to_v810.hide(tab_db_to_3553S2EX)
        db_to_v810.hide(tab_8120S2_to_db)
        db_to_v810.hide(tab_db_to_8120S2)

        if event.widget.tab(event.widget.select(), "text") != "[3483] V810 to DB":

            db_to_v810.add(tab_3483S2EX_to_db, text="[3483] V810 to DB")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

            db_to_v810.add(tab_db_to_3483S2EX, text="[3483] DB to V810")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

    if event.widget.tab(event.widget.select(), "text") == " V810-3553S2EX ":
        db_to_v810.hide(tab_3163_to_db)
        db_to_v810.hide(tab_db_to_3163)
        db_to_v810.hide(tab_3483S2EX_to_db)
        db_to_v810.hide(tab_db_to_3483S2EX)
        db_to_v810.hide(tab_8120S2_to_db)
        db_to_v810.hide(tab_db_to_8120S2)

        if event.widget.tab(event.widget.select(), "text") != "[3553] V810 to DB":

            db_to_v810.add(tab_3553S2EX_to_db, text="[3553] V810 to DB")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

            db_to_v810.add(tab_db_to_3553S2EX, text="[3553] DB to V810")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

    if event.widget.tab(event.widget.select(), "text") == " V810-8120S2 ":
        db_to_v810.hide(tab_3163_to_db)
        db_to_v810.hide(tab_db_to_3163)
        db_to_v810.hide(tab_3483S2EX_to_db)
        db_to_v810.hide(tab_db_to_3483S2EX)
        db_to_v810.hide(tab_3553S2EX_to_db)
        db_to_v810.hide(tab_db_to_3553S2EX)

        if event.widget.tab(event.widget.select(), "text") != "[3553] V810 to DB":

            db_to_v810.add(tab_8120S2_to_db, text="[8120] V810 to DB")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)

            db_to_v810.add(tab_db_to_8120S2, text="[8120] DB to V810")
            db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)


if __name__ == "__main__":
    root = tk.Tk()

    v = StringVar(root, "0")
    v0 = StringVar(root, "0")
    extract_set: dict = {}
    extract_set0: dict = {}

    obj_config = Config()
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = ws - int(obj_config.screenWidth)
    y = hs - int(obj_config.screenHeight)
    window_position = f"{int(obj_config.screenWidth)}x{int(obj_config.screenHeight)}+{int(x)}+{int(y)}"
    root.title(obj_config.title)
    root.geometry(window_position)
    # root.resizable(0, 0)
    # root.iconbitmap(obj_config.ico) # Icon for Win
    photo = PhotoImage(file=obj_config.ico)  # Icon for Linux
    root.iconphoto(False, photo)  # Incon for Linux

    root.configure(background=obj_config.bgColor)

    # --- Main View ---
    main_frame_view = ttk.LabelFrame(root, text=" Main View ")
    main_frame_view.pack(expand=1, fill="both", padx=10, pady=10)

    l_item = Label(main_frame_view, text=f"", bg="#333333", fg="#999999", pady="1")
    l_item.config(font=("Arial", 12, "bold"))
    l_item.grid(row=0, column=0, sticky=W)
    l_item_amount = Label(
        main_frame_view, text=f"", bg="#333333", fg="#999999", pady="1"
    )
    l_item_amount.config(font=("Arial", 12, "bold"))
    l_item_amount.grid(row=0, column=2, sticky=W)
    l_qty = Label(main_frame_view, text=f"", bg="#333333", fg="#555555", pady="2")
    l_qty.config(font=("Arial", 10))
    l_qty.grid(row=0, column=1, sticky=E)
    l_date = Label(main_frame_view, text=f"", bg="#333333", fg="#555555", pady="2")
    l_date.config(font=("Arial", 10))
    l_date.grid(row=0, column=3, sticky=W)
    l_date_db = Label(main_frame_view, text=f"", bg="#333333", fg="#999999", pady="2")
    l_date_db.config(font=("Arial", 10))
    l_date_db.grid(row=0, column=4, sticky=W)

    tab_control_main = ttk.Notebook(main_frame_view)

    # --- V849 & V817 section ---
    tab_main1 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main1, text=" V849 ")

    l_v849_prog = Label(tab_main1, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    l_v849_prog.configure(font=("Arial", 10))
    l_v849_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v849_scan_time_l = Label(
        tab_main1, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v849_scan_time_l.configure(font=("Arial", 10))
    l_v849_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v849_scan_time = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_scan_time.configure(font=("Arial", 10))
    l_v849_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v849_uph85_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_uph85_l.configure(font=("Arial", 10))
    l_v849_uph85_l.grid(row=2, column=0, sticky=E)
    l_v849_uph_85 = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_uph_85.configure(font=("Arial", 10))
    l_v849_uph_85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v849_uph95_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_uph95_l.configure(font=("Arial", 10))
    l_v849_uph95_l.grid(row=3, column=0, sticky=E)
    l_v849_uph_95 = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_uph_95.configure(font=("Arial", 10))
    l_v849_uph_95.grid(row=3, column=1, columnspan=5, sticky=W)

    l_v849_baan_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_baan_l.configure(font=("Arial", 10))
    l_v849_baan_l.grid(row=4, column=0, sticky=E)
    l_v849_baan = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_baan.configure(font=("Arial", 10))
    l_v849_baan.grid(row=4, column=1, sticky=W)

    l_v849_lc_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_lc_l.configure(font=("Arial", 10))
    l_v849_lc_l.grid(row=4, column=2, sticky=E)
    l_V849_lc = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_V849_lc.configure(font=("Arial", 10))
    l_V849_lc.grid(row=4, column=3, sticky=W)

    l_v849_epi_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_epi_l.configure(font=("Arial", 10))
    l_v849_epi_l.grid(row=4, column=4, sticky=E)
    l_v849_epi = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_epi.configure(font=("Arial", 10))
    l_v849_epi.grid(row=4, column=5, sticky=W)

    l_v849_comment_l = Label(tab_main1, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v849_comment_l.configure(font=("Arial", 10))
    l_v849_comment_l.grid(row=5, column=0, sticky=E)
    l_v849_comment = Label(tab_main1, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v849_comment.configure(font=("Arial", 10, "italic"))
    l_v849_comment.grid(row=5, column=1, columnspan=5, sticky=W)

    tab_main2 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main2, text=" V817 ")

    l_v817_prog = Label(tab_main2, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    l_v817_prog.configure(font=("Arial", 10))
    l_v817_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v817_scan_time_l = Label(
        tab_main2, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v817_scan_time_l.configure(font=("Arial", 10))
    l_v817_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v817_scan_time = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_scan_time.configure(font=("Arial", 10))
    l_v817_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v817_uph85_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_uph85_l.configure(font=("Arial", 10))
    l_v817_uph85_l.grid(row=2, column=0, sticky=E)
    l_v817_uph85 = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_uph85.configure(font=("Arial", 10))
    l_v817_uph85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v817_uph95_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_uph95_l.configure(font=("Arial", 10))
    l_v817_uph95_l.grid(row=3, column=0, sticky=E)
    l_v817_uph95 = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_uph95.configure(font=("Arial", 10))
    l_v817_uph95.grid(row=3, column=1, columnspan=5, sticky=W)

    l_v817_baan_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_baan_l.configure(font=("Arial", 10))
    l_v817_baan_l.grid(row=4, column=0, sticky=E)
    l_v817_baan = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_baan.configure(font=("Arial", 10))
    l_v817_baan.grid(row=4, column=1, sticky=W)

    l_v817_lc_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_lc_l.configure(font=("Arial", 10))
    l_v817_lc_l.grid(row=4, column=2, sticky=E)
    l_v817_lc = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_lc.configure(font=("Arial", 10))
    l_v817_lc.grid(row=4, column=3, sticky=W)

    l_v817_epi_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_epi_l.configure(font=("Arial", 10))
    l_v817_epi_l.grid(row=4, column=4, sticky=E)
    l_v817_epi = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_epi.configure(font=("Arial", 10))
    l_v817_epi.grid(row=4, column=5, sticky=W)

    l_v817_comment_l = Label(tab_main2, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v817_comment_l.configure(font=("Arial", 10))
    l_v817_comment_l.grid(row=5, column=0, sticky=E)
    l_v817_comment = Label(tab_main2, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v817_comment.configure(font=("Arial", 10, "italic"))
    l_v817_comment.grid(row=5, column=1, columnspan=5, sticky=W)
    # --- The End of V849 & V817 section ---

    # --- V810-3163 section ---
    tab_main3 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main3, text=" V810-3163 ")

    l_v8103163_prog = Label(tab_main3, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    l_v8103163_prog.configure(font=("Arial", 10))
    l_v8103163_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v8103163_scan_time_l = Label(
        tab_main3, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103163_scan_time_l.configure(font=("Arial", 10))
    l_v8103163_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v8103163_scan_time = Label(
        tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103163_scan_time.configure(font=("Arial", 10))
    l_v8103163_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v8103163_uph85_l = Label(
        tab_main3, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103163_uph85_l.configure(font=("Arial", 10))
    l_v8103163_uph85_l.grid(row=2, column=0, sticky=E)
    l_v8103163_uph85 = Label(tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103163_uph85.configure(font=("Arial", 10))
    l_v8103163_uph85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v8103163_uph95_l = Label(
        tab_main3, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103163_uph95_l.configure(font=("Arial", 10))
    l_v8103163_uph95_l.grid(row=3, column=0, sticky=E)
    l_v8103163_uph95 = Label(tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103163_uph95.configure(font=("Arial", 10))
    l_v8103163_uph95.grid(row=3, column=1, columnspan=5, sticky=W)

    l_v8103163_baan_l = Label(tab_main3, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v8103163_baan_l.configure(font=("Arial", 10))
    l_v8103163_baan_l.grid(row=4, column=0, sticky=E)
    l_v8103163_baan = Label(tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103163_baan.configure(font=("Arial", 10))
    l_v8103163_baan.grid(row=4, column=1, sticky=W)

    l_v8103163_lc_l = Label(tab_main3, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v8103163_lc_l.configure(font=("Arial", 10))
    l_v8103163_lc_l.grid(row=4, column=2, sticky=E)
    l_v8103163_lc = Label(tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103163_lc.configure(font=("Arial", 10))
    l_v8103163_lc.grid(row=4, column=3, sticky=W)

    l_v8103163_epi_l = Label(tab_main3, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v8103163_epi_l.configure(font=("Arial", 10))
    l_v8103163_epi_l.grid(row=4, column=4, sticky=E)
    l_v8103163_epi = Label(tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103163_epi.configure(font=("Arial", 10))
    l_v8103163_epi.grid(row=4, column=5, sticky=W)

    l_v8103163_comment_l = Label(
        tab_main3, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103163_comment_l.configure(font=("Arial", 10))
    l_v8103163_comment_l.grid(row=5, column=0, sticky=E)
    l_v8103163_comment = Label(
        tab_main3, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103163_comment.configure(font=("Arial", 10, "italic"))
    l_v8103163_comment.grid(row=5, column=1, columnspan=5, sticky=W)
    # --- The End of V810-3163 section ---

    # --- V810-3483S2EX section ---
    tab_main4 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main4, text=" V810-3483S2EX ")

    l_v8103483s2ex_prog = Label(
        tab_main4, text=f"", bg="#444444", fg="#FFFFFF", pady="1"
    )
    l_v8103483s2ex_prog.configure(font=("Arial", 10))
    l_v8103483s2ex_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v8103483s2ex_scan_time_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_scan_time_l.configure(font=("Arial", 10))
    l_v8103483s2ex_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v8103483s2ex_scan_time = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_scan_time.configure(font=("Arial", 10))
    l_v8103483s2ex_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v8103483s2ex_uph85_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_uph85_l.configure(font=("Arial", 10))
    l_v8103483s2ex_uph85_l.grid(row=2, column=0, sticky=E)
    l_v8103483s2ex_uph85 = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_uph85.configure(font=("Arial", 10))
    l_v8103483s2ex_uph85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v8103483s2ex_uph95_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_uph95_l.configure(font=("Arial", 10))
    l_v8103483s2ex_uph95_l.grid(row=3, column=0, sticky=E)
    l_v8103483s2ex_uph95 = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_uph95.configure(font=("Arial", 10))
    l_v8103483s2ex_uph95.grid(row=3, column=1, columnspan=5, sticky=W)

    L_v8103483s2_ex_baan_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    L_v8103483s2_ex_baan_l.configure(font=("Arial", 10))
    L_v8103483s2_ex_baan_l.grid(row=4, column=0, sticky=E)
    l_v8103483s2ex_baan = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_baan.configure(font=("Arial", 10))
    l_v8103483s2ex_baan.grid(row=4, column=1, sticky=W)

    l_v8103483s2ex_lc_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_lc_l.configure(font=("Arial", 10))
    l_v8103483s2ex_lc_l.grid(row=4, column=2, sticky=E)
    l_v8103483s2ex_lc = Label(tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103483s2ex_lc.configure(font=("Arial", 10))
    l_v8103483s2ex_lc.grid(row=4, column=3, sticky=W)

    l_v8103483s2ex_epi_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_epi_l.configure(font=("Arial", 10))
    l_v8103483s2ex_epi_l.grid(row=4, column=4, sticky=E)
    l_v8103483s2ex_epi = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_epi.configure(font=("Arial", 10))
    l_v8103483s2ex_epi.grid(row=4, column=5, sticky=W)

    l_v8103483s2ex_comment_l = Label(
        tab_main4, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103483s2ex_comment_l.configure(font=("Arial", 10))
    l_v8103483s2ex_comment_l.grid(row=5, column=0, sticky=E)
    l_v8103483s2ex_comment = Label(
        tab_main4, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103483s2ex_comment.configure(font=("Arial", 10, "italic"))
    l_v8103483s2ex_comment.grid(row=5, column=1, columnspan=5, sticky=W)
    # --- The Ebd V810-3483S2EX section ---

    # --- V810-355532EX section ---
    tab_main5 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main5, text=" V810-355532EX ")

    l_v8103553s2ex_prog = Label(
        tab_main5, text=f"", bg="#444444", fg="#FFFFFF", pady="1"
    )
    l_v8103553s2ex_prog.configure(font=("Arial", 10))
    l_v8103553s2ex_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v8103553s2ex_scan_time_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_scan_time_l.configure(font=("Arial", 10))
    l_v8103553s2ex_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v8103553s2ex_scan_time = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_scan_time.configure(font=("Arial", 10))
    l_v8103553s2ex_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v8103553s2ex_uph85_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_uph85_l.configure(font=("Arial", 10))
    l_v8103553s2ex_uph85_l.grid(row=2, column=0, sticky=E)
    l_v8103553s2ex_uph85 = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_uph85.configure(font=("Arial", 10))
    l_v8103553s2ex_uph85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v8103553s2ex_uph95_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_uph95_l.configure(font=("Arial", 10))
    l_v8103553s2ex_uph95_l.grid(row=3, column=0, sticky=E)
    l_v8103553s2ex_uph95 = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_uph95.configure(font=("Arial", 10))
    l_v8103553s2ex_uph95.grid(row=3, column=1, columnspan=5, sticky=W)

    l_v8103553s2ex_baan_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_baan_l.configure(font=("Arial", 10))
    l_v8103553s2ex_baan_l.grid(row=4, column=0, sticky=E)
    l_v8103553s2ex_baan = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_baan.configure(font=("Arial", 10))
    l_v8103553s2ex_baan.grid(row=4, column=1, sticky=W)

    l_v8103553s2ex_lc_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_lc_l.configure(font=("Arial", 10))
    l_v8103553s2ex_lc_l.grid(row=4, column=2, sticky=E)
    l_v8103553s2ex_lc = Label(tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8103553s2ex_lc.configure(font=("Arial", 10))
    l_v8103553s2ex_lc.grid(row=4, column=3, sticky=W)

    l_v8103553s2ex_epi_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_epi_l.configure(font=("Arial", 10))
    l_v8103553s2ex_epi_l.grid(row=4, column=4, sticky=E)
    l_v8103553s2ex_epi = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_epi.configure(font=("Arial", 10))
    l_v8103553s2ex_epi.grid(row=4, column=5, sticky=W)

    l_v8103553s2ex_comment_l = Label(
        tab_main5, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8103553s2ex_comment_l.configure(font=("Arial", 10))
    l_v8103553s2ex_comment_l.grid(row=5, column=0, sticky=E)
    l_v8103553s2ex_comment = Label(
        tab_main5, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8103553s2ex_comment.configure(font=("Arial", 10, "italic"))
    l_v8103553s2ex_comment.grid(row=5, column=1, columnspan=5, sticky=W)
    # --- The End V810-355532EX section ---
    # --- V810-81202 section ---
    tab_main6 = ttk.Frame(tab_control_main)
    tab_control_main.add(tab_main6, text=" V810-8120S2 ")

    l_v8108120s2_prog = Label(tab_main6, text=f"", bg="#444444", fg="#FFFFFF", pady="1")
    l_v8108120s2_prog.configure(font=("Arial", 10))
    l_v8108120s2_prog.grid(row=0, column=0, columnspan=6, sticky=W)

    l_v8108120s2_scan_time_l = Label(
        tab_main6, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8108120s2_scan_time_l.configure(font=("Arial", 10))
    l_v8108120s2_scan_time_l.grid(row=1, column=0, sticky=E)
    l_v8108120s2_scan_time = Label(
        tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8108120s2_scan_time.configure(font=("Arial", 10))
    l_v8108120s2_scan_time.grid(row=1, column=1, columnspan=5, sticky=W)

    l_v8108120s2_uph85_l = Label(
        tab_main6, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8108120s2_uph85_l.configure(font=("Arial", 10))
    l_v8108120s2_uph85_l.grid(row=2, column=0, sticky=E)
    l_v8108120s2_uph85 = Label(
        tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8108120s2_uph85.configure(font=("Arial", 10))
    l_v8108120s2_uph85.grid(row=2, column=1, columnspan=5, sticky=W)
    l_v8108120s2_uph95_l = Label(
        tab_main6, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8108120s2_uph95_l.configure(font=("Arial", 10))
    l_v8108120s2_uph95_l.grid(row=3, column=0, sticky=E)
    l_v8108120s2uph95 = Label(tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8108120s2uph95.configure(font=("Arial", 10))
    l_v8108120s2uph95.grid(row=3, column=1, columnspan=5, sticky=W)

    l_v8108120s2_baan_l = Label(
        tab_main6, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8108120s2_baan_l.configure(font=("Arial", 10))
    l_v8108120s2_baan_l.grid(row=4, column=0, sticky=E)
    l_v8108120s2_baan = Label(tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8108120s2_baan.configure(font=("Arial", 10))
    l_v8108120s2_baan.grid(row=4, column=1, sticky=W)

    l_v8108120s2lc_l = Label(tab_main6, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v8108120s2lc_l.configure(font=("Arial", 10))
    l_v8108120s2lc_l.grid(row=4, column=2, sticky=E)
    l_v8108120s2_lc = Label(tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8108120s2_lc.configure(font=("Arial", 10))
    l_v8108120s2_lc.grid(row=4, column=3, sticky=W)

    l_v8108120s2epi_l = Label(tab_main6, text=f"", bg="#444444", fg="#666666", pady="1")
    l_v8108120s2epi_l.configure(font=("Arial", 10))
    l_v8108120s2epi_l.grid(row=4, column=4, sticky=E)
    l_v8108120s2_epi = Label(tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1")
    l_v8108120s2_epi.configure(font=("Arial", 10))
    l_v8108120s2_epi.grid(row=4, column=5, sticky=W)

    l_v8108120s2comment_l = Label(
        tab_main6, text=f"", bg="#444444", fg="#666666", pady="1"
    )
    l_v8108120s2comment_l.configure(font=("Arial", 10))
    l_v8108120s2comment_l.grid(row=5, column=0, sticky=E)
    l_v8108120s2_comment = Label(
        tab_main6, text=f"", bg="#444444", fg="#AAAAAA", pady="1"
    )
    l_v8108120s2_comment.configure(font=("Arial", 10))
    l_v8108120s2_comment.grid(row=5, column=1, columnspan=5, sticky=W)
    # --- The End V810-81202 section ---

    tab_control_main.grid(row=1, column=0, columnspan=5, sticky=W)

# ------------------- The End Main View ----------------------------

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text=" --- Main --- ")
    tab_control.pack(expand=1, fill="both", padx=10, pady=10)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text=" --- New --- ")
    tab_control.pack(expand=1, fill="both", padx=10, pady=10)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text=" --- Add --- ")
    tab_control.pack(expand=1, fill="both", padx=10, pady=10)
    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab4, text=" --- Comparison --- ")
    tab_control.pack(expand=1, fill="both", padx=10, pady=10)

    tab_control.bind("<<NotebookTabChanged>>", tab_selected)

    add_frame = ttk.LabelFrame(tab3, text=" New Items: ")

# --- Comparison ---
    v810_device = ttk.Notebook(tab4)

    tab_3163 = ttk.Frame(v810_device)
    v810_device.add(tab_3163, text=" V810-3163 ")
    v810_device.pack(expand=1, fill="both", padx=10, pady=10)


    tab_3483S2EX = ttk.Frame(v810_device)
    v810_device.add(tab_3483S2EX, text=" V810-3483S2EX ")
    v810_device.pack(expand=1, fill="both", padx=10, pady=10)

    tab_3553S2EX = ttk.Frame(v810_device)
    v810_device.add(tab_3553S2EX, text=" V810-3553S2EX ")
    v810_device.pack(expand=1, fill="both", padx=10, pady=10)

    tab_8120S2 = ttk.Frame(v810_device)
    v810_device.add(tab_8120S2, text=" V810-8120S2 ")
    v810_device.pack(expand=1, fill="both", padx=10, pady=10)

    v810_device.bind("<<NotebookTabChanged>>", tab_selected_comparison)

    db_to_v810 = ttk.Notebook(v810_device)

    obj_comparison = ComparisonView(
        dir_name=obj_config.pathImgV8103163,
        db_name="VITROXI_PROG",
        root=root
    )
    tab_3163_to_db = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_3163_to_db, text="[3163] V810 to DB")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_list_to_db(tab=tab_3163_to_db)

    tab_db_to_3163 = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_db_to_3163, text="[3163] DB to V810")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_db_to_list(tab=tab_db_to_3163)

    obj_comparison = ComparisonView(
        dir_name=obj_config.pathImgV8103483S2EX,
        db_name="VITROXIII_PROG",
        root=root
    )


    tab_3483S2EX_to_db = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_3483S2EX_to_db, text="[3483] V810 to DB")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_list_to_db(tab=tab_3483S2EX_to_db)

    tab_db_to_3483S2EX = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_db_to_3483S2EX, text="[3483] DB to V810")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_db_to_list(tab=tab_db_to_3483S2EX)

    obj_comparison = ComparisonView(
        dir_name=obj_config.pathImgV8103553S2EX,
        db_name="VITROXIV_PROG",
        root=root
    )

    tab_3553S2EX_to_db = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_3553S2EX_to_db, text="[3553] V810 to DB")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_list_to_db(tab=tab_3553S2EX_to_db)

    tab_db_to_3553S2EX = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_db_to_3553S2EX, text="[3553] DB to V810")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_db_to_list(tab=tab_db_to_3553S2EX)

    obj_comparison = ComparisonView(
        dir_name=obj_config.pathImgV8108120S2,
        db_name="VITROXII_PROG",
        root=root
    )

    tab_8120S2_to_db = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_8120S2_to_db, text="[8120] V810 to DB")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_list_to_db(tab=tab_8120S2_to_db)

    tab_db_to_8120S2 = ttk.Frame(db_to_v810)
    db_to_v810.add(tab_db_to_8120S2, text="[8120] DB to V810")
    db_to_v810.pack(expand=1, fill="both", padx=25, pady=25)
    obj_comparison.compare_db_to_list(tab=tab_db_to_8120S2)

# --- The End Comparison ---

    var_new_record = IntVar()

    obj_styles = Styles(root)

# --- INSERT ---

    obj_new_item_ex = NewItem(tab2, root)
    obj_new_item_ex.main_frame_insert(" Insert Main ")

    obj_new_item_ex.checkbox_title(" ViTrox Ex ", 4)
    obj_checkbox_menu_ex_3163 = CheckboxMenu(
        tab2, root, obj_new_item_ex.checkbox_frame, f"{obj_config.machines[5]}",
    )
    obj_checkbox_menu_ex_3163.checkboxMenu(f"{obj_config.devices[2]}", 1)

    obj_checkbox_menu_ex_3483s2 = CheckboxMenu(
        tab2, root, obj_new_item_ex.checkbox_frame, f"{obj_config.machines[3]}",
    )
    obj_checkbox_menu_ex_3483s2.checkboxMenu(f"{obj_config.devices[1]}", 2)

    obj_checkbox_menu_ex_3553s2 = CheckboxMenu(
        tab2, root, obj_new_item_ex.checkbox_frame, f"{obj_config.machines[2]}",
    )
    obj_checkbox_menu_ex_3553s2.checkboxMenu(f"{obj_config.devices[0]}", 3)

    objNewItemXXL = NewItem(tab2, root)
    objNewItemXXL.checkbox_title(" ViTrox XXL ", 5)

    obj_checkbox_menu_xxl_8120s2 = CheckboxMenu(
        tab2, root, objNewItemXXL.checkbox_frame, f"{obj_config.machines[3]}",
    )
    obj_checkbox_menu_xxl_8120s2.checkboxMenu(f"{obj_config.devices[3]}", 1)

    objNewItem5DX = NewItem(tab2, root)
    objNewItem5DX.checkbox_title(" 5DX ", 6)

    obj_checkbox_menu_5dx_v849 = CheckboxMenu(
        tab2, root, objNewItem5DX.checkbox_frame, f"{obj_config.machines[0]}"
    )
    obj_checkbox_menu_5dx_v849.checkboxMenu(f"{obj_config.devices[5]}", 1)
    obj_checkbox_menu_5dx_v849.alignmentTime()

    obj_checkbox_menu_5dx_v817 = CheckboxMenu(
        tab2, root, objNewItem5DX.checkbox_frame, f" {obj_config.machines[1]} "
    )
    obj_checkbox_menu_5dx_v817.checkboxMenu(f"{obj_config.devices[4]}", 2)
    obj_checkbox_menu_5dx_v817.alignmentTime()

    button_insert = ttk.Button(
        obj_new_item_ex.main_frame,
        text="Insert",
        width=35,
        command=insert_button,
        cursor="hand2",
    )
    button_insert.grid(row=1, column=0, columnspan=2, pady=2)
    button_reset = ttk.Button(
        obj_new_item_ex.main_frame,
        text="Reset",
        width=15,
        command=reset,
        cursor="hand2",
    )
    button_reset.grid(row=1, column=2, columnspan=2, pady=2)
# --- The End INSERT ---

# --- TreeView column & heading customize ---
    tree = ttk.Treeview(tab1)

    tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
    tree.column("#0", width=20, minwidth=20, stretch=tk.NO)
    tree.column("one", width=45, minwidth=45, stretch=tk.NO)
    tree.column("two", width=275, minwidth=190, stretch=tk.NO)
    tree.column("three", width=150, minwidth=130, stretch=tk.NO)
    tree.column("four", width=35, minwidth=30, stretch=tk.NO)
    tree.column("five", width=40, minwidth=30, stretch=tk.NO)
    tree.column("six", width=40, minwidth=30, stretch=tk.NO)
    tree.column("seven", width=40, minwidth=30, stretch=tk.NO)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("one", text="ID", anchor=tk.W)
    tree.heading("two", text="Item", anchor=tk.W)
    tree.heading("three", text="Date / Time", anchor=tk.W)
    tree.heading("four", text="Qty", anchor=tk.W)
    tree.heading("five", text="BaaN", anchor=tk.W)
    tree.heading("six", text="LC", anchor=tk.W)
    tree.heading("seven", text="EPI", anchor=tk.W)
# --- The End TreeView column & heading customize ---

# --- Search ---
    obj_search = ContextualMenu(root, "0", True, True, False)
    e_search = Entry(
        tab1,
        relief="solid",
        textvariable=obj_search.captureEntry,
        borderwidth=1,
        width=55,
        bg="#212121",
        fg="#FFFFFF",
    )
    e_search.config(
        font=("Arial", 10), highlightbackground="#000000", highlightcolor="#33FFBE"
    )
    e_search.grid(row=0, column=0, pady=1)
    e_search.bind("<Button-3>", obj_search.do_popup)
    root.bind("<Button-1>", obj_search.release_contextual_menu)
    obj_search.set_entry(e_search)

    obj_search_phrase = Search(tree, e_search)
    b_search = ttk.Button(tab1, text="Search", width=10, command=obj_search_phrase.search_phrase, cursor="hand2")
    b_search.grid(row=0, column=1, pady=1)
    b_search_r = ttk.Button(
        tab1, text="Refresh", width=10, command=refresh, cursor="exchange"
    )
    b_search_r.grid(row=0, column=2, pady=1)
# --- The End Search ---

    refresh()
    root.mainloop()
