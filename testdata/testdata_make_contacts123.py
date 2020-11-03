from model.contact_form import ContactForm


def testdata_create_3_contacts(app):
    if app.contact.count() != 0:
        app.contact.del_all()
    contact_a_postfix = 1
    contact_b_postfix = int(contact_a_postfix)+1
    contact_c_postfix = int(contact_b_postfix)+1
    contact_a = ContactForm(contact_name=contact_a_postfix,
                            contact_lastname=contact_a_postfix,
                            contact_address=contact_a_postfix,
                            contact_email=contact_a_postfix,
                            contact_mobile=contact_a_postfix)
    contact_b = ContactForm(contact_name=contact_b_postfix,
                            contact_lastname=contact_b_postfix,
                            contact_address=contact_b_postfix,
                            contact_email=contact_b_postfix,
                            contact_mobile=contact_b_postfix)
    contact_c = ContactForm(contact_name=contact_c_postfix,
                            contact_lastname=contact_c_postfix,
                            contact_address=contact_c_postfix,
                            contact_email=contact_c_postfix,
                            contact_mobile=contact_c_postfix)
    app.contact.create(contact_a)
    app.contact.create(contact_b)
    app.contact.create(contact_c)
