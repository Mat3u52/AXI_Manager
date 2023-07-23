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
            # one_record = self.selectSearchID(self.id_record)
            # print(one_record[0][1])

            dirs_and_files = os.listdir(Config().pathRecipe)

            for device in dirs_and_files:
                # container: set[str] = set()
                print(os.path.join(Config().pathRecipe, device))
                container: set[str] = set(os.listdir(os.path.join(Config().pathRecipe, device)))

                # txt = "__test03.txt"
                # search_for = re.search(f"^{self.selectSearchID(self.id_record)[0][1]}....$", txt)
                # if search_for:
                #     print("yes")
                # else:
                #     print("no")
                test1 = "test"
                test = re.compile(r".(?:txt|jpeg|jpg|png)")
                print(type(test))
                str2 = "test.txt"
                result = test.findall(str2)
                print(result)
                if test1 + test is str2:
                    print('ok')
                # if test in container:
                #     print('exist')
                # else:
                #     print('not exist')
                # print(container)

                # if self.selectSearchID(self.id_record)[0][1] in container:
                #     print('exist')
                # else:
                #     print('not exist')
                # print(container)

        except ValueError:
            print("Record do not exist.")
