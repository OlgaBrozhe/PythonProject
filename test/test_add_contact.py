from model.contact_form import ContactForm


def test_add_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    contact = ContactForm("TestUserName1", "TestUserLastName1", "TestUserEmail1", "TestUserCompany", "TestUserTelephoneMobile1")
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contacts_list()
    # First check if group was created
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    # Append old list with new item, sort lists ascending and check if they are still equal
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)