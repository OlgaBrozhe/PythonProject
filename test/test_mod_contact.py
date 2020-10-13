from model.contact_form import ContactForm


#def test_mod_first_contact(app):
 #   app.contact.mod_first(ContactForm("TestModUserName1", "TestModUserLastName1", "TestModUserEmail1", "TestModUserCompany", "TestModUserTelephoneMobile1"))

def test_mod_first_contact_name(app):
    # Check if any contact exist, and if not - create one, insert name
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Modify first contact name
    old_contacts_list = app.contact.get_contacts_list()
    # Write new id of the first group into old list for comparison purposes
    contact = ContactForm(contact_name="TestModContactName1")
    contact.contact_id = old_contacts_list[0].contact_id
    app.contact.mod_first(contact)
    new_contacts_list = app.contact.get_contacts_list()
    # First check if contact was modified meaning len is the same
    assert len(old_contacts_list) == len(new_contacts_list)
    # Second check, lists comparison
    old_contacts_list[0] = contact
    # Compare lists sorted by id ascending
    assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)

# def test_mod_first_contact_lastname(app):
#     # Check if any contact exist, and if not - create one, insert last name
#     if app.contact.count() == 0:
#         app.contact.create(ContactForm(contact_lastname="AutocreatedContact"))
#     # Modify first contact last name
#     old_contacts_list = app.contact.get_contacts_list()
#     # Write new id of the first group into old list for comparison purposes
#     contact = ContactForm(contact_lastname="TestModContactLastName1")
#     contact.contact_id = old_contacts_list[0].contact_id
#     app.contact.mod_first(contact)
#     new_contacts_list = app.contact.get_contacts_list()
#     # First check if contact was modified meaning len is the same
#     assert len(old_contacts_list) == len(new_contacts_list)
#     # Second check, lists comparison
#     old_contacts_list[0] = contact
#     # Compare lists sorted by id ascending
#     assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)

# def test_mod_first_contact_email(app):
#     # Check if any contact exist, and if not - create one, insert email
#     if app.contact.count() == 0:
#         app.contact.create(ContactForm(contact_email="AutocreatedContact"))
#     # Modify first contact email
#     app.contact.mod_first(ContactForm(contact_email="TestModContactEmail1"))
#
# def test_mod_first_contact_company(app):
#     # Check if any contact exist, and if not - create one, insert company
#     if app.contact.count() == 0:
#         app.contact.create(ContactForm(contact_company="AutocreatedContact"))
#     # Modify first contact company
#     app.contact.mod_first(ContactForm(contact_company="TestModContactCompany1"))
#
# def test_mod_first_contact_mobile(app):
#     # Check if any contact exist, and if not - create one, insert mobile
#     if app.contact.count() == 0:
#         app.contact.create(ContactForm(contact_mobile="AutocreatedContact"))
#     # Modify first contact mobile
#     app.contact.mod_first(ContactForm(contact_mobile="TestModContactMobile1"))