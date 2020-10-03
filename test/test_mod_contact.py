from model.contact_form import ContactForm


def test_mod_first_contact(app):
    app.contact.mod_first(ContactForm("TestModUserName1", "TestModUserLastName1", "TestModUserEmail1", "TestModUserCompany", "TestModUserTelephoneMobile1"))