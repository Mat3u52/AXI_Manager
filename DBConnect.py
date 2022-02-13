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

    def update(self, ID, item):
        self.ID = int(ID)
        self.item = str(item)
        sql = "UPDATE mk_diary SET ITEM = %s WHERE ITEM_ID = %s"
        val = (self.item, self.ID)
        self.dbCursor.execute(sql, val)
        #self.dbCursor.commit() # ???????

    def closeDB(self):
        self.dbCursor.close()
        self.db.close()