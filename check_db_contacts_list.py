from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups_list = db.get_db_groups_list()
    for group in groups_list:
        print(group)
    print("The number of groups in the database is:")
    print(len(groups_list))
    contacts_list = db.get_db_contacts_list()
    for contact in contacts_list:
        print(contact)
    print("The number of contacts in the database is:")
    print(len(contacts_list))
finally:
    db.destroy()
