from model.contact_form import ContactForm


def test_add_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    contact = ContactForm(contact_name="TestName", contact_lastname="TestLastName", contact_address="TestAddress",
                          contact_email="TestEmail", contact_company="TestCompany", contact_homephone="+14250000000",
                          contact_mobile="+14250000001", contact_workphone="+14250000002", contact_fax="+14250000003",
                          contact_secondary_phone="+14250000004")
    app.contact.create(contact)
    # First check if group was created
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    # Append old list with new item, sort lists ascending and check if they are still equal
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=ContactForm.id_or_max) == sorted(new_contacts_list, key=ContactForm.id_or_max)
