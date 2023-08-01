import os
import re
from DBConnect import DBConnect
from Config import Config


class RemoveRecord(DBConnect):
    
    def __init__(self, id_record: str) -> None:
        super().__init__()
        self.id_record: str = str(id_record)

    def remove_total(self):
        try:
            # self.delete_by_id(self.id_record)
            print("removed")
            print(self.selectSearchID(self.id_record)[0][1])

            dirs_and_files = os.listdir(Config().pathRecipe)

            for device in dirs_and_files:
                # print(os.path.join(Config().pathRecipe, device))
                container: set[str] = set(os.listdir(os.path.join(Config().pathRecipe, device)))

                if self.selectSearchID(self.id_record)[0][1] + r".png" in container or \
                        self.selectSearchID(self.id_record)[0][1] + r".jpg" in container or \
                        self.selectSearchID(self.id_record)[0][1] + r".txt" in container:
                    print(f'exist')
                    path = os.path.join(Config().pathRecipe, device)
                    try:  # .png
                        print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.png")
                        os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.png")
                    except FileNotFoundError:
                        print("The .png file does not exist!")
                    try:  # .jpg
                        print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.jpg")
                        os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.jpg")
                    except FileNotFoundError:
                        print("The .jpg file does not exist!")
                    try:  # .txt
                        print(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.txt")
                        os.remove(f"{os.path.join(path, self.selectSearchID(self.id_record)[0][1])}.txt")
                    except FileNotFoundError:
                        print("The .txt file does not exist!")
                else:
                    print('The .png or .jpg or .txt file does not exist!')

        except ValueError:
            print("Record in database does not exist!")
