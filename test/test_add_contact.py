from model.contact_form import ContactForm
import re


def test_add_contact(app, json_data_contacts, db, check_ui):
    contact = json_data_contacts
    old_contacts_list = db.get_db_contacts_list()
    app.contact.create(contact)
    new_contacts_list = db.get_db_contacts_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_contacts_list.append(contact)
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