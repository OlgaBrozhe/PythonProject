#from datetime import datetime
from pony.orm import *
from model.group_form import GroupForm
from model.contact_form import ContactForm
from pymysql.converters import decoders


# ORM - object relational mapping
class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        group_id = PrimaryKey(int, column='group_id')
        group_name = Optional(str, column='group_name')
        group_header = Optional(str, column='group_header')
        group_footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        contact_id = PrimaryKey(int, column='id')
        contact_name = Optional(str, column='firstname')
        contact_lastname = Optional(str, column='lastname')
        contact_homephone = Optional(str, column='home')
        contact_mobile = Optional(str, column='mobile')
        contact_workphone = Optional(str, column='work')
        contact_email = Optional(str, column='email')
        contact_secondary_phone = Optional(str, column='phone2')
        #deprecated = Optional(datetime, column='deprecated')
        deprecated = Optional(str, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert_group(group):
            return GroupForm(group_id=str(group.group_id), group_name=group.group_name,
                             group_header=group.group_header, group_footer=group.group_footer)
        return list(map(convert_group, groups))

    def convert_contacts_to_model(self, contacts):
        def convert_contact(contact):
            return ContactForm(contact_id=str(contact.contact_id),
                               contact_name=contact.contact_name, contact_lastname=contact.contact_lastname,
                               contact_homephone=contact.contact_homephone, contact_mobile=contact.contact_mobile,
                               contact_workphone=contact.contact_workphone, contact_email=contact.contact_email,
                               contact_secondary_phone=contact.contact_secondary_phone)
        return list(map(convert_contact, contacts))

    @db_session
    def get_db_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
        # This will be the following query:
        # SELECT `g`.`group_id`, `g`.`group_name`, `g`.`group_header`, `g`.`group_footer`
        # FROM `group_list` `g`

    @db_session
    def get_db_contacts_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
        # This will be the following query:
        # GET CONNECTION FROM THE LOCAL POOL
        # SELECT `c`.`id`, `c`.`firstname`, `c`.`lastname`, `c`.`home`, `c`.`mobile`, `c`.`work`, `c`.`email`,
        # `c`.`phone2`, `c`.`deprecated`
        # FROM `addressbook` `c`
