import pymysql
from tkinter import messagebox
import math
class DBConnect:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='mk_database',
                             charset='utf8mb4')
        self.dbCursor = self.db.cursor()

    def selectAll(self):
        self.dbCursor.execute("SELECT * FROM mk_diary ORDER BY ITEM ASC")
        records = self.dbCursor.fetchall()
        return records

    def selectSearchID(self, ID):
        self.ID = ID
        self.dbCursor.execute("SELECT * FROM mk_diary WHERE ITEM_ID LIKE "+self.ID+"")
        records = self.dbCursor.fetchall()
        return records

    def selectSearchItem(self, item):
        self.item = item
        self.dbCursor.execute("SELECT * FROM mk_diary WHERE ITEM LIKE %s LIMIT 1", (self.item))
        records = self.dbCursor.fetchall()
        return records

    def update(self, ID, item, itemAmount, vitroxIVProg, vitroxIVTest, vitroxIVLinecapa, vitroxIVEPI, vitroxIVBAAN1, vitroxIVComments):
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
            self.vitroxIVUPH85 = math.floor((3600/(float(self.vitroxIVTest)+15)*0.85)) * int(self.itemAmount)
            self.vitroxIVUPH95 = math.floor((3600/(float(self.vitroxIVTest)+15)*0.95)) * int(self.itemAmount)
            self.vitroxIVUPH95Time = ((3600/float(self.vitroxIVUPH95)) / int(self.itemAmount))
        else:
            self.vitroxIVUPH85 = 0
            self.vitroxIVUPH95 = 0
            self.vitroxIVUPH95Time = 0

        sql = "UPDATE mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, " \
                "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s," \
                " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s," \
                " VITROXIV_DSVR = %s, VITROXIV_TIME = %s " \
                "WHERE ITEM_ID = %s"
        val = (self.item, self.itemAmount, self.vitroxIVProg, self.vitroxIVTest, self.vitroxIVLinecapa, self.vitroxIVEPI,
                self.vitroxIVBAAN1, self.vitroxIVComments, self.vitroxIVUPH85, self.vitroxIVUPH95, self.vitroxIVUPH95Time, self.ID)
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def switch(self, x):
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

    def insert(self, initDevice, initStatus, initItem, initAmount,
               initProg, initTest, initLinecapa, initEPI, initBAAN1, initComments, initUPH85, initUPH95, initUPH95Time,
               initStatusDevice = False,

               initAlignTime = 0, initLaserTime = 0, initThicknessTime = 0, initTotalTest = 0,
               initStatus5DX = False,
               initProg5DX = "", initTest5DX = 0, initLinecapa5DX = "NONE", initEPI5DX = "NONE", initBAAN15DX = "NONE",
               initComments5DX = "", initUPH855DX = 0, initUPH955DX = 0, initUPH95Time5DX = 0,
               initAlignTime5DX = 0, initLaserTime5DX = 0, initThicknessTime5DX = 0, initTotalTest5DX = 0):

        if initDevice and initStatus and initItem and initAmount \
                and (initStatusDevice == True or initStatus5DX == True):
            self.device = initDevice
            self.status = initStatus
            self.item = initItem
            self.itemAmount = initAmount
            messagebox.showwarning("OK!", f"Flag Item: {initStatus}\n Flag prog: {initStatusDevice}")
            self.flag = False

            self.devices = ('V849_V817', 'V810-3163', 'V810-3483S2EX', 'V810-3553S2EX', 'V810-8120S2')

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

            self.dxUPH85 = 0 #common
            self.dxUPH95Time = 0 #common
            self.dxUPH95 = 0 #common

            self.dxAlign = 0 #added
            self.dxMap = 0 #added
            self.dxAutoThickness = 0 #added
            self.dxTest = 0


            self.dxBAAN1 = "NONE" #common


            self.V849Prog = ""
            self.V849Linecapa = "NONE"
            self.V849EPI = "NONE"
            self.V849Comments = ""
            self.V849HEX = "" #added

            self.V817Prog = ""
            self.V817Linecapa = "NONE"
            self.V817EPI = "NONE"
            self.V817Comments = ""
            self.V817HEX = "" #added



            for self.machine in self.devices:
                if self.machine == self.device:
                    print(self.device)
                    print(self.status)
                    print(self.item)
                    print(self.itemAmount)

                    if self.selectSearchItem(self.item):
                        print("exist")
                        for self.row in self.selectSearchItem(self.item):
                            print(f"From DB:")
                            print(f"db item: {self.row[1]}")
                            msgBox = messagebox.askquestion("The record already exist in DB!", f"Existing Item: {self.row[1]}\n\n "
                                                    f"Amount of the PCB in panel: {self.row[3]}\n\n "
                                                    f"V810-3553S2EX: {self.row[54]} Scanning Time: {self.row[52]}\n "
                                                    f"V810-3483S2EX: {self.row[45]} Scanning Time: {self.row[50]}\n "
                                                    f"V810-8120S2: {self.row[31]} Scanning Time: {self.row[35]}\n "
                                                    f"V849: {self.row[17]}\n "
                                                    f"V817: {self.row[22]}")
                            if msgBox == 'yes':
                                print("update!!!!!!!")
                            else:
                                print("NOT update")

                            self.flag = True
                    else:
                        print("not exist")
                        if self.device == 'V810-3553S2EX':
                            self.V8103553S2EXProg = initProg
                            self.V8103553S2EXTest = initTest
                            self.V8103553S2EXLinecapa = initLinecapa
                            self.V8103553S2EXEPI = initEPI
                            self.V8103553S2EXBAAN1 = initBAAN1
                            self.V8103553S2EXComments = initComments
                            self.V8103553S2EXUPH85 = initUPH85
                            self.V8103553S2EXUPH95 = initUPH95
                            self.V8103553S2EXUPH95Time = initUPH95Time
                        elif self.device == 'V810-3483S2EX':
                            self.V8103483S2EXProg = initProg
                            self.V8103483S2EXTest = initTest
                            self.V8103483S2EXLinecapa = initLinecapa
                            self.V8103483S2EXEPI = initEPI
                            self.V8103483S2EXBAAN1 = initBAAN1
                            self.V8103483S2EXComments = initComments
                            self.V8103483S2EXUPH85 = initUPH85
                            self.V8103483S2EXUPH95 = initUPH95
                            self.V8103483S2EXUPH95Time = initUPH95Time
                        elif self.device == 'V810-8120S2':
                            self.V8108120S2Prog = initProg
                            self.V8108120S2Test = initTest
                            self.V8108120S2Linecapa = initLinecapa
                            self.V8108120S2EPI = initEPI
                            self.V8108120S2BAAN1 = initBAAN1
                            self.V8108120S2Comments = initComments
                            self.V8108120S2UPH85 = initUPH85
                            self.V8108120S2UPH95 = initUPH95
                            self.V8108120S2UPH95Time = initUPH95Time
                        elif self.device == 'V810-3163':
                            self.V8103163Prog = initProg
                            self.V8103163Test = initTest
                            self.V8103163Linecapa = initLinecapa
                            self.V8103163EPI = initEPI
                            self.V8103163BAAN1 = initBAAN1
                            self.V8103163Comments = initComments
                            self.V8103163UPH85 = initUPH85
                            self.V8103163UPH95 = initUPH95
                            self.V8103163UPH95Time = initUPH95Time
                        elif self.device == 'V849_V817':

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

                            print(self.V849Prog)
                            print(self.V849Linecapa)
                            print(self.V849EPI)
                            print(self.V849Comments)
                            print(self.V849HEX)

                            print(self.V817Prog)
                            print(self.V817Linecapa)
                            print(self.V817EPI)
                            print(self.V817Comments)
                            print(self.V817HEX)

                            if initTotalTest >= initTotalTest5DX:
                                #5dx 1

                                self.dxAlign = initAlignTime
                                self.dxMap = initLaserTime
                                self.dxAutoThickness = initThicknessTime
                                self.dxTest = initTest

                                self.dxUPH85 = initUPH85
                                self.dxUPH95Time = initUPH95Time
                                self.dxUPH95 = initUPH95

                            else:
                                #5dx 2

                                self.dxAlign = initAlignTime5DX
                                self.dxMap = initLaserTime5DX
                                self.dxAutoThickness = initThicknessTime5DX
                                self.dxTest = initTest5DX

                                self.dxUPH85 = initUPH855DX
                                self.dxUPH95Time = initUPH95Time5DX
                                self.dxUPH95 = initUPH955DX


                            if int(self.switch(initBAAN1)) >= int(self.switch(initBAAN15DX)):
                                self.initBAAN1 = initBAAN1
                            else:
                                self.initBAAN1 = initBAAN15DX

                            print(self.initBAAN1)

                            print(self.dxAlign)
                            print(self.dxMap)
                            print(self.dxAutoThickness)
                            print(self.dxTest)
                            print(self.dxUPH85)
                            print(self.dxUPH95)
                            print(self.dxUPH95Time)

                        messagebox.showwarning("Awesome!", "The record is added :)")
                        self.flag = False

                    #print(self.flag)


            #self._insert()


    def _insert(self):
        sql = "INSERT mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, " \
                    "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s," \
                    " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s," \
                    " VITROXIV_DSVR = %s, VITROXIV_TIME = %s," \
                    " VITROXIII_PROG = %s, VITROXIII_TEST = %s, VITROXIII_LINECAPA = %s," \
                    " VITROXIII_EPI = %s, VITROXIII_BAAN1 = %s, VITROXIII_COMMENTS = %s, VITROXIII_BAAN = %s," \
                    " VITROXIII_DSVR = %s, VITROXIII_TIME = %s," \
                    " VITROXII_PROG = %s, VITROXII_TEST = %s, VITROXII_LINECAPA = %s," \
                    " VITROXII_EPI = %s, VITROXII_BAAN1 = %s, VITROXII_COMMENTS = %s, VITROXII_BAAN = %s," \
                    " VITROXII_DSVR = %s, VITROXII_TIME = %s," \
                    " VITROXI_PROG = %s, VITROX_TEST = %s, VITROXI_LINECAPA = %s," \
                    " VITROXI_EPI = %s, VITROX_BAAN1 = %s, VITROXI_COMMENTS = %s, VITROX_BAAN = %s," \
                    " VITROX_DSVR = %s, VITROX_TIME = %s," \
                    " 5DX_BAAN = %s, 5DX_TIME = %s, 5DX_DSVR = %s, 5DX_ALIGN = %s, 5DX_MAP = %s, 5DX_AUTO_THICKNESS = %s," \
                    " 5DX_TEST = %s, 5DX_BAAN1 = %s, 5DXI_PROG = %s, 5DXI_LINECAPA = %s, 5DXI_EPI = %s," \
                    " 5DXI_COMMENTS = %s, HEXI = %s, 5DXII_PROG = %s, 5DXII_LINECAPA = %s, 5DXII_EPI = %s," \
                    " 5DXII_COMMENTS = %s, HEXII = %s"
        val = (
            self.item, self.itemAmount,

            self.V8103553S2EXProg, self.V8103553S2EXTest, self.V8103553S2EXLinecapa, self.V8103553S2EXEPI,
            self.V8103553S2EXBAAN1, self.V8103553S2EXComments, self.V8103553S2EXUPH85, self.V8103553S2EXUPH95,
            self.V8103553S2EXUPH95Time,

            self.V8103483S2EXProg, self.V8103483S2EXTest, self.V8103483S2EXLinecapa, self.V8103483S2EXEPI,
            self.V8103483S2EXBAAN1, self.V8103483S2EXComments, self.V8103483S2EXUPH85, self.V8103483S2EXUPH95,
            self.V8103483S2EXUPH95Time,

            self.V8108120S2Prog, self.V8108120S2Test, self.V8108120S2Linecapa, self.V8108120S2EPI,
            self.V8108120S2BAAN1, self.V8108120S2Comments, self.V8108120S2UPH85, self.V8108120S2UPH95,
            self.V8108120S2UPH95Time,

            self.V8103163Prog, self.V8103163Test, self.V8103163Linecapa, self.V8103163EPI,
            self.V8103163BAAN1, self.V8103163Comments, self.V8103163UPH85, self.V8103163UPH95, self.V8103163UPH95Time,

            self.dxUPH85, self.dxUPH95Time, self.dxUPH95, self.dxAlign, self.dxMap, self.dxAutoThickness,
            self.dxTest, self.dxBAAN1, self.V849Prog, self.V849Linecapa, self.V849EPI, self.V849Comments,
            self.V849HEX, self.V817Prog, self.V817Linecapa, self.V817EPI, self.V817Comments, self.V817HEX

        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def _update(self):
        sql = "UPDATE mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, " \
                  "VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s," \
                  " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s," \
                  " VITROXIV_DSVR = %s, VITROXIV_TIME = %s," \
                  " VITROXIII_PROG = %s, VITROXIII_TEST = %s, VITROXIII_LINECAPA = %s," \
                  " VITROXIII_EPI = %s, VITROXIII_BAAN1 = %s, VITROXIII_COMMENTS = %s, VITROXIII_BAAN = %s," \
                  " VITROXIII_DSVR = %s, VITROXIII_TIME = %s," \
                  " VITROXII_PROG = %s, VITROXII_TEST = %s, VITROXII_LINECAPA = %s," \
                  " VITROXII_EPI = %s, VITROXII_BAAN1 = %s, VITROXII_COMMENTS = %s, VITROXII_BAAN = %s," \
                  " VITROXII_DSVR = %s, VITROXII_TIME = %s," \
                  " VITROXI_PROG = %s, VITROX_TEST = %s, VITROXI_LINECAPA = %s," \
                  " VITROXI_EPI = %s, VITROX_BAAN1 = %s, VITROXI_COMMENTS = %s, VITROX_BAAN = %s," \
                  " VITROX_DSVR = %s, VITROX_TIME = %s," \
                  " 5DX_BAAN = %s, 5DX_TIME = %s, 5DX_DSVR = %s, 5DX_ALIGN = %s, 5DX_MAP = %s, 5DX_AUTO_THICKNESS = %s," \
                  " 5DX_TEST = %s, 5DX_BAAN1 = %s, 5DXI_PROG = %s, 5DXI_LINECAPA = %s, 5DXI_EPI = %s," \
                  " 5DXI_COMMENTS = %s, HEXI = %s, 5DXII_PROG = %s, 5DXII_LINECAPA = %s, 5DXII_EPI = %s," \
                  " 5DXII_COMMENTS = %s, HEXII = %s"
        val = (
                self.item, self.itemAmount,

                self.V8103553S2EXProg, self.V8103553S2EXTest, self.V8103553S2EXLinecapa, self.V8103553S2EXEPI,
                self.V8103553S2EXBAAN1, self.V8103553S2EXComments, self.V8103553S2EXUPH85, self.V8103553S2EXUPH95,
                self.V8103553S2EXUPH95Time,

                self.V8103483S2EXProg, self.V8103483S2EXTest, self.V8103483S2EXLinecapa, self.V8103483S2EXEPI,
                self.V8103483S2EXBAAN1, self.V8103483S2EXComments, self.V8103483S2EXUPH85, self.V8103483S2EXUPH95,
                self.V8103483S2EXUPH95Time,

                self.V8108120S2Prog, self.V8108120S2Test, self.V8108120S2Linecapa, self.V8108120S2EPI,
                self.V8108120S2BAAN1, self.V8108120S2Comments, self.V8108120S2UPH85, self.V8108120S2UPH95,
                self.V8108120S2UPH95Time,

                self.V8103163Prog, self.V8103163Test, self.V8103163Linecapa, self.V8103163EPI,
                self.V8103163BAAN1, self.V8103163Comments, self.V8103163UPH85, self.V8103163UPH95,
                self.V8103163UPH95Time,

                self.dxUPH85, self.dxUPH95Time, self.dxUPH95, self.dxAlign, self.dxMap, self.dxAutoThickness,
                self.dxTest, self.dxBAAN1, self.V849Prog, self.V849Linecapa, self.V849EPI, self.V849Comments,
                self.V849HEX, self.V817Prog, self.V817Linecapa, self.V817EPI, self.V817Comments, self.V817HEX

        )
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def closeDB(self):
        self.dbCursor.close()
        self.db.close()
#def __del__(self):
#    self.dbCursor.close()
#    self.db.close()
#    print("DB")
