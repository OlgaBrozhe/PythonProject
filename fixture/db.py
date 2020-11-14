import pymysql.cursors
from model.group_form import GroupForm
from model.contact_form import ContactForm


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

    def get_db_contacts_list(self):
        db_contacts_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('''select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 
            from addressbook where deprecated="0000-00-00 00:00:00"''')
            # for row in cursor.fetchall():
            #     print(row)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                db_contacts_list.append(ContactForm(contact_id=str(id), contact_name=firstname,
                                                    contact_lastname=lastname, contact_address=address,
                                                    contact_homephone=home, contact_mobile=mobile,
                                                    contact_workphone=work, contact_email=email, contact_email2=email2,
                                                    contact_email3=email3, contact_secondary_phone=phone2))
        finally:
            cursor.close()
        return db_contacts_list

    def destroy(self):
        self.connection.close()
