from model.contact_form import ContactForm


def testdata_create_contacts123(app):
    if app.contact.count() != 0:
        app.contact.del_all()
    contact1 = ContactForm(contact_name="1", contact_lastname="1")
    contact2 = ContactForm(contact_name="2", contact_lastname="2")
    contact3 = ContactForm(contact_name="3", contact_lastname="3")
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact.create(contact3)
