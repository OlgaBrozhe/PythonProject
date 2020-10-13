from model.contact_form import ContactForm


def test_del_first_contact(app):
    # Check if any contact exist, and if not - create one
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Delete first contact
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.del_first()
    new_contacts_list = app.contact.get_contacts_list()
    # First check - if contact was deleted at all
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    # Second check - compare lists before and after deletion
    old_contacts_list[0:1] = []
    assert old_contacts_list == new_contacts_list