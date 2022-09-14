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

    def insertValidator(self, item, itemAmount,
               initialV8103553S2EXProg, initialV8103553S2EXTest, initialV8103553S2EXLinecapa, initialV8103553S2EXEPI, initialV8103553S2EXBAAN1, initialV8103553S2EXComments,
               initialV8103483S2EXProg, initialV8103483S2EXTest, initialV8103483S2EXLinecapa, initialV8103483S2EXEPI, initialV8103483S2EXBAAN1, initialV8103483S2EXComments,
               initialV8103163Prog, initialV8103163Test, initialV8103163Linecapa, initialV8103163EPI, initialV8103163BAAN1, initialV8103163Comments,
               initialV8108120S2Prog, initialV8108120S2Test, initialV8108120S2Linecapa, initialV8108120S2EPI, initialV8108120S2BAAN1, initialV8108120S2Comments,

                initialDXUPH85, initialDXUPH95Time, initialDXUPH95,

                initialAlignTime, initialLaserTime, initialThicknessTime, initialTestTime,

                initialBaan5DXStatus,

                initialProgV849, initialV849Linecapa, initialV849EPI, initialCommentsV849, initialHexV849,

                initialProgV817, initialV817Linecapa, initialV817EPI, initialCommentsV817, initialHexV817
                        ):
        if item and int(itemAmount) > 0:
            self.item = str(item.strip())
            self.itemAmount = int(itemAmount)

            # --- ViTrox IV ---
            if initialV8103553S2EXProg and int(initialV8103553S2EXTest) > 0:
                self.V8103553S2EXProg = str(initialV8103553S2EXProg.strip())
                self.V8103553S2EXTest = str(initialV8103553S2EXTest)
                self.V8103553S2EXLinecapa = str(initialV8103553S2EXLinecapa)
                self.V8103553S2EXEPI = str(initialV8103553S2EXEPI)
                self.V8103553S2EXBAAN1 = str(initialV8103553S2EXBAAN1)
                self.V8103553S2EXComments = str(initialV8103553S2EXComments)
                if float(self.V8103553S2EXTest) > 0:
                    self.V8103553S2EXUPH85 = math.floor((3600 / (float(self.V8103553S2EXTest) + 15) * 0.85)) * int(
                        self.itemAmount)
                    self.V8103553S2EXUPH95 = math.floor((3600 / (float(self.V8103553S2EXTest) + 15) * 0.95)) * int(
                        self.itemAmount)
                    self.V8103553S2EXUPH95Time = ((3600 / float(self.V8103553S2EXUPH95)) / int(self.itemAmount))
                else:
                    self.V8103553S2EXTest = 0
                    self.V8103553S2EXUPH85 = 0
                    self.V8103553S2EXUPH95 = 0
                    self.V8103553S2EXUPH95Time = 0
            else:
                self.V8103553S2EXProg = ""
                self.V8103553S2EXTest = 0
                self.V8103553S2EXLinecapa = "NONE"
                self.V8103553S2EXEPI = "NONE"
                self.V8103553S2EXBAAN1 = "NONE"
                self.V8103553S2EXComments = ""
                self.V8103553S2EXUPH85 = 0
                self.V8103553S2EXUPH95 = 0
                self.V8103553S2EXUPH95Time = 0
            # --- The End ViTrox IV ---
            # --- ViTrox III ---
            if initialV8103483S2EXProg and int(initialV8103483S2EXTest) > 0:
                self.V8103483S2EXProg = str(initialV8103483S2EXProg.strip())
                self.V8103483S2EXTest = str(initialV8103483S2EXTest)
                self.V8103483S2EXLinecapa = str(initialV8103483S2EXLinecapa)
                self.V8103483S2EXEPI = str(initialV8103483S2EXEPI)
                self.V8103483S2EXBAAN1 = str(initialV8103483S2EXBAAN1)
                self.V8103483S2EXComments = str(initialV8103483S2EXComments)
                if float(self.V8103483S2EXTest) > 0:
                    self.V8103483S2EXUPH85 = math.floor((3600 / (float(self.V8103483S2EXTest) + 15) * 0.85)) * int(
                        self.itemAmount)
                    self.V8103483S2EXUPH95 = math.floor((3600 / (float(self.V8103483S2EXTest) + 15) * 0.95)) * int(
                        self.itemAmount)
                    self.V8103483S2EXUPH95Time = ((3600 / float(self.V8103483S2EXUPH95)) / int(self.itemAmount))
                else:
                    self.V8103483S2EXTest = 0
                    self.V8103483S2EXUPH85 = 0
                    self.V8103483S2EXUPH95 = 0
                    self.V8103483S2EXUPH95Time = 0
            else:
                self.V8103483S2EXProg = ""
                self.V8103483S2EXTest = 0
                self.V8103483S2EXLinecapa = "NONE"
                self.V8103483S2EXEPI = "NONE"
                self.V8103483S2EXBAAN1 = "NONE"
                self.V8103483S2EXComments = ""
                self.V8103483S2EXUPH85 = 0
                self.V8103483S2EXUPH95 = 0
                self.V8103483S2EXUPH95Time = 0
            # --- The End ViTrxo III ---
            # --- ViTrox XXL ---
            if initialV8108120S2Prog and int(initialV8108120S2Test) > 0:
                self.V8108120S2Prog = str(initialV8108120S2Prog.strip())
                self.V8108120S2Test = str(initialV8108120S2Test)
                self.V8108120S2Linecapa = str(initialV8108120S2Linecapa)
                self.V8108120S2EPI = str(initialV8108120S2EPI)
                self.V8108120S2BAAN1 = str(initialV8108120S2BAAN1)
                self.V8108120S2Comments = str(initialV8108120S2Comments)
                if float(self.V8108120S2Test) > 0:
                    self.V8108120S2UPH85 = math.floor((3600 / (float(self.V8108120S2Test) + 15) * 0.85)) * int(
                        self.itemAmount)
                    self.V8108120S2UPH95 = math.floor((3600 / (float(self.V8108120S2Test) + 15) * 0.95)) * int(
                        self.itemAmount)
                    self.V8108120S2UPH95Time = ((3600 / float(self.V8108120S2UPH95)) / int(self.itemAmount))
                else:
                    self.V8108120S2Test = 0
                    self.V8108120S2UPH85 = 0
                    self.V8108120S2UPH95 = 0
                    self.V8108120S2UPH95Time = 0
            else:
                self.V8108120S2Prog = ""
                self.V8108120S2Test = 0
                self.V8108120S2Linecapa = "NONE"
                self.V8108120S2EPI = "NONE"
                self.V8108120S2BAAN1 = "NONE"
                self.V8108120S2Comments = ""
                self.V8108120S2UPH85 = 0
                self.V8108120S2UPH95 = 0
                self.V8108120S2UPH95Time = 0
            # --- The End ViTrox XXL ---
            # --- ViTroxEx I ---
            if initialV8103163Prog and int(initialV8103163Test) > 0:
                self.V8103163Prog = str(initialV8103163Prog.strip())
                self.V8103163Test = str(initialV8103163Test)
                self.V8103163Linecapa = str(initialV8103163Linecapa)
                self.V8103163EPI = str(initialV8103163EPI)
                self.V8103163BAAN1 = str(initialV8103163BAAN1)
                self.V8103163Comments = str(initialV8103163Comments)
                if float(self.V8103163Test) > 0:
                    self.V8103163UPH85 = math.floor((3600 / (float(self.V8103163Test) + 15) * 0.85)) * int(
                        self.itemAmount)
                    self.V8103163UPH95 = math.floor((3600 / (float(self.V8103163Test) + 15) * 0.95)) * int(
                        self.itemAmount)
                    self.V8103163UPH95Time = ((3600 / float(self.V8103163UPH95)) / int(self.itemAmount))
                else:
                    self.V8103163Test = 0
                    self.V8103163UPH85 = 0
                    self.V8103163UPH95 = 0
                    self.V8103163UPH95Time = 0
            else:
                self.V8103163Prog = ""
                self.V8103163Test = 0
                self.V8103163Linecapa = "NONE"
                self.V8103163EPI = "NONE"
                self.V8103163BAAN1 = "NONE"
                self.V8103163Comments = ""
                self.V8103163UPH85 = 0
                self.V8103163UPH95 = 0
                self.V8103163UPH95Time = 0
            # --- The End ViTrox I ---

            # --- 5DX I & II ---
            if (initialProgV849 and int(initialTestTime) > 0) or \
                    (initialProgV817 and int(initialTestTime) > 0):
                self.V849Prog = str(initialProgV849)
                self.V849Linecapa = str(initialV849Linecapa)
                self.V849EPI = str(initialV849EPI)
                self.V849Comments = str(initialCommentsV849)
                self.V849HEX = str(initialHexV849)

                self.V817Prog = str(initialProgV817)
                self.V817Linecapa = str(initialV817Linecapa)
                self.V817EPI = str(initialV817EPI)
                self.V817Comments = str(initialCommentsV817)
                self.V817HEX = str(initialHexV817)

                self.dxBAAN1 = str(initialBaan5DXStatus)
                self.dxUPH85 = int(initialDXUPH85)
                self.dxUPH95 = int(initialDXUPH95)
                self.dxUPH95Time = int(initialDXUPH95Time)
                self.dxAlign = int(initialAlignTime)
                self.dxMap = int(initialLaserTime)
                self.dxAutoThickness = int(initialThicknessTime)
                self.dxTest = int(initialTestTime)

            else:
                self.V849Prog = ""
                self.V849Linecapa = "NONE"
                self.V849EPI = "NONE"
                self.V849Comments = ""
                self.V849HEX = ""

                self.V817Prog = ""
                self.V817Linecapa = "NONE"
                self.V817EPI = "NONE"
                self.V817Comments = ""
                self.V817HEX = ""

                self.dxBAAN1 = "NONE"
                self.dxUPH85 = 0
                self.dxUPH95 = 0
                self.dxUPH95Time = 0
                self.dxAlign = 0
                self.dxMap = 0
                self.dxAutoThickness = 0
                self.dxTest = 0
            # --- The End 5DX I & II ---

            messagebox.showwarning("Awesome!", "The record is added :)")
            self._insert()
        else:
            messagebox.showwarning("Warning!", "Lack of Item or Qty.")

    #def insert(self, item, itemAmount,
    #           initialV8103553S2EXProg, initialV8103553S2EXTest, initialV8103553S2EXLinecapa, initialV8103553S2EXEPI, initialV8103553S2EXBAAN1, initialV8103553S2EXComments,
    #           initialV8103483S2EXProg, initialV8103483S2EXTest, initialV8103483S2EXLinecapa, initialV8103483S2EXEPI, initialV8103483S2EXBAAN1, initialV8103483S2EXComments,
    #           initialV8103163Prog, initialV8103163Test, initialV8103163Linecapa, initialV8103163EPI, initialV8103163BAAN1, initialV8103163Comments):
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

    def closeDB(self):
        self.dbCursor.close()
        self.db.close()
#def __del__(self):
#    self.dbCursor.close()
#    self.db.close()
#    print("DB")
