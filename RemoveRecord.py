from DBConnect import DBConnect


class RemoveRecord(DBConnect):
    
    def __init__(self, id_record: str) -> None:
        super().__init__()
        self.id_record: str = str(id_record)

    def remove_total(self):
        try:
            self.delete_by_id(self.id_record)
            print("removed")
        except:
            print("Record do not exist.")
