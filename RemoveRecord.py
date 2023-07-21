import os
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
            # one_record = self.selectSearchID(self.id_record)
            # print(one_record[0][1])

            dirs_anf_files = os.listdir(Config().pathRecipe)
            for device in dirs_anf_files:
                container: set[str] = set()

                print(os.path.join(Config().pathRecipe, device))

        except:
            print("Record do not exist.")
