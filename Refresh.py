from DBConnect import DBConnect


class Refresh:
    def __init__(self) -> None:
        pass

    def foreign_app_status(self, *args) -> bool:
        """
        The method is verifying the status of "_BAAN1, _LINECAPA, _EPI" in the DB.
        example: `5DX_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL

        :return: True - if status is no or lack and False otherwise
        :rtype: bool
        """
        status: bool = False
        container_ineligible: tuple = ("YES", "Yes", "yes", "NONE", "None", "none")
        container_eligible: tuple = ("NO", "No", "no", "LACK", "Lack", "lack")
        for app_status in args:
            if app_status not in container_ineligible \
                    and app_status is not None \
                    and app_status in container_eligible:
                status = True
        return status


if __name__ == "__main__":
    obj_refresh = Refresh
    print(obj_refresh.foreign_app_status('None', 'yes', '', None))


# row[11] != "YES"
# and row[11] != "NONE"
# and row[11] is not None
# and (row[11] == "NO" or row[11] == "LACK")
