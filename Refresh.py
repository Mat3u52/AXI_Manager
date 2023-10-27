from DBConnect import DBConnect


class Refresh:
    def __init__(self) -> None:
        pass

    def baan_status(self, *args) -> None:
        status = None
        for baan_status in args:
            if baan_status == 'NO':
                status = 0
        return status


if __name__ == "__main__":
    obj_refresh = Refresh
    print(obj_refresh.baan_status('None', 'yes', 'NO'))
