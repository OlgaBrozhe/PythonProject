from model.contact_form import ContactForm
import pytest
import re
from data.data_contacts import testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(contact)
    # First check if contact was created
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_contacts_list.append(contact)
    assert sorted([clear(x) for x in old_contacts_list], key=ContactForm.id_or_max) == \
           sorted([clear(x) for x in new_contacts_list], key=ContactForm.id_or_max)


def clear(s):
    contact_name_cleared = re.sub("[() -]", "", s.contact_name)
    s.contact_name = contact_name_cleared
    contact_lastname_cleared = re.sub("[() -]", "", s.contact_lastname)
    s.contact_lastname = contact_lastname_cleared
    return s