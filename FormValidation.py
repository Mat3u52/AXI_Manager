import tkinter
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

        self.flag_init_status = False

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

    def validator(self,
                  prog: str = "",
                  test_time: int = 0,
                  line_capa: str = "NONE",
                  epi: str = "NONE",
                  baan_status: str = "NONE",
                  comments: str = "",
                  flag_item_status: bool = False,
                  item_amount: int = 0,
                  align_time: int = 0,
                  laser_time: int = 0,
                  thickness_time: int = 0) -> None:
        """
        Function validate the variable.

        :param prog: program name
        :type prog: str
        :param test_time: time of scanning
        :type test_time: int
        :param line_capa: status of line capacity
        :type line_capa: str
        :param epi: status of epi
        :type epi: str
        :param baan_status: status of baan
        :type baan_status: str
        :param comments: comments
        :type comments: str
        :param flag_item_status: flag of item status
        :type flag_item_status: bool
        :param item_amount: amount of the boards in the panel
        :type item_amount: int
        :param align_time: time of alignment
        :type align_time: int
        :param laser_time: time of laser mapping
        :type laser_time: int
        :param thickness_time: time of automatic thickness measure
        :type thickness_time: int
        :return: message error or uph
        :rtype: None
        """
        try:
            self.flag_validator = False
            self.flag_init_status = flag_item_status
            if self.flag_init_status is True and \
                    prog != '' and \
                    test_time != '' and int(test_time) > 0 and \
                    line_capa and epi and baan_status and \
                    item_amount != '' and int(item_amount) > 0:

                self.prog = str(prog.strip())
                self.prog = self.prog.replace('/', '_')
                self.prog = self.prog.replace('\\', '_')
                self.test_time = int(test_time)
                self.line_capa = str(line_capa)
                self.epi = str(epi)
                self.baan_status = str(baan_status)
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
                self.totalTime = int(self.test_time) + int(self.alignTime) + int(self.laserTime) + int(self.thicknessTime)

                if (self._compute_uph(int(self.totalTime), 85, int(self.itemAmount)) > 0) and \
                        (self._compute_uph(int(self.totalTime), 95, int(self.itemAmount)) > 0):

                    self.uph85 = self._compute_uph(int(self.totalTime), 85, int(self.itemAmount))
                    self.uph95 = self._compute_uph(int(self.totalTime), 95, int(self.itemAmount))
                    self.uph95Time = self._convert_uph_to_time(self.uph95, self.itemAmount)
                    self.flag_validator = True

                else:
                    self.flag_validator = False

            else:
                self.prog = ""
                self.test_time = 0
                self.line_capa = "NONE"
                self.epi = "NONE"
                self.baan_status = "NONE"
                self.comments = ""
                self.uph85 = 0
                self.uph95 = 0
                self.uph95Time = 0
                self.alignTime = 0
                self.laserTime = 0
                self.thicknessTime = 0
                self.hex = ""
                self.flag_validator = False

        except ValueError:
            messagebox.showwarning("Warning!", "Wrong value.")

    def _compute_uph(self,
                     total_scanning_time: int,
                     capability: int,
                     qty_pcb: int,
                     transmit: int = 15,
                     ) -> None:
        """
        The auxiliary method to calculate unit per hour.

        :param total_scanning_time: time of scanning pcb
        :type total_scanning_time: int
        :param capability: efficiency factor
        :type capability: int
        :param qty_pcb: qty of boards in the panel
        :type qty_pcb: int
        :return: uph or 0
        :rtype: None
        """
        if int(total_scanning_time) > 0 and \
                int(capability) > 0 and \
                int(qty_pcb) > 0 and \
                int(transmit) > 0:
            self.total_scanning_time = total_scanning_time
            self.capability = capability
            self.qty_pcb = qty_pcb
            self.transmit = transmit

            self.uph = floor((3600 / (float(self.total_scanning_time) + int(self.transmit)) *
                              (float(self.capability) / 100))) * int(self.qty_pcb)
            return self.uph
        else:
            return 0

    def _convert_uph_to_time(self,
                             uph: int,
                             qty_pcb: int
                             ) -> None:
        """
        The auxiliary method to convert the uph to time

        :param uph: unit per hour
        :type uph: int
        :param qty_pcb: qty of boards in the panel
        :type qty_pcb: int
        :return: cycle time
        :rtype: None
        """
        if uph > 0 and qty_pcb > 0:
            self.uph = uph
            self.qty_pcb = qty_pcb
            self.cycle_time = ((3600 / float(self.uph)) / int(self.qty_pcb))
            return self.cycle_time
        else:
            return 0

    def clean_up_item(self,
                      entry_item: tkinter.Entry,
                      entry_qty: tkinter.Entry
                      ) -> None:
        """
        The method clean up two main fields in the form.

        :param entry_item: entry of item
        :type entry_item: tkinter.Entry
        :param entry_qty: entry of qty
        :type entry_qty: tkinter.Entry
        :return: clean up entry
        :rtype: None
        """

        if (self.flagInit is True) and entry_item and entry_qty:
            self.entry_item = entry_item
            self.entry_qty = entry_qty
            self.entry_item.delete(0, END)
            self.entry_qty.delete(0, END)

    def clean_up(self,
                 entry_program_name: tkinter.Entry,
                 ei1, ci2, ci3, ci4, ei5, ei6=0, ei7=0, ei8=0) -> None:
        """
        The method clean up whole form.
        :param entry_program_name: field of program name
        :type entry_program_name: tkinter.Entry
        :return: clean up each one entry from form
        :rtype: None
        """
        if (self.flag_validator is True) \
                and entry_program_name and ei1 and ci2 and ci3 and ci4 and ei5:
            self.flag_init_status = False
            self.entry_program_name = entry_program_name
            self.ei1 = ei1
            self.ci2 = ci2
            self.ci3 = ci3
            self.ci4 = ci4
            self.ei5 = ei5
            self.entry_program_name.delete(0, END)
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
        result = FormValidation._convert_uph_to_time(self, uph, qty_pcb)

        # then
        assert result

    def test__convert_uph_to_time_error(self) -> None:
        assert not FormValidation._convert_uph_to_time(self, 0, 0)
        assert not FormValidation._convert_uph_to_time(self, 0, 1)
        assert not FormValidation._convert_uph_to_time(self, 1, 0)
        # assert not FormValidation._convertUPHToTime(self, 1, 1)

    def test_validator_item(self, capsys) -> None:
        item: str = "test"
        item_amount: int = 1

        FormValidation.validator_item(self, item, item_amount)
        out, err = capsys.readouterr()

        assert out == 'OK - validator_item\n'
