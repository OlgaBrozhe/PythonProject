from model.contact_form import ContactForm
import random


def test_del_contact(app, db, check_ui):
    # Check if any contact exist, and if not - create one
    if db.get_db_contacts_list() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Delete random contact
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
        sorted_new_contacts_list = sorted(new_contacts_list, key=ContactForm.id_or_max)
        sorted_old_contacts_list = sorted(app.contact.get_contacts_list(), key=ContactForm.id_or_max)
        assert sorted_old_contacts_list == sorted_new_contacts_list
