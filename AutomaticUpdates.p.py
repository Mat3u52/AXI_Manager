import os
from Config import Config

class AutomaticUpdates:
    def __init__(self):
        pass

    def bildGrid(self):
        showFiles = os.listdir("C:\\_PythonProject\\AXI_Manager\\Log\\V810-3163")
        print(showFiles)


if __name__ == "__main__":
    objAutomaticUpdates = AutomaticUpdates()
    objAutomaticUpdates.bildGrid()