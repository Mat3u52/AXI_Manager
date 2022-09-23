from math import *
from tkinter import messagebox
from tkinter import *

class FormValidation:
    def __init__(self):
        self.flagInit = False

    def validatorItem(self, item, itemAmount):
        self.item = ""
        self.itemAmount = 0
        try:
            if item != '' and itemAmount != '' and\
                    itemAmount != '' and int(itemAmount) > 0:

                self.item = str(item.strip())
                self.itemAmount = int(itemAmount)
                self.flagInit = True

                print(self.item)
                print(self.itemAmount)
                messagebox.showwarning("OK")
            else:
                self.flagInit = False
                messagebox.showwarning("Warning!", "Lack of Item or Qty.")
        except ValueError:
            messagebox.showwarning("Warning!", "Wrong value.")

    def switch(self, x):
        match self.x:
            case "NONE":
                return 0
            case "YES":
                return 1
            case "NO":
                return 2
            case "LACK":
                return 3
            case _:
                return 0

    def validator(self, prog="", test=0, linecapa="NONE", epi="NONE", baan1="NONE", comments="",
                        flagItemStatus=False, itemAmount=0, alignTime=0, laserTime=0, thicknessTime=0):
        try:
            self.flagValidatorViTrox = False
            self.flagInitStatus = flagItemStatus
            if self.flagInitStatus is True and\
                    prog != '' and \
                    test != '' and int(test) > 0 and\
                    linecapa and epi and baan1 and\
                    comments and \
                    itemAmount != '' and int(itemAmount) > 0:

                self.prog = str(prog.strip())
                self.test = int(test)
                self.linecapa = str(linecapa)
                self.epi = str(epi)
                self.baan1 = str(baan1)
                self.comments = str(comments)
                self.itemAmount = int(itemAmount)

                if alignTime != '':
                    self.alignTime = int(alignTime)
                else:
                    self.alignTime = 0
                if laserTime != '':
                    self.laserTime = int(laserTime)
                else:
                    self.laserTime = 0
                if thicknessTime != '':
                    self.thicknessTime = int(thicknessTime)
                else:
                    self.thicknessTime = 0

                self.hex = ""

                # self.totalTime = self.test
                self.totalTime = int(self.test) + int(self.alignTime) + int(self.laserTime) + int(self.thicknessTime)

                if (self._computeUPH(int(self.totalTime), 85, int(self.itemAmount)) > 0) and \
                        (self._computeUPH(int(self.totalTime), 95, int(self.itemAmount)) > 0):

                    self.uph85 = self._computeUPH(int(self.totalTime), 85, int(self.itemAmount))
                    self.uph95 = self._computeUPH(int(self.totalTime), 95, int(self.itemAmount))
                    self.uph95Time = self._convertUPHToTime(self.uph95, self.itemAmount)
                    self.flagValidatorViTrox = True

                    messagebox.showwarning("OK")

                    print(self.itemAmount)
                    print(self.prog)
                    print(self.test)
                    print(self.linecapa)
                    print(self.epi)
                    print(self.baan1)
                    print(self.comments)
                    print(self.uph85)
                    print(self.uph95)
                    print(self.uph95Time)

                else:
                    self.flagValidatorViTrox = False

            else:
                self.prog = ""
                self.test = 0
                self.linecapa = "NONE"
                self.epi = "NONE"
                self.baan1 = "NONE"
                self.comments = ""
                self.uph85 = 0
                self.uph95 = 0
                self.uph95Time = 0

                self.alignTime = 0
                self.laserTime = 0
                self.thicknessTime = 0

                self.hex = ""

                self.flagValidatorViTrox = False
        except ValueError:
            messagebox.showwarning("Warning!", "Wrong value.")


    def _status5DX(self, baanV849="NONE", baanV817="NONE"):
        self.baanV849 = baanV849
        self.baanV817 = baanV817
        if int(self.switch(self.baanV849)) <= int(self.switch(self.baanV817)):
            return self.baanV817
        else:
            return self.baanV849


    def readyToInsert(self, totalTestV849=0, totalTestV817=0):
        #self.totalTestV849 = totalTestV849
        #self.totalTestV817 = totalTestV817
        if totalTestV849 >= totalTestV817:
            print("5dx1")

            #print(cls.itemAmount)
            #print(cls.prog)
            #print(cls.test)
            #print(cls.linecapa)
            #print(cls.epi)
            #print(cls.baan1) # !!!!
            #print(cls.comments)
            #print(cls.uph85)
            #print(cls.uph95)
            #print(cls.uph95Time)
        else:
            print("5dx2")
            #print(cls.itemAmount)
            #print(cls.prog)
            #print(cls.test)
            #print(cls.linecapa)
            #print(cls.epi)
            #print(cls.baan1) # !!!!
            #print(cls.comments)
            #print(cls.uph85)
            #print(cls.uph95)
            #print(cls.uph95Time)






    #                            dxUPH85,
    #                            dxUPH95Time,
    #                            dxUPH95,

    #                            alignTime,
    #                            laserTime,
    #                            thicknessTime,
    #                            testTime,

    #                            baan5DXStatus,

    #                               progV849,
    #                               objCheckboxMenu5DX0.CI_2.get(),
    #                               objCheckboxMenu5DX0.CI_3.get(),
    #                               commentsV849,
    #                            hexV849,

    #                            progV817,
    #                            objCheckboxMenu5DX1.CI_2.get(),
    #                            objCheckboxMenu5DX1.CI_3.get(),
    #                            commentsV817,
    #                            hexV817

    def _computeUPH(self, totalScaningTime, capability, qtyPCB):
        if totalScaningTime > 0 and capability > 0 and qtyPCB > 0:
            self.totalScaningTime = totalScaningTime
            self.capability = capability
            self.qtyPCB = qtyPCB

            self.uph = floor((3600 / (float(self.totalScaningTime) + 15) *
                              (float(self.capability) / 100))) * int(self.qtyPCB)
            return self.uph
        else:
            return 0


    def _convertUPHToTime(self, uph, qtyPCB):
        if uph > 0 and qtyPCB > 0:
            self.uph = uph
            self.qtyPCB = qtyPCB
            self.cycleTime = ((3600 / float(self.uph)) / int(self.qtyPCB))
            return self.cycleTime
        else:
            return 0

    def cleanUpItem(self, ei2, ei3):
        if (self.flagInit is True) and ei2 and ei3:
            self.ei2 = ei2
            self.ei3 = ei3
            self.ei2.delete(0, END)
            self.ei3.delete(0, END)
        else:
            pass

    def cleanUp(self, ei0, ei1, ci2, ci3, ci4, ei5, ei6=0, ei7=0, ei8=0):
        if (self.flagValidatorViTrox is True) \
                and ei0 and ei1 and ci2 and ci3 and ci4 and ei5:
            self.flagInitStatus = False
            self.ei0 = ei0
            self.ei1 = ei1
            self.ci2 = ci2
            self.ci3 = ci3
            self.ci4 = ci4
            self.ei5 = ei5
            self.ei0.delete(0, END)
            self.ei1.delete(0, END)
            self.ci2.current(0)
            self.ci3.current(0)
            self.ci4.current(0)
            self.ei5.delete(0, END)

            if ei6 or ei7 or ei8:
                self.ei6 = ei6
                self.ei7 = ei7
                self.ei8 = ei8
                self.ei6.delete(0, END)
                self.ei7.delete(0, END)
                self.ei8.delete(0, END)
        else:
            pass
