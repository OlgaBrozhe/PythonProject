import random
from fixture.orm import ORMFixture
from model.group_form import GroupForm
from model.contact_form import ContactForm

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_remove_contact_from_group(app, db):
    # Make sure groups and contacts lists are not empty
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
    # Make sure the contact is in the group
    db_contacts_in_group = orm.get_db_contacts_in_group(GroupForm(group_id=group.group_id))
    if contact not in db_contacts_in_group:
        app.contact.add_contact_to_group(contact.contact_id, group.group_id)
    # Remove the contact from the group
    app.contact.remove_contact_from_group(contact.contact_id, group.group_id)
    assert contact not in db_contacts_in_group
