from time import sleep

import pymysql.cursors
from model.group_form import GroupForm


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit=True to clear cache after each query
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_db_groups_list(self):
        db_groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            # for row in cursor.fetchall():
            #     print(row)
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                db_groups_list.append(GroupForm(group_id=str(group_id), group_name=group_name,
                                                group_header=group_header, group_footer=group_footer))
        finally:
            cursor.close()
        return db_groups_list

    def destroy(self):
        self.connection.close()

