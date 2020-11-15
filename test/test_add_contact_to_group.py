import random
from fixture.orm import ORMFixture
from model.group_form import GroupForm
from model.contact_form import ContactForm

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # Get groups and contacts list, make sure they are not empty
    db_groups_list = db.get_db_groups_list()
    db_contacts_list = db.get_db_contacts_list()
    if not db_groups_list:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
        db_groups_list = db.get_db_groups_list()
    if not db_contacts_list:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
        db_contacts_list = db.get_db_contacts_list()
    # Choose random group and contact
    group = random.choice(db_groups_list)
    contact = random.choice(db_contacts_list)
    # Check if the contact is not in the group. Options:
    # 1. The contact is not in the group - add it to the group.
    # 2. The contact is in the group - ok, choose another one, which is not in the group.
    # 3. All other contacts are also in the group, list db_contacts_not_in_group is empty - create contact and
    # add it to the group.
    db_contacts_in_group = orm.get_db_contacts_in_group(GroupForm(group_id=group.group_id))
    db_contacts_not_in_group = orm.get_db_contacts_not_in_group(GroupForm(group_id=group.group_id))
    if contact not in db_contacts_in_group:
        app.contact.add_contact_to_group(contact.contact_id, group.group_id)
    else:
        if db_contacts_not_in_group:
            contact = random.choice(db_contacts_not_in_group)
            app.contact.add_contact_to_group(contact.contact_id, group.group_id)
        else:
            if not db_contacts_not_in_group:
                contact = ContactForm(contact_name="AutocreatedContact")
                app.contact.create(contact)
                contact = db.get_db_contacts_list()[-1]
                app.contact.add_contact_to_group(contact.contact_id, group.group_id)
    # db - check the contact was added in the group
    db_contacts_in_group = orm.get_db_contacts_in_group(GroupForm(group_id=group.group_id))
    assert contact in db_contacts_in_group
