from model.contact_form import ContactForm


def test_add_contact(app):
    app.contact.create(ContactForm("TestUserName1", "TestUserLastName1", "TestUserEmail1", "TestUserCompany", "TestUserTelephoneMobile1"))
