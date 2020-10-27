from model.contact_form import ContactForm
import random
import string
import pytest
import re


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


def random_phone(prefix, maxlen):
    #symbols = string.digits*10 + string.punctuation + " "*10
    symbols = string.digits * 10 + " " * 10
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


testdata = [ContactForm(contact_name=random_string("CN__", 10), contact_lastname=random_string("CLN__",15),
                        contact_email=random_string("CE__@", 20), contact_email2=random_string("CE2__@", 20),
                        contact_homephone=random_phone("+", 15), contact_mobile=random_phone("+", 15),
                        contact_workphone=random_phone("+", 15), contact_secondary_phone=random_phone("+", 15))
            for i in range(5)]


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