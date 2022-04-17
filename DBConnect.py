import pymysql
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
        #self.dbCursor.execute("SELECT * FROM mk_diary WHERE ITEM_ID LIKE '%"+self.ID+"%'")
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
            self.vitroxIVUPH85 = math.floor(3600/(float(self.vitroxIVTest)+15)*0.85)
            self.vitroxIVUPH95 = math.floor(3600/(float(self.vitroxIVTest)+15)*0.95)
            self.vitroxIVUPH95Time = (3600/float(self.vitroxIVUPH95))
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

    def insert(self, item, itemAmount,
               vitroxIVProg, vitroxIVTest, vitroxIVLinecapa, vitroxIVEPI, vitroxIVBAAN1, vitroxIVComments):

        #if item and type(itemAmount) == int:
        if item and int(itemAmount) > 0:
            self.item = str(item)
            self.itemAmount = int(itemAmount)

#-----------Vitrox IV----------------------------
            if vitroxIVProg and int(vitroxIVTest) > 0:
                self.vitroxIVProg = str(vitroxIVProg)
                self.vitroxIVTest = str(vitroxIVTest)
                self.vitroxIVLinecapa = str(vitroxIVLinecapa)
                self.vitroxIVEPI = str(vitroxIVEPI)
                self.vitroxIVBAAN1 = str(vitroxIVBAAN1)
                self.vitroxIVComments = str(vitroxIVComments)
                if float(vitroxIVTest) > 0:
                    self.vitroxIVUPH85 = math.floor(3600 / (float(self.vitroxIVTest) + 15) * 0.85)
                    self.vitroxIVUPH95 = math.floor(3600 / (float(self.vitroxIVTest) + 15) * 0.95)
                    self.vitroxIVUPH95Time = (3600 / float(self.vitroxIVUPH95))
                else:
                    self.vitroxIVTest = 0
                    self.vitroxIVUPH85 = 0
                    self.vitroxIVUPH95 = 0
                    self.vitroxIVUPH95Time = 0
            else:
                self.vitroxIVProg = ""
                self.vitroxIVTest = 0
                self.vitroxIVLinecapa = "NONE"
                self.vitroxIVEPI = "NONE"
                self.vitroxIVBAAN1 = "NONE"
                self.vitroxIVComments = ""
                self.vitroxIVUPH85 = 0
                self.vitroxIVUPH95 = 0
                self.vitroxIVUPH95Time = 0
#----------The End Vitrox IV----------

            self.vitroxIIIProg = ""
            self.vitroxIIITest = 0
            self.vitroxIIILinecapa = "NONE"
            self.vitroxIIIEPI = "NONE"
            self.vitroxIIIBAAN1 = "NONE"
            self.vitroxIIIComments = ""
            self.vitroxIIIUPH85 = 0
            self.vitroxIIIUPH95 = 0
            self.vitroxIIIUPH95Time = 0

            self.vitroxIIProg = ""
            self.vitroxIITest = 0
            self.vitroxIILinecapa = "NONE"
            self.vitroxIIEPI = "NONE"
            self.vitroxIIBAAN1 = "NONE"
            self.vitroxIIComments = ""
            self.vitroxIIUPH85 = 0
            self.vitroxIIUPH95 = 0
            self.vitroxIIUPH95Time = 0

            self.vitroxIProg = ""
            self.vitroxITest = 0
            self.vitroxILinecapa = "NONE"
            self.vitroxIEPI = "NONE"
            self.vitroxIBAAN1 = "NONE"
            self.vitroxIComments = ""
            self.vitroxIUPH85 = 0
            self.vitroxIUPH95 = 0
            self.vitroxIUPH95Time = 0

            self.vitroxIProg = ""
            self.vitroxITest = 0
            self.vitroxILinecapa = "NONE"
            self.vitroxIEPI = "NONE"
            self.vitroxIBAAN1 = "NONE"
            self.vitroxIComments = ""
            self.vitroxIUPH85 = 0
            self.vitroxIUPH95 = 0
            self.vitroxIUPH95Time = 0

            self.dxIProg = ""
            self.dxILinecapa = "NONE"
            self.dxIEPI = "NONE"
            self.dxIComments = ""
            self.dxIHEX = ""
            self.dxIIProg = ""
            self.dxIILinecapa = "NONE"
            self.dxIIEPI = "NONE"
            self.dxIIComments = ""
            self.dxIIHEX = ""
            self.dxBAAN1 = "NONE"
            self.dxUPH85 = 0
            self.dxUPH95 = 0
            self.dxUPH95Time = 0
            self.dxAlign = 0
            self.dxMap = 0
            self.dxAutoThickness = 0
            self.dxTest = 0


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

            self.vitroxIVProg, self.vitroxIVTest, self.vitroxIVLinecapa, self.vitroxIVEPI,
            self.vitroxIVBAAN1, self.vitroxIVComments, self.vitroxIVUPH85, self.vitroxIVUPH95, self.vitroxIVUPH95Time,

            self.vitroxIIIProg, self.vitroxIIITest, self.vitroxIIILinecapa, self.vitroxIIIEPI,
            self.vitroxIIIBAAN1, self.vitroxIIIComments, self.vitroxIIIUPH85, self.vitroxIIIUPH95, self.vitroxIIIUPH95Time,

            self.vitroxIIProg, self.vitroxIITest, self.vitroxIILinecapa, self.vitroxIIEPI,
            self.vitroxIIBAAN1, self.vitroxIIComments, self.vitroxIIUPH85, self.vitroxIIUPH95,
            self.vitroxIIUPH95Time,

            self.vitroxIProg, self.vitroxITest, self.vitroxILinecapa, self.vitroxIEPI,
            self.vitroxIBAAN1, self.vitroxIComments, self.vitroxIUPH85, self.vitroxIUPH95,
            self.vitroxIUPH95Time,

            self.dxUPH85, self.dxUPH95Time, self.dxUPH95, self.dxAlign, self.dxMap, self.dxAutoThickness,
            self.dxTest, self.dxBAAN1, self.dxIProg, self.dxILinecapa, self.dxIEPI, self.dxIComments,
            self.dxIHEX, self.dxIIProg, self.dxIILinecapa, self.dxIIEPI, self.dxIIComments, self.dxIIHEX

            )
            self.dbCursor.execute(sql, val)
            self.db.commit()

        else:
            print("Lack of Item and Qty")

    def closeDB(self):
        self.dbCursor.close()
        self.db.close()