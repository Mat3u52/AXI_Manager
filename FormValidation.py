from math import floor
from tkinter import END, messagebox


class FormValidation:
    def __init__(self) -> None:
        """
        Init for FormValidation.

        :return: Init values for variables
        :rtype: None
        """

        self.flagInit: bool = False
        self.totalTime: int = 0
        self.uph85: int = 0
        self.uph95: int = 0

        self.item: str = ""
        self.itemAmount: int = 0

        self.x: str = ""

    def validator_item(self, item: str, item_amount: int) -> None:
        """
        Verification two fields whether are filled in

        :param item: item name
        :type item: str
        :param item_amount: amount of boards in the panel
        :type item_amount: int
        :return: messagebox
        :rtype: None
        """
        try:
            if item != '' and item_amount != '' and int(item_amount) > 0:
                self.item = str(item.strip())
                self.itemAmount = int(item_amount)
                self.flagInit = True
            else:
                self.flagInit = False
                messagebox.showwarning("Warning!", "Lack of Item or Qty.")
        except ValueError:
            messagebox.showwarning("Warning!", "Wrong value.")

    def switch(self, x: str) -> int:
        """
        the method simulate switch from other technologies

        :param x: take the phrase
        :type x: str
        :return: number
        :rtype: int
        """
        self.x = x
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
                  flag_item_status=False, item_amount=0, align_time=0, laser_time=0, thickness_time=0):
        try:
            self.flagValidator = False
            self.flagInitStatus = flag_item_status
            if self.flagInitStatus is True and \
                    prog != '' and \
                    test != '' and int(test) > 0 and \
                    linecapa and epi and baan1 and \
                    item_amount != '' and int(item_amount) > 0:

                self.prog = str(prog.strip())
                self.prog = self.prog.replace('/', '_')
                self.prog = self.prog.replace('\\', '_')
                self.test = int(test)
                self.linecapa = str(linecapa)
                self.epi = str(epi)
                self.baan1 = str(baan1)
                self.comments = str(comments)
                self.itemAmount = int(item_amount)

                if align_time != '':
                    self.alignTime = int(align_time)
                else:
                    self.alignTime = 0
                if laser_time != '':
                    self.laserTime = int(laser_time)
                else:
                    self.laserTime = 0
                if thickness_time != '':
                    self.thicknessTime = int(thickness_time)
                else:
                    self.thicknessTime = 0

                self.hex = ""
                self.totalTime = int(self.test) + int(self.alignTime) + int(self.laserTime) + int(self.thicknessTime)

                if (self._computeUPH(int(self.totalTime), 85, int(self.itemAmount)) > 0) and \
                        (self._computeUPH(int(self.totalTime), 95, int(self.itemAmount)) > 0):

                    self.uph85 = self._computeUPH(int(self.totalTime), 85, int(self.itemAmount))
                    self.uph95 = self._computeUPH(int(self.totalTime), 95, int(self.itemAmount))
                    self.uph95Time = self._convertUPHToTime(self.uph95, self.itemAmount)
                    self.flagValidator = True

                else:
                    self.flagValidator = False

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

                self.flagValidator = False

        except ValueError:
            messagebox.showwarning("Warning!", "Wrong value.")

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

    def _convertUPHToTime(self, uph, qty_pcb):
        if uph > 0 and qty_pcb > 0:
            self.uph = uph
            self.qtyPCB = qty_pcb
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

    def cleanUp(self, ei0, ei1, ci2, ci3, ci4, ei5, ei6=0, ei7=0, ei8=0):
        if (self.flagValidator is True) \
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


class TestFormValidation:
    def test__convert_uph_to_time(self) -> None:
        # given
        uph: float = 60
        qty_pcb: int = 1

        # when
        result = FormValidation._convertUPHToTime(self, uph, qty_pcb)

        # then
        assert result

    def test__convert_uph_to_time_error(self) -> None:
        assert not FormValidation._convertUPHToTime(self, 0, 0)
        assert not FormValidation._convertUPHToTime(self, 0, 1)
        assert not FormValidation._convertUPHToTime(self, 1, 0)
        # assert not FormValidation._convertUPHToTime(self, 1, 1)

    def test_validator_item(self, capsys) -> None:
        item: str = "test"
        item_amount: int = 1

        FormValidation.validator_item(self, item, item_amount)
        out, err = capsys.readouterr()

        assert out == 'OK - validator_item\n'



