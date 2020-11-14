from model.contact_form import ContactForm
import random
import re


def test_del_contact(app, db, check_ui):
    # Check if any contact exist, and if not - create one
    old_contacts_list = db.get_db_contacts_list()
    if not old_contacts_list:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
        old_contacts_list = db.get_db_contacts_list()
    contact = random.choice(old_contacts_list)
    app.contact.del_by_id(contact.contact_id)
    new_contacts_list = db.get_db_contacts_list()
    # First check - if contact was deleted at all
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    # Second check - if remained contacts are equal
    old_contacts_list.remove(contact)
    assert old_contacts_list == new_contacts_list
    if check_ui:
        sorted_db_new_contacts_list = sorted([clear(x) for x in new_contacts_list], key=ContactForm.id_or_max)
        sorted_ui_new_contacts_list = sorted([clear(x) for x in app.contact.get_contacts_list()], key=ContactForm.id_or_max)
        assert sorted_db_new_contacts_list == sorted_ui_new_contacts_list

def clear(s):
    contact_name_cleared = re.sub("[() -]", "", s.contact_name)
    contact_lastname_cleared = re.sub("[() -]", "", s.contact_lastname)
    s.contact_name = contact_name_cleared
    s.contact_lastname = contact_lastname_cleared
    return s
