from DBConnect import DBConnect


class RemoveRecord(DBConnect):
    
    def __init__(self, id_record: int) -> None:
        super().__init__()
        self.id_record: int = int(id_record)

    def remove_total(self):
        pass
