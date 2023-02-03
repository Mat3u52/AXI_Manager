import os

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

    def recipe_list(self) -> list[str]:
        inventory = os.listdir(self.dir_name)
        return inventory



if __name__ == "__main__":
    obj_comparison = Comparison("/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3163-/")
    print(obj_comparison)
    obj_comparison.comparison_error()
