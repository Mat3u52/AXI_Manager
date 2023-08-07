from tkinter import Label, W, END, E, IntVar, Entry, ttk, messagebox, PhotoImage, Button, StringVar
from DBConnect import DBConnect

class Refresh:
    def __init__(self, tree: ttk) -> None:
        self.tree = tree

    def refresh(self) -> None:
        """
        The function returns the table to the default shape. Show all record from DB.

        :return: Show all records in table from DB
        :rtype: None
        """
        self.tree.selection_clear()
        self.tree.selection_remove(self.tree.focus())
        # e_search.delete(0, END)
        for record in self.tree.get_children():
            self.tree.delete(record)

        obj_db = DBConnect()

        # ---Create striped row tags---
        self.tree.tag_configure("DX", background="#222222")
        self.tree.tag_configure("V", background="#333333")
        self.tree.tag_configure("one", background="#111111")
        self.tree.tag_configure("baan", background="#111111", foreground="#EB0E0E")
        self.tree.tag_configure("baan0", foreground="#EB0E0E")
        # ---The End Create striped row---

        count = 1
        count1 = 1
        count2 = 0

        for row in obj_db.selectAll():
            if count % 2 == 0:
                if (
                    (
                        row[11] != "YES"
                        and row[11] != "NONE"
                        and row[11] is not None
                        and (row[11] == "NO" or row[11] == "LACK")
                    )
                    or (
                        row[16] != "YES"
                        and row[16] != "NONE"
                        and row[16] is not None
                        and (row[16] == "NO" or row[16] == "LACK")
                    )
                    or (
                        row[38] != "YES"
                        and row[38] != "NONE"
                        and row[38] is not None
                        and (row[38] == "NO" or row[38] == "LACK")
                    )
                    or (
                        row[44] != "YES"
                        and row[44] != "NONE"
                        and row[44] is not None
                        and (row[44] == "NO" or row[44] == "LACK")
                    )
                    or (
                        row[53] != "YES"
                        and row[53] != "NONE"
                        and row[53] is not None
                        and (row[53] == "NO" or row[53] == "LACK")
                    )
                ):
                    folder1 = self.tree.insert(
                        parent="",
                        index=count,
                        iid=count1,
                        text=f"box",
                        values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                        tag="baan",
                    )
                else:
                    folder1 = self.tree.insert(
                        parent="",
                        index=count,
                        iid=count1,
                        text=f"box",
                        values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                        tag="one",
                    )
            else:
                if (
                    (
                        row[11] != "YES"
                        and row[11] != "NONE"
                        and row[11] is not None
                        and (row[11] == "NO" or row[11] == "LACK")
                    )
                    or (
                        row[16] != "YES"
                        and row[16] != "NONE"
                        and row[16] is not None
                        and (row[16] == "NO" or row[16] == "LACK")
                    )
                    or (
                        row[38] != "YES"
                        and row[38] != "NONE"
                        and row[38] is not None
                        and (row[38] == "NO" or row[38] == "LACK")
                    )
                    or (
                        row[44] != "YES"
                        and row[44] != "NONE"
                        and row[44] is not None
                        and (row[44] == "NO" or row[44] == "LACK")
                    )
                    or (
                        row[53] != "YES"
                        and row[53] != "NONE"
                        and row[53] is not None
                        and (row[53] == "NO" or row[53] == "LACK")
                    )
                ):
                    folder1 = self.tree.insert(
                        parent="",
                        index=count,
                        iid=count1,
                        text=f"box",
                        values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                        tag="baan0",
                    )
                else:
                    folder1 = self.tree.insert(
                        parent="",
                        index=count,
                        iid=str(count1),
                        text=f"box",
                        values=(f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}"),
                    )
            count1 += 1
            if int(len(str(row[17]))) > 4:
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"5DX I",
                        f"85%: {row[4]}, 95%: {row[6]}",
                        "",
                        f"{row[11]}",
                        f"{row[18]}",
                        f"{row[19]}",
                    ),
                    tags="DX",
                )
            count1 += 2
            if int(len(str(row[22]))) > 4:
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"5DX II",
                        f"85%: {row[4]}, 95%: {row[6]}",
                        "",
                        f"{row[11]}",
                        f"{row[23]}",
                        f"{row[24]}",
                    ),
                    tags="DX",
                )
            count1 += 3

            if row[27] is not None and (
                (int(row[15]) != 0 or int(row[14]) != 0) or int(row[12])
            ):
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"ViTrox Ex I",
                        f"85%: {row[12]}, 95%: {row[14]}",
                        "",
                        f"{row[16]}",
                        f"{row[28]}",
                        f"{row[29]}",
                    ),
                    tags="V",
                )
            count1 += 4

            if row[45] is not None and (
                (row[43] is not None and int(row[43]) > 0) or int(row[40])
            ):
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"ViTrox Ex II",
                        f"85%: {row[40]}, 95%: {row[42]}",
                        "",
                        f"{row[44]}",
                        f"{row[46]}",
                        f"{row[47]}",
                    ),
                    tags="V",
                )
            count1 += 4

            if row[54] is not None and (
                (row[52] is not None and int(row[52]) > 0) or int(row[49])
            ):
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"ViTrox Ex III",
                        f"85%: {row[49]}, 95%: {row[51]}",
                        "",
                        f"{row[53]}",
                        f"{row[55]}",
                        f"{row[56]}",
                    ),
                    tags="V",
                )
            count1 += 5

            if row[31] is not None and (
                (row[37] is not None and int(row[37]) > 0) or int(row[39])
            ):
                self.tree.insert(
                    folder1,
                    index="end",
                    iid=str(count1),
                    text=f"",
                    values=(
                        f"{row[0]}",
                        f"ViTrox XXL I",
                        f"85%: {row[39]}, 95%: {row[36]}",
                        "",
                        f"{row[38]}",
                        f"{row[32]}",
                        f"{row[33]}",
                    ),
                    tags="V",
                )

            # self.tree.bind("<<TreeviewSelect>>", get_selected_row)

            self.tree.grid(row=1, column=0, columnspan=3, pady=2)
            count += 1
            count1 += 1
            count2 += 1

        obj_db.closeDB()


    # # ---Scrollbar--------------
    #     vsb = ttk.Scrollbar(tab1, orient="vertical", command=self.tree.yview)
    #     vsb.place(
    #         x=obj_config.scrollX, y=obj_config.scrollY, height=obj_config.scrollHeight
    #     )
    #     self.tree.configure(yscrollcommand=vsb.set)
    #
    #
    # # ---The End of Scrollbar---