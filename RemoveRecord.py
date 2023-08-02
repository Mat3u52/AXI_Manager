import os
import tkinter as tk
from tkinter import messagebox
from DBConnect import DBConnect
from Config import Config


class RemoveRecord(DBConnect):
    
    def __init__(self, id_record: str) -> None:
        super().__init__()
        self.id_record: str = str(id_record)

    def remove_total(self) -> None:
        msg_box = tk.messagebox.askquestion('Remove Record',
                                            'Are you sure you want to remove record?',
                                            icon='warning')
        if msg_box == 'yes':
            try:
                # print("removed")
                # print(self.selectSearchID(self.id_record)[0][1])

                dirs_and_files = os.listdir(Config().pathRecipe)

                for device in dirs_and_files:
                    # print(os.path.join(Config().pathRecipe, device))
                    container: set[str] = set(os.listdir(os.path.join(Config().pathRecipe, device)))
                    print(self.selectSearchID(self.id_record)[0][1].replace("/", "_"))
                    if self.selectSearchID(self.id_record)[0][1].replace("/", "_") + r".png" in container or \
                            self.selectSearchID(self.id_record)[0][1].replace("/", "_") + r".jpg" in container or \
                            self.selectSearchID(self.id_record)[0][1].replace("/", "_") + r".txt" in container:
                        print(f'exist')
                        print(self.selectSearchID(self.id_record)[0][1])
                        path = os.path.join(Config().pathRecipe, device)
                        try:  # .png
                            print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1]).replace('/', '_')}.png")
                            # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.png")
                        except FileNotFoundError:
                            print("The .png file does not exist!")
                        try:  # .jpg
                            print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1]).replace('/', '_')}.jpg")
                            # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.jpg")
                        except FileNotFoundError:
                            print("The .jpg file does not exist!")
                        try:  # .txt
                            print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1]).replace('/', '_')}.txt")
                            # os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.txt")
                        except FileNotFoundError:
                            print("The .txt file does not exist!")
                    else:
                        print('The .png or .jpg or .txt file does not exist!')

                # self.delete_by_id(self.id_record)

            except ValueError:
                print("Record in database does not exist!")
