import os
import tkinter as tk
from tkinter import messagebox
from DBConnect import DBConnect
from Config import Config


class RemoveRecord(DBConnect):
    flag: bool = False

    def __init__(self, id_record: str) -> None:
        super().__init__()
        self.id_record: str = str(id_record)

    def remove_total(self) -> bool:
        msg_box = tk.messagebox.askquestion('Remove Record',
                                            f'Are you sure you want to remove'
                                            f' {self.selectSearchID(self.id_record)[0][1]} '
                                            f'record?',
                                            icon='warning')
        if msg_box == 'yes':
            try:
                # print("removed")
                # print(self.selectSearchID(self.id_record)[0][1])

                dirs_and_files = os.listdir(Config().pathRecipe)

                recipes: tuple = (self.selectSearchID(self.id_record)[0][17],
                                  self.selectSearchID(self.id_record)[0][22],
                                  self.selectSearchID(self.id_record)[0][27],
                                  self.selectSearchID(self.id_record)[0][31],
                                  self.selectSearchID(self.id_record)[0][45],
                                  self.selectSearchID(self.id_record)[0][54])
                print(recipes)
                for device in dirs_and_files:
                    # print(os.path.join(Config().pathRecipe, device))
                    container: set[str] = set(os.listdir(os.path.join(Config().pathRecipe, device)))

                    for recipe in recipes:
                        if str(recipe) + r".png" in container or \
                                str(recipe) + r".jpg" in container or \
                                str(recipe) + r".txt" in container:
                            print(str(recipe))
                            path = os.path.join(Config().pathRecipe, device)
                            try:  # .png
                                print(f"{os.path.join(path, str(recipe))}.png")
                                # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.png")
                            except FileNotFoundError:
                                print("The .png file does not exist!")
                            try:  # .jpg
                                print(f"{os.path.join(path, str(recipe))}.jpg")
                                # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.jpg")
                            except FileNotFoundError:
                                print("The .jpg file does not exist!")
                            try:  # .txt
                                print(f"{os.path.join(path, str(recipe))}.txt")
                                # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.txt")
                            except FileNotFoundError:
                                print("The .txt file does not exist!")
                        else:
                            print('The .png or .jpg or .txt file does not exist!')

                # self.delete_by_id(self.id_record)
                RemoveRecord.flag = True
                return True
            except ValueError:
                print("Record in database does not exist!")
                return False
