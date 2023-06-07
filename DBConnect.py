import pymysql
from tkinter import messagebox
import math


class DBConnect:
    def __init__(self) -> None:
        """
        Constructor of DBConnect class. It establishes a connection to database mk_database.

        :return: Credentials to database
        :rtype: None
        """
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="toor",
            database="mk_database",
            charset="utf8mb4",
        )
        self.dbCursor = self.db.cursor()
        self.flagSucceeded = False

    def selectAll(self) -> tuple:
        self.dbCursor.execute("SELECT * FROM mk_diary ORDER BY ITEM ASC")
        records = self.dbCursor.fetchall()
        return records

    def select_recipe(self, device: str) -> tuple:
        device = device
        self.dbCursor.execute(
            "SELECT " + device + " FROM mk_diary ORDER BY " + device + " ASC"
        )
        records = self.dbCursor.fetchall()
        return records

    def selectSearchID(self, ID: str) -> tuple:
        self.ID = ID
        self.dbCursor.execute(
            "SELECT * FROM mk_diary WHERE ITEM_ID LIKE " + self.ID + ""
        )
        records = self.dbCursor.fetchall()
        return records

    def selectSearchItem(self, item: str) -> tuple:
        self.item = item
        self.dbCursor.execute(
            "SELECT * FROM mk_diary WHERE ITEM LIKE %s LIMIT 1", (self.item)
        )
        records = self.dbCursor.fetchall()
        return records

    def delete_by_id(self, record_id: str) -> None:
        """
        Delete one record by id

        :param record_id: id of record to remove
        :type record_id: str
        :return: removed record from mk_diary
        :rtype: None
        """
        record_id = record_id
        self.dbCursor.execute(
            "DELETE FROM mk_diary WHERE ITEM_ID = "+record_id+""
        )

    def update(
        self,
        ID,
        item,
        itemAmount,
        vitroxIVProg,
        vitroxIVTest,
        vitroxIVLinecapa,
        vitroxIVEPI,
        vitroxIVBAAN1,
        vitroxIVComments,
    ):
        self.ID = int(ID)
        self.item = str(item)
        self.itemAmount = int(itemAmount)

        self.vitroxIVProg = str(vitroxIVProg)
        self.vitroxIVTest = str(vitroxIVTest)
        self.vitroxIVLinecapa = str(vitroxIVLinecapa)
        self.vitroxIVEPI = str(vitroxIVEPI)
        self.vitroxIVBAAN1 = str(vitroxIVBAAN1)
        self.vitroxIVComments = str(vitroxIVComments)
        if float(vitroxIVTest) > 0:
            self.vitroxIVUPH85 = math.floor(
                (3600 / (float(self.vitroxIVTest) + 15) * 0.85)
            ) * int(self.itemAmount)
            self.vitroxIVUPH95 = math.floor(
                (3600 / (float(self.vitroxIVTest) + 15) * 0.95)
            ) * int(self.itemAmount)
            self.vitroxIVUPH95Time = (3600 / float(self.vitroxIVUPH95)) / int(
                self.itemAmount
            )
        else:
            self.vitroxIVUPH85 = 0
            self.vitroxIVUPH95 = 0
            self.vitroxIVUPH95Time = 0

        sql = (
            "UPDATE mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, "
            "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s,"
            " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s,"
            " VITROXIV_DSVR = %s, VITROXIV_TIME = %s "
            "WHERE ITEM_ID = %s"
        )
        val = (
            self.item,
            self.itemAmount,
            self.vitroxIVProg,
            self.vitroxIVTest,
            self.vitroxIVLinecapa,
            self.vitroxIVEPI,
            self.vitroxIVBAAN1,
            self.vitroxIVComments,
            self.vitroxIVUPH85,
            self.vitroxIVUPH95,
            self.vitroxIVUPH95Time,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def switch(self, x) -> int:
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

    def insert(
        self,
        initDevice,
        initStatus,
        initItem,
        initAmount,
        initProg,
        initTest,
        initLinecapa,
        initEPI,
        initBAAN1,
        initComments,
        initUPH85,
        initUPH95,
        initUPH95Time,
        initStatusDevice=False,
        initAlignTime=0,
        initLaserTime=0,
        initThicknessTime=0,
        initTotalTest=0,
        initStatus5DX=False,
        initProg5DX="",
        initTest5DX=0,
        initLinecapa5DX="NONE",
        initEPI5DX="NONE",
        initBAAN15DX="NONE",
        initComments5DX="",
        initUPH855DX=0,
        initUPH955DX=0,
        initUPH95Time5DX=0,
        initAlignTime5DX=0,
        initLaserTime5DX=0,
        initThicknessTime5DX=0,
        initTotalTest5DX=0,
    ):
        if (
            initDevice
            and initStatus
            and initItem
            and initAmount
            and (initStatusDevice is True or initStatus5DX is True)
        ):
            self.device = initDevice
            self.status = initStatus
            self.item = initItem
            self.itemAmount = initAmount
            self.flag = False

            self.devices = (
                "V849_V817",
                "V810-3163",
                "V810-3483S2EX",
                "V810-3553S2EX",
                "V810-8120S2",
            )

            self.V8103553S2EXProg = ""
            self.V8103553S2EXTest = 0
            self.V8103553S2EXLinecapa = "NONE"
            self.V8103553S2EXEPI = "NONE"
            self.V8103553S2EXBAAN1 = "NONE"
            self.V8103553S2EXComments = ""
            self.V8103553S2EXUPH85 = 0
            self.V8103553S2EXUPH95 = 0
            self.V8103553S2EXUPH95Time = 0

            self.V8103483S2EXProg = ""
            self.V8103483S2EXTest = 0
            self.V8103483S2EXLinecapa = "NONE"
            self.V8103483S2EXEPI = "NONE"
            self.V8103483S2EXBAAN1 = "NONE"
            self.V8103483S2EXComments = ""
            self.V8103483S2EXUPH85 = 0
            self.V8103483S2EXUPH95 = 0
            self.V8103483S2EXUPH95Time = 0

            self.V8108120S2Prog = ""
            self.V8108120S2Test = 0
            self.V8108120S2Linecapa = "NONE"
            self.V8108120S2EPI = "NONE"
            self.V8108120S2BAAN1 = "NONE"
            self.V8108120S2Comments = ""
            self.V8108120S2UPH85 = 0
            self.V8108120S2UPH95 = 0
            self.V8108120S2UPH95Time = 0

            self.V8103163Prog = ""
            self.V8103163Test = 0
            self.V8103163Linecapa = "NONE"
            self.V8103163EPI = "NONE"
            self.V8103163BAAN1 = "NONE"
            self.V8103163Comments = ""
            self.V8103163UPH85 = 0
            self.V8103163UPH95 = 0
            self.V8103163UPH95Time = 0

            self.dxUPH85 = 0  # common
            self.dxUPH95Time = 0  # common
            self.dxUPH95 = 0  # common

            self.dxAlign = 0  # added
            self.dxMap = 0  # added
            self.dxAutoThickness = 0  # added
            self.dxTest = 0

            self.dxBAAN1 = "NONE"  # common

            self.V849Prog = ""
            self.V849Linecapa = "NONE"
            self.V849EPI = "NONE"
            self.V849Comments = ""
            self.V849HEX = ""  # added

            self.V817Prog = ""
            self.V817Linecapa = "NONE"
            self.V817EPI = "NONE"
            self.V817Comments = ""
            self.V817HEX = ""  # added

            for self.machine in self.devices:
                if self.machine == self.device:
                    if self.selectSearchItem(self.item):
                        for self.row in self.selectSearchItem(self.item):
                            pass
                        msgBox = messagebox.askquestion(
                            f"The record already exist in DB! - {self.machine}",
                            f"Device: {self.machine}\n\n"
                            f"Existing Item: {self.row[1]} [  {self.row[0]} ]\n\n "
                            f"Amount of the board in one panel: {self.row[3]}\n\n "
                            f"Do you want to update the record?",
                        )
                        # msgBox = messagebox.askquestion(f"The record already exist in DB! - {self.machine}",
                        #                                 f"Existing Item: {self.row[1]} [  {self.row[0]} ]\n\n "
                        #                                 f"Amount of the board in one panel: {self.row[3]}\n\n "
                        #                                 f"ViTroxEx:\n\n"
                        #                                 f"V810-3553S2EX: {self.row[54]} Scanning Time: {self.row[52]}\n "
                        #                                 f"V810-3483S2EX: {self.row[45]} Scanning Time: {self.row[41]}\n "
                        #                                 f"V810-3163: {self.row[27]} Scanning Time: {self.row[13]}\n "
                        #                                 f"\n\nViTrox XXL:\n\n"
                        #                                 f"V810-8120S2: {self.row[31]} Scanning Time: {self.row[35]}\n "
                        #                                 f"\n\n5DX:\n\n"
                        #                                 f"V849: {self.row[17]}\n"
                        #                                 f"V817: {self.row[22]}\n\n "
                        #                                 f"A:{self.row[7]} M:{self.row[8]} Th:{self.row[9]} T:{self.row[10]} \n\n"
                        #                                 f"Do you want to update the record?")
                        if msgBox == "yes":
                            if self.device == "V810-3553S2EX":
                                self.V8103553S2EXProg = initProg
                                self.V8103553S2EXTest = initTest
                                self.V8103553S2EXLinecapa = initLinecapa
                                self.V8103553S2EXEPI = initEPI
                                self.V8103553S2EXBAAN1 = initBAAN1
                                self.V8103553S2EXComments = initComments
                                self.V8103553S2EXUPH85 = initUPH85
                                self.V8103553S2EXUPH95 = initUPH95
                                self.V8103553S2EXUPH95Time = initUPH95Time

                                if (
                                    self.V8103553S2EXProg != ""
                                    and int(self.V8103553S2EXTest) > 0
                                ):
                                    self._updateV8103553S2EX(self.row[0])

                            elif self.device == "V810-3483S2EX":
                                self.V8103483S2EXProg = initProg
                                self.V8103483S2EXTest = initTest
                                self.V8103483S2EXLinecapa = initLinecapa
                                self.V8103483S2EXEPI = initEPI
                                self.V8103483S2EXBAAN1 = initBAAN1
                                self.V8103483S2EXComments = initComments
                                self.V8103483S2EXUPH85 = initUPH85
                                self.V8103483S2EXUPH95 = initUPH95
                                self.V8103483S2EXUPH95Time = initUPH95Time

                                if (
                                    self.V8103483S2EXProg != ""
                                    and int(self.V8103483S2EXTest) > 0
                                ):
                                    self._updateV8103483S2EX(self.row[0])

                            elif self.device == "V810-8120S2":
                                self.V8108120S2Prog = initProg
                                self.V8108120S2Test = initTest
                                self.V8108120S2Linecapa = initLinecapa
                                self.V8108120S2EPI = initEPI
                                self.V8108120S2BAAN1 = initBAAN1
                                self.V8108120S2Comments = initComments
                                self.V8108120S2UPH85 = initUPH85
                                self.V8108120S2UPH95 = initUPH95
                                self.V8108120S2UPH95Time = initUPH95Time

                                if (
                                    self.V8108120S2Prog != ""
                                    and int(self.V8108120S2Test) > 0
                                ):
                                    self._updateV8108120S2(self.row[0])

                            elif self.device == "V810-3163":
                                self.V8103163Prog = initProg
                                self.V8103163Test = initTest
                                self.V8103163Linecapa = initLinecapa
                                self.V8103163EPI = initEPI
                                self.V8103163BAAN1 = initBAAN1
                                self.V8103163Comments = initComments
                                self.V8103163UPH85 = initUPH85
                                self.V8103163UPH95 = initUPH95
                                self.V8103163UPH95Time = initUPH95Time

                                if (
                                    self.V8103163Prog != ""
                                    and int(self.V8103163Test) > 0
                                ):
                                    self._updateV8103163(self.row[0])

                            elif self.device == "V849_V817":
                                self.V849Prog = initProg
                                self.V849Linecapa = initLinecapa
                                self.V849EPI = initEPI
                                self.V849Comments = initComments
                                self.V849HEX = ""

                                self.V817Prog = initProg5DX
                                self.V817Linecapa = initLinecapa5DX
                                self.V817EPI = initEPI5DX
                                self.V817Comments = initComments5DX
                                self.V817HEX = ""

                                if initTotalTest >= initTotalTest5DX:
                                    # 5dx 1
                                    self.dxAlign = initAlignTime
                                    self.dxMap = initLaserTime
                                    self.dxAutoThickness = initThicknessTime
                                    self.dxTest = initTest

                                    self.dxUPH85 = initUPH85
                                    self.dxUPH95Time = initUPH95Time
                                    self.dxUPH95 = initUPH95

                                else:
                                    # 5dx 2
                                    self.dxAlign = initAlignTime5DX
                                    self.dxMap = initLaserTime5DX
                                    self.dxAutoThickness = initThicknessTime5DX
                                    self.dxTest = initTest5DX

                                    self.dxUPH85 = initUPH855DX
                                    self.dxUPH95Time = initUPH95Time5DX
                                    self.dxUPH95 = initUPH955DX

                                if int(self.switch(initBAAN1)) >= int(
                                    self.switch(initBAAN15DX)
                                ):
                                    self.dxBAAN1 = initBAAN1
                                else:
                                    self.dxBAAN1 = initBAAN15DX

                            if (self.V849Prog != "" or self.V817Prog != "") and int(
                                self.dxTest
                            ) > 0:
                                self._updateV849V817(self.row[0])

                            self.flagSucceeded = True

                        self.flag = True
                    else:
                        if self.device == "V810-3553S2EX":
                            self.V8103553S2EXProg = initProg
                            self.V8103553S2EXTest = initTest
                            self.V8103553S2EXLinecapa = initLinecapa
                            self.V8103553S2EXEPI = initEPI
                            self.V8103553S2EXBAAN1 = initBAAN1
                            self.V8103553S2EXComments = initComments
                            self.V8103553S2EXUPH85 = initUPH85
                            self.V8103553S2EXUPH95 = initUPH95
                            self.V8103553S2EXUPH95Time = initUPH95Time
                        elif self.device == "V810-3483S2EX":
                            self.V8103483S2EXProg = initProg
                            self.V8103483S2EXTest = initTest
                            self.V8103483S2EXLinecapa = initLinecapa
                            self.V8103483S2EXEPI = initEPI
                            self.V8103483S2EXBAAN1 = initBAAN1
                            self.V8103483S2EXComments = initComments
                            self.V8103483S2EXUPH85 = initUPH85
                            self.V8103483S2EXUPH95 = initUPH95
                            self.V8103483S2EXUPH95Time = initUPH95Time
                        elif self.device == "V810-8120S2":
                            self.V8108120S2Prog = initProg
                            self.V8108120S2Test = initTest
                            self.V8108120S2Linecapa = initLinecapa
                            self.V8108120S2EPI = initEPI
                            self.V8108120S2BAAN1 = initBAAN1
                            self.V8108120S2Comments = initComments
                            self.V8108120S2UPH85 = initUPH85
                            self.V8108120S2UPH95 = initUPH95
                            self.V8108120S2UPH95Time = initUPH95Time
                        elif self.device == "V810-3163":
                            self.V8103163Prog = initProg
                            self.V8103163Test = initTest
                            self.V8103163Linecapa = initLinecapa
                            self.V8103163EPI = initEPI
                            self.V8103163BAAN1 = initBAAN1
                            self.V8103163Comments = initComments
                            self.V8103163UPH85 = initUPH85
                            self.V8103163UPH95 = initUPH95
                            self.V8103163UPH95Time = initUPH95Time
                        elif self.device == "V849_V817":
                            self.V849Prog = initProg
                            self.V849Linecapa = initLinecapa
                            self.V849EPI = initEPI
                            self.V849Comments = initComments
                            self.V849HEX = ""

                            self.V817Prog = initProg5DX
                            self.V817Linecapa = initLinecapa5DX
                            self.V817EPI = initEPI5DX
                            self.V817Comments = initComments5DX
                            self.V817HEX = ""

                            if initTotalTest >= initTotalTest5DX:
                                # 5dx 1
                                self.dxAlign = initAlignTime
                                self.dxMap = initLaserTime
                                self.dxAutoThickness = initThicknessTime
                                self.dxTest = initTest

                                self.dxUPH85 = initUPH85
                                self.dxUPH95Time = initUPH95Time
                                self.dxUPH95 = initUPH95

                            else:
                                # 5dx 2
                                self.dxAlign = initAlignTime5DX
                                self.dxMap = initLaserTime5DX
                                self.dxAutoThickness = initThicknessTime5DX
                                self.dxTest = initTest5DX

                                self.dxUPH85 = initUPH855DX
                                self.dxUPH95Time = initUPH95Time5DX
                                self.dxUPH95 = initUPH955DX

                            if int(self.switch(initBAAN1)) >= int(
                                self.switch(initBAAN15DX)
                            ):
                                self.dxBAAN1 = initBAAN1
                            else:
                                self.dxBAAN1 = initBAAN15DX

                        self.flagSucceeded = True
                        self.flag = False
                        self._insert()

    def _insert(self) -> None:
        sql = (
            "INSERT mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, "
            "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s,"
            " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s,"
            " VITROXIV_DSVR = %s, VITROXIV_TIME = %s,"
            " VITROXIII_PROG = %s, VITROXIII_TEST = %s, VITROXIII_LINECAPA = %s,"
            " VITROXIII_EPI = %s, VITROXIII_BAAN1 = %s, VITROXIII_COMMENTS = %s, VITROXIII_BAAN = %s,"
            " VITROXIII_DSVR = %s, VITROXIII_TIME = %s,"
            " VITROXII_PROG = %s, VITROXII_TEST = %s, VITROXII_LINECAPA = %s,"
            " VITROXII_EPI = %s, VITROXII_BAAN1 = %s, VITROXII_COMMENTS = %s, VITROXII_BAAN = %s,"
            " VITROXII_DSVR = %s, VITROXII_TIME = %s,"
            " VITROXI_PROG = %s, VITROX_TEST = %s, VITROXI_LINECAPA = %s,"
            " VITROXI_EPI = %s, VITROX_BAAN1 = %s, VITROXI_COMMENTS = %s, VITROX_BAAN = %s,"
            " VITROX_DSVR = %s, VITROX_TIME = %s,"
            " 5DX_BAAN = %s, 5DX_TIME = %s, 5DX_DSVR = %s, 5DX_ALIGN = %s, 5DX_MAP = %s, 5DX_AUTO_THICKNESS = %s,"
            " 5DX_TEST = %s, 5DX_BAAN1 = %s, 5DXI_PROG = %s, 5DXI_LINECAPA = %s, 5DXI_EPI = %s,"
            " 5DXI_COMMENTS = %s, HEXI = %s, 5DXII_PROG = %s, 5DXII_LINECAPA = %s, 5DXII_EPI = %s,"
            " 5DXII_COMMENTS = %s, HEXII = %s"
        )
        val = (
            self.item,
            self.itemAmount,
            self.V8103553S2EXProg,
            self.V8103553S2EXTest,
            self.V8103553S2EXLinecapa,
            self.V8103553S2EXEPI,
            self.V8103553S2EXBAAN1,
            self.V8103553S2EXComments,
            self.V8103553S2EXUPH85,
            self.V8103553S2EXUPH95,
            self.V8103553S2EXUPH95Time,
            self.V8103483S2EXProg,
            self.V8103483S2EXTest,
            self.V8103483S2EXLinecapa,
            self.V8103483S2EXEPI,
            self.V8103483S2EXBAAN1,
            self.V8103483S2EXComments,
            self.V8103483S2EXUPH85,
            self.V8103483S2EXUPH95,
            self.V8103483S2EXUPH95Time,
            self.V8108120S2Prog,
            self.V8108120S2Test,
            self.V8108120S2Linecapa,
            self.V8108120S2EPI,
            self.V8108120S2BAAN1,
            self.V8108120S2Comments,
            self.V8108120S2UPH85,
            self.V8108120S2UPH95,
            self.V8108120S2UPH95Time,
            self.V8103163Prog,
            self.V8103163Test,
            self.V8103163Linecapa,
            self.V8103163EPI,
            self.V8103163BAAN1,
            self.V8103163Comments,
            self.V8103163UPH85,
            self.V8103163UPH95,
            self.V8103163UPH95Time,
            self.dxUPH85,
            self.dxUPH95Time,
            self.dxUPH95,
            self.dxAlign,
            self.dxMap,
            self.dxAutoThickness,
            self.dxTest,
            self.dxBAAN1,
            self.V849Prog,
            self.V849Linecapa,
            self.V849EPI,
            self.V849Comments,
            self.V849HEX,
            self.V817Prog,
            self.V817Linecapa,
            self.V817EPI,
            self.V817Comments,
            self.V817HEX,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _updateV8103553S2EX(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET "
            "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s,"
            " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s,"
            " VITROXIV_DSVR = %s, VITROXIV_TIME = %s WHERE ITEM_ID = %s"
        )
        val = (
            self.V8103553S2EXProg,
            self.V8103553S2EXTest,
            self.V8103553S2EXLinecapa,
            self.V8103553S2EXEPI,
            self.V8103553S2EXBAAN1,
            self.V8103553S2EXComments,
            self.V8103553S2EXUPH85,
            self.V8103553S2EXUPH95,
            self.V8103553S2EXUPH95Time,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _updateV8103483S2EX(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET "
            " VITROXIII_PROG = %s, VITROXIII_TEST = %s, VITROXIII_LINECAPA = %s,"
            " VITROXIII_EPI = %s, VITROXIII_BAAN1 = %s, VITROXIII_COMMENTS = %s, VITROXIII_BAAN = %s,"
            " VITROXIII_DSVR = %s, VITROXIII_TIME = %s WHERE ITEM_ID = %s"
        )
        val = (
            self.V8103483S2EXProg,
            self.V8103483S2EXTest,
            self.V8103483S2EXLinecapa,
            self.V8103483S2EXEPI,
            self.V8103483S2EXBAAN1,
            self.V8103483S2EXComments,
            self.V8103483S2EXUPH85,
            self.V8103483S2EXUPH95,
            self.V8103483S2EXUPH95Time,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _updateV8108120S2(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET "
            " VITROXII_PROG = %s, VITROXII_TEST = %s, VITROXII_LINECAPA = %s,"
            " VITROXII_EPI = %s, VITROXII_BAAN1 = %s, VITROXII_COMMENTS = %s, VITROXII_BAAN = %s,"
            " VITROXII_DSVR = %s, VITROXII_TIME = %s WHERE ITEM_ID = %s"
        )
        val = (
            self.V8108120S2Prog,
            self.V8108120S2Test,
            self.V8108120S2Linecapa,
            self.V8108120S2EPI,
            self.V8108120S2BAAN1,
            self.V8108120S2Comments,
            self.V8108120S2UPH85,
            self.V8108120S2UPH95,
            self.V8108120S2UPH95Time,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _updateV8103163(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET "
            " VITROXI_PROG = %s, VITROX_TEST = %s, VITROXI_LINECAPA = %s,"
            " VITROXI_EPI = %s, VITROX_BAAN1 = %s, VITROXI_COMMENTS = %s, VITROX_BAAN = %s,"
            " VITROX_DSVR = %s, VITROX_TIME = %s WHERE ITEM_ID = %s"
        )
        val = (
            self.V8103163Prog,
            self.V8103163Test,
            self.V8103163Linecapa,
            self.V8103163EPI,
            self.V8103163BAAN1,
            self.V8103163Comments,
            self.V8103163UPH85,
            self.V8103163UPH95,
            self.V8103163UPH95Time,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _updateV849V817(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET "
            " 5DX_BAAN = %s, 5DX_TIME = %s, 5DX_DSVR = %s, 5DX_ALIGN = %s, 5DX_MAP = %s, 5DX_AUTO_THICKNESS = %s,"
            " 5DX_TEST = %s, 5DX_BAAN1 = %s, 5DXI_PROG = %s, 5DXI_LINECAPA = %s, 5DXI_EPI = %s,"
            " 5DXI_COMMENTS = %s, HEXI = %s, 5DXII_PROG = %s, 5DXII_LINECAPA = %s, 5DXII_EPI = %s,"
            " 5DXII_COMMENTS = %s, HEXII = %s WHERE ITEM_ID = %s"
        )
        val = (
            self.dxUPH85,
            self.dxUPH95Time,
            self.dxUPH95,
            self.dxAlign,
            self.dxMap,
            self.dxAutoThickness,
            self.dxTest,
            self.dxBAAN1,
            self.V849Prog,
            self.V849Linecapa,
            self.V849EPI,
            self.V849Comments,
            self.V849HEX,
            self.V817Prog,
            self.V817Linecapa,
            self.V817EPI,
            self.V817Comments,
            self.V817HEX,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _update(self, id: int) -> None:
        self.ID = id
        sql = (
            "UPDATE mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, "
            "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s,"
            " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s,"
            " VITROXIV_DSVR = %s, VITROXIV_TIME = %s,"
            " VITROXIII_PROG = %s, VITROXIII_TEST = %s, VITROXIII_LINECAPA = %s,"
            " VITROXIII_EPI = %s, VITROXIII_BAAN1 = %s, VITROXIII_COMMENTS = %s, VITROXIII_BAAN = %s,"
            " VITROXIII_DSVR = %s, VITROXIII_TIME = %s,"
            " VITROXII_PROG = %s, VITROXII_TEST = %s, VITROXII_LINECAPA = %s,"
            " VITROXII_EPI = %s, VITROXII_BAAN1 = %s, VITROXII_COMMENTS = %s, VITROXII_BAAN = %s,"
            " VITROXII_DSVR = %s, VITROXII_TIME = %s,"
            " VITROXI_PROG = %s, VITROX_TEST = %s, VITROXI_LINECAPA = %s,"
            " VITROXI_EPI = %s, VITROX_BAAN1 = %s, VITROXI_COMMENTS = %s, VITROX_BAAN = %s,"
            " VITROX_DSVR = %s, VITROX_TIME = %s,"
            " 5DX_BAAN = %s, 5DX_TIME = %s, 5DX_DSVR = %s, 5DX_ALIGN = %s, 5DX_MAP = %s, 5DX_AUTO_THICKNESS = %s,"
            " 5DX_TEST = %s, 5DX_BAAN1 = %s, 5DXI_PROG = %s, 5DXI_LINECAPA = %s, 5DXI_EPI = %s,"
            " 5DXI_COMMENTS = %s, HEXI = %s, 5DXII_PROG = %s, 5DXII_LINECAPA = %s, 5DXII_EPI = %s,"
            " 5DXII_COMMENTS = %s, HEXII = %s"
            " WHERE ITEM_ID = %s"
        )
        val = (
            self.item,
            self.itemAmount,
            self.V8103553S2EXProg,
            self.V8103553S2EXTest,
            self.V8103553S2EXLinecapa,
            self.V8103553S2EXEPI,
            self.V8103553S2EXBAAN1,
            self.V8103553S2EXComments,
            self.V8103553S2EXUPH85,
            self.V8103553S2EXUPH95,
            self.V8103553S2EXUPH95Time,
            self.V8103483S2EXProg,
            self.V8103483S2EXTest,
            self.V8103483S2EXLinecapa,
            self.V8103483S2EXEPI,
            self.V8103483S2EXBAAN1,
            self.V8103483S2EXComments,
            self.V8103483S2EXUPH85,
            self.V8103483S2EXUPH95,
            self.V8103483S2EXUPH95Time,
            self.V8108120S2Prog,
            self.V8108120S2Test,
            self.V8108120S2Linecapa,
            self.V8108120S2EPI,
            self.V8108120S2BAAN1,
            self.V8108120S2Comments,
            self.V8108120S2UPH85,
            self.V8108120S2UPH95,
            self.V8108120S2UPH95Time,
            self.V8103163Prog,
            self.V8103163Test,
            self.V8103163Linecapa,
            self.V8103163EPI,
            self.V8103163BAAN1,
            self.V8103163Comments,
            self.V8103163UPH85,
            self.V8103163UPH95,
            self.V8103163UPH95Time,
            self.dxUPH85,
            self.dxUPH95Time,
            self.dxUPH95,
            self.dxAlign,
            self.dxMap,
            self.dxAutoThickness,
            self.dxTest,
            self.dxBAAN1,
            self.V849Prog,
            self.V849Linecapa,
            self.V849EPI,
            self.V849Comments,
            self.V849HEX,
            self.V817Prog,
            self.V817Linecapa,
            self.V817EPI,
            self.V817Comments,
            self.V817HEX,
            self.ID,
        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def closeDB(self) -> None:
        self.dbCursor.close()
        self.db.close()


# def __del__(self): <-- in the Python the __del__ not always works
#    self.dbCursor.close()
#    self.db.close()
#    print("DB")
