from model.contact_form import ContactForm
from random import randrange


def test_del_contact(app):
    # Check if any contact exist, and if not - create one
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Delete contact
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.del_by_index(index)
    new_contacts_list = app.contact.get_contacts_list()
    # First check - if contact was deleted at all
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    # Second check - if remained contacts are equal
    old_contacts_list[index:index+1] = []
    assert old_contacts_list == new_contacts_list
