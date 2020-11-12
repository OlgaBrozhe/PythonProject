# from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group_form import GroupForm

#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # Get groups
    groups = db.get_db_groups_list()
    for group in groups:
        print(group)
    print("The number of groups in the database is:")
    print(len(groups))
    # Get contacts
    contacts = db.get_db_contacts_list()
    for contact in contacts:
        print(contact)
    print("The number of contacts in the database is:")
    print(len(contacts))
    # Get groups with its contacts
    groups_with_contacts = db.get_db_contacts_in_group(GroupForm(group_id="499"))
    for contacts_in_group in groups_with_contacts:
        print(contacts_in_group)
    print("The number of contacts in the group is:")
    print(len(contacts_in_group))
finally:
    #db.destroy()
    pass
