from model.contact_form import ContactForm
from random import randrange


def test_mod_contact_name(app):
    # Check if any contact exist, and if not - create one, insert name
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Modify random contact name
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    contact = ContactForm(contact_name="TestModContactName1")
    # Ensure other parameters of the modified item will remain
    contact.contact_id = old_contacts_list[index].contact_id
    contact.contact_lastname = old_contacts_list[index].contact_lastname
    app.contact.mod_by_index(index, contact)
    new_contacts_list = app.contact.get_contacts_list()
    # First check if contact was modified meaning len is the same
    assert len(old_contacts_list) == len(new_contacts_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    old_contacts_list[index] = contact
    assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)


def test_mod_contact_lastname(app):
    # Check if any contact exist, and if not - create one, insert last name
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_lastname="AutocreatedContact"))
    # Modify random contact last name
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    contact = ContactForm(contact_lastname="TestModContactLastName1")
    # Ensure other parameters of the modified item will remain
    contact.contact_id = old_contacts_list[index].contact_id
    contact.contact_name = old_contacts_list[index].contact_name
    app.contact.mod_by_index(index, contact)
    new_contacts_list = app.contact.get_contacts_list()
    # First check if contact was modified meaning len is the same
    assert len(old_contacts_list) == len(new_contacts_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    old_contacts_list[index] = contact
    assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)


#     self.change_field_value("firstname", contact_form.contact_name)
#     self.change_field_value("lastname", contact_form.contact_lastname)
#     self.change_field_value("email", contact_form.contact_email)
#     self.change_field_value("company", contact_form.contact_company)
#     self.change_field_value("home", contact_form.contact_homephone)
#     self.change_field_value("mobile", contact_form.contact_mobile)
#     self.change_field_value("work", contact_form.contact_workphone)
#     self.change_field_value("fax", contact_form.contact_fax)