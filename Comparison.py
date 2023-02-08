import os
from DBConnect import DBConnect

class Comparison:
    def __init__(self, dir_name: str) -> None:
        self.dir_name: str = dir_name

    def __repr__(self):
        return self.dir_name

    #@staticmethod
    def comparison_error(self) -> bool:
        if os.path.exists(self.dir_name):
            return True
        else:
            return False

    def recipes_list(self) -> set[str]:
        inventory: set[str] = set()

        for prog in os.listdir(self.dir_name):
            inventory.add(prog[0:-4])

        return inventory


if __name__ == "__main__":
    obj_comparison = Comparison("/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3163/")
    print(obj_comparison)
    if obj_comparison.comparison_error():
        #recipes_list = os.listdir(obj_comparison.dir_name)
        print(obj_comparison.recipes_list())
        obj_DBConnect = DBConnect()
        print(obj_DBConnect.select_recipe('VITROXI_PROG'))

        inventory_db: set[str] = set()
        for prog_db in obj_DBConnect.select_recipe('VITROXI_PROG'):
            inventory_db.add(prog_db)
        print(inventory_db)

        print(obj_comparison.recipes_list().difference(inventory_db))

