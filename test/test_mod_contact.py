from model.contact_form import ContactForm
import random


def test_mod_contact_name(app, db):
    # Check if any contact exist, and if not - create one, insert name
    if db.get_db_contacts_list() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Modify random contact name
    old_contacts_list = db.get_db_contacts_list()
    contact_selected = random.choice(old_contacts_list)
    contact = ContactForm(contact_name="TestModContactName1")
    # Ensure other parameters of the modified item will remain
    contact.contact_id = contact_selected.contact_id
    contact.contact_lastname = contact_selected.contact_lastname
    app.contact.mod_by_id(contact.contact_id, contact)
    new_contacts_list = db.get_db_contacts_list()
    # First check if contact was modified meaning len is the same
    assert len(old_contacts_list) == len(new_contacts_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    for item in old_contacts_list:
        if item.contact_id == contact.contact_id:
            item.contact_name = contact.contact_name
    sorted_old_contacts_list = sorted(old_contacts_list, key=ContactForm.id_or_max)
    sorted_new_contacts_list = sorted(new_contacts_list, key=ContactForm.id_or_max)
    assert sorted_old_contacts_list == sorted_new_contacts_list


def test_mod_contact_lastname(app, db):
    # Check if any contact exist, and if not - create one, insert last name
    if db.get_db_contacts_list() == 0:
        app.contact.create(ContactForm(contact_lastname="AutocreatedContact"))
    # Modify random contact last name
    old_contacts_list = db.get_db_contacts_list()
    contact_selected = random.choice(old_contacts_list)
    contact = ContactForm(contact_lastname="TestModContactLastName1")
    # Ensure other parameters of the modified item will remain
    contact.contact_id = contact_selected.contact_id
    contact.contact_name = contact_selected.contact_name
    app.contact.mod_by_id(contact.contact_id, contact)
    new_contacts_list = db.get_db_contacts_list()
    # First check if contact was modified meaning len is the same
    assert len(old_contacts_list) == len(new_contacts_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    for item in old_contacts_list:
        if item.contact_id == contact.contact_id:
            item.contact_lastname = contact.contact_lastname
    sorted_old_contacts_list = sorted(old_contacts_list, key=ContactForm.id_or_max)
    sorted_new_contacts_list = sorted(new_contacts_list, key=ContactForm.id_or_max)
    assert sorted_old_contacts_list == sorted_new_contacts_list
