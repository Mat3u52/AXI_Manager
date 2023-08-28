import os
from DBConnect import DBConnect

# from dataclasses import dataclass


class Comparison:
    # @dataclass(frozen=True)
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

    def __repr__(self) -> str:
        """
        Gives the string of variable

        :return: String of variables
        :rtype: str
        """
        return self.dir_name

    def recipes_db(self) -> set[str]:
        """
        Gives set of recipes name from database.

        :return: Recipes name in set
        :rtype: set
        """
        inventory: set[str] = set()
        try:
            for program_db in DBConnect().select_recipe(self.db_name):
                inventory.add(program_db[0])
            return inventory
        except Exception:
            return inventory

    def recipes_list(self) -> set[str]:
        """
        Gives set of recipes name from files in directory.

        :return: Recipes name in set
        :rtype: set
        """
        inventory: set[str] = set()
        try:
            for prog in os.listdir(self.dir_name):
                inventory.add(prog[0:-4])
            return inventory
        except FileNotFoundError:
            return inventory

    def one_recipe_in_dir(self) -> bool:
        pass


# if __name__ == "__main__":
#     obj_comparison = Comparison(dir_name="/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3483S2EX/",
#                                 db_name="VITROXIII_PROG")

    # png to db
    # print(obj_comparison.recipes_list().difference(obj_comparison.recipes_db()).remove(''))
    # print(obj_comparison.recipes_list().difference(obj_comparison.recipes_db()))
    # db to png
    # print(obj_comparison.recipes_db().difference(obj_comparison.recipes_list()).remove(''))
    # print(obj_comparison.recipes_db().difference(obj_comparison.recipes_list()))

