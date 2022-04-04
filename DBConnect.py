import pymysql
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

    def selectSearchID(self,ID):
        self.ID = ID
        self.dbCursor.execute("SELECT * FROM mk_diary WHERE ITEM_ID LIKE '%"+self.ID+"%'")
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
        if vitroxIVTest > 0:
            self.vitroxIVUPH85 = (3600/(self.vitroxIVTest+15)*0.85)
            self.vitroxIVUPH95 = (3600/(self.vitroxIVTest+15)*0.95)
            self.vitroxIVUPH95Time = (3600/self.vitroxIVUPH95)

        sql = "UPDATE mk_diary SET ITEM = %s, ITEM_AMOUNT = %s, VITROXIV_PROG = %s, VITROXIV_TEST = %s, VITROXIV_LINECAPA = %s," \
              " VITROXIV_EPI = %s, VITROXIV_BAAN1 = %s, VITROXIV_COMMENTS = %s, VITROXIV_BAAN = %s," \
              " VITROXIV_DSVR = %s, VITROXIV_TIME = %s WHERE ITEM_ID = %s"
        val = (self.item, self.itemAmount, self.vitroxIVProg, self.vitroxIVTest, self.vitroxIVLinecapa, self.vitroxIVEPI,
               self.vitroxIVBAAN1, self.vitroxIVComments, self.vitroxIVUPH85, self.vitroxIVUPH95, self.vitroxIVUPH95Time, self.ID)
        self.dbCursor.execute(sql, val)
        self.db.commit()

    def insert(self, newItem):
        self.newItem = str(newItem)

    def closeDB(self):
        self.dbCursor.close()
        self.db.close()