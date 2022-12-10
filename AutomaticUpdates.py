import os
from Config import Config


class AutomaticUpdates(Config):
    def __init__(self):
        Config.__init__(self)
        #super().__init__()
        self.id = 0
        self.dicRecipe = {}

    def bildGrid(self) -> None:
        for self.device in self.devices:
            self.showFiles = os.listdir(self.pathLog+"/"+self.device)
            for self.showFile in self.showFiles:
                self.file = open(self.pathLog+"/"+self.device+"/"+self.showFile, "r")
                self.contentOfFile = self.file.readlines()
                self.strCycleTime = self.contentOfFile[14]
                self.cycleTime = (int(self.strCycleTime[18:21]) * 60) + int(self.strCycleTime[24:26])

                if os.path.isfile(self.pathRecipe+"/"+self.device+"/"+self.showFile[7:-5]+".txt"):
                    try:
                        self.fileRecipe = open(self.pathRecipe + "/" + self.device + "/" + self.showFile[7:-5]+".txt", "r").read()
                        self.lines = self.fileRecipe.split('\n')
                        self.i = 0
                        for self.line in self.lines:
                            if self.line == '# number of boards':
                                self.handle = self.i
                                #self.id += 1
                            self.i += 1
                        try:
                            self.fileRecipeInfo = open(
                                self.pathRecipe + "/" + self.device + "/" + self.showFile[7:-5] + ".txt", "r")
                            self.contentOfFileRecipe = self.fileRecipeInfo.readlines()
                            self.strBoardQTY = self.contentOfFileRecipe[int(self.handle)+1].strip('\n')

                            self.dicRecipe[int(self.id)] = {}
                            self.dicRecipe[int(self.id)]['device'] = self.device
                            self.dicRecipe[int(self.id)]['recipe'] = self.showFile[7:-5]
                            self.dicRecipe[int(self.id)]['cycleTime'] = self.cycleTime
                            self.dicRecipe[int(self.id)]['boardQty'] = self.strBoardQTY
                            self.id += 1
                        except FileNotFoundError:
                            pass
                        finally:
                            self.fileRecipeInfo.close()
                    except FileNotFoundError:
                        pass
                    finally:
                        pass
                        #self.fileRecipe.close()
                self.file.close()
        return self.dicRecipe

    def updateDic(self, id: int) -> None:
        self.id = id
        os.remove(self.pathLog+"/"+self.dicRecipe[self.id].get("device")+"/Recipe="+self.dicRecipe[self.id].get("recipe")+"$.txt")
        #del self.dicRecipe[self.id]
        self.dicRecipe.clear()


#if __name__ == "__main__":
#    objAutomaticUpdates = AutomaticUpdates()
    #print(objAutomaticUpdates.bildGrid().get(1))
#    print(len(objAutomaticUpdates.bildGrid()))
#    for i in range(len(objAutomaticUpdates.bildGrid())):
#        print(objAutomaticUpdates.bildGrid().get(i))
        #print(i)