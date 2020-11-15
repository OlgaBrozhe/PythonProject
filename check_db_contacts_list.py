# from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group_form import GroupForm

#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # Get groups
    groups = db.get_db_groups_list()
    # for group in groups:
    #     print(group)
    # Get contacts
    contacts = db.get_db_contacts_list()
    # for contact in contacts:
    #     print(contact)
    # Get contacts not in the group
    # Insert group id
    input_group = input("Enter group id \n")
    contacts_not_in_group = db.get_db_contacts_not_in_group(GroupForm(group_id=input_group))
    contact_not_in_group_id = []
    for item in contacts_not_in_group:
        contact_not_in_group_id.append(item.contact_id)
    # Get groups with its contacts
    contacts_in_group = db.get_db_contacts_in_group(GroupForm(group_id=input_group))
    contact_in_group_id = []
    for item in contacts_in_group:
        contact_in_group_id.append(item.contact_id)
    print("There are " + str(len(contacts_in_group)) + " contacts in group " + str(input_group) + " . ID: " +
          str(contact_in_group_id))
    print("There are " + str(len(contacts_not_in_group)) + " contacts not in group " + str(input_group) + " . ID: " +
          str(contact_not_in_group_id))
    print("There are overall " + str(len(groups)) + " groups and " + str(len(contacts)) + " contacts in the database")
finally:
    #db.destroy()
    pass
