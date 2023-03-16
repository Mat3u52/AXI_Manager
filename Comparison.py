import os
from DBConnect import DBConnect


class Comparison:
    def __init__(self, dir_name: str, db_name: str) -> None:
        """
        Constructor for Comparison class. Define tow main variables.

        :param dir_name: Given path the png/img files.
        :type dir_name: str
        :param db_name: Given name of the machine type from DB
        :type db_name: str
        :return: Init class
        :rtype: None
        """
        self.dir_name: str = dir_name
        self.db_name: str = db_name

    def __repr__(self):
        return self.dir_name

    def comparison_error(self) -> bool:
        if os.path.exists(self.dir_name):
            return True
        else:
            return False

    def recipes_db(self) -> set[str]:
        inventory: set[str] = set()
        for program_db in DBConnect.select_recipe('VITROXI_PROG'):
            inventory.add(program_db[0])

        return inventory

    def recipes_list(self) -> set[str]:
        inventory: set[str] = set()

        for prog in os.listdir(self.dir_name):
            inventory.add(prog[0:-4])

        return inventory


if __name__ == "__main__":
    obj_comparison = Comparison(dir_name="/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3163/",
                                db_name='VITROXI_PROG')
    if obj_comparison.comparison_error():
        # print(obj_comparison.recipes_list())
        obj_DBConnect = DBConnect()

        inventory_db: set[str] = set()
        for prog_db in obj_DBConnect.select_recipe('VITROXI_PROG'):
            inventory_db.add(prog_db[0])
        # print(inventory_db)

        # png to db
        print(obj_comparison.recipes_list().difference(inventory_db))
        # db to png
        print(inventory_db.difference(obj_comparison.recipes_list()))

