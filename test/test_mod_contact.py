from model.contact_form import ContactForm


#def test_mod_first_contact(app):
 #   app.contact.mod_first(ContactForm("TestModUserName1", "TestModUserLastName1", "TestModUserEmail1", "TestModUserCompany", "TestModUserTelephoneMobile1"))

def test_mod_first_contact_name(app):
    app.contact.mod_first(ContactForm(contact_name="TestModContactName1"))

def test_mod_first_contact_lastname(app):
    app.contact.mod_first(ContactForm(contact_lastname="TestModContactLastName1"))

def test_mod_first_contact_email(app):
    app.contact.mod_first(ContactForm(contact_email="TestModContactEmail1"))

def test_mod_first_contact_company(app):
    app.contact.mod_first(ContactForm(contact_company="TestModContactCompany1"))

def test_mod_first_contact_mobile(app):
    app.contact.mod_first(ContactForm(contact_mobile="TestModContactMobile1"))