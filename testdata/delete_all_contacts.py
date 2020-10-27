from random import randrange


def test_del_contact(app):
    while app.contact.count() != 0:
        contacts_list = app.contact.get_contacts_list()
        index = randrange(len(contacts_list))
        app.contact.del_by_index(index)
