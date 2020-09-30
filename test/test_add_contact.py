from model.contact_form import ContactForm


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(ContactForm("TestUserName1", "TestUserLastName1", "TestUserEmail1", "TestUserCompany", "TestUserTelephoneMobile1"))
    app.session.logout()
