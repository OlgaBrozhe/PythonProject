from model.contact_form import ContactForm


#def test_mod_first_contact(app):
 #   app.contact.mod_first(ContactForm("TestModUserName1", "TestModUserLastName1", "TestModUserEmail1", "TestModUserCompany", "TestModUserTelephoneMobile1"))

def test_mod_first_contact_name(app):
    # Check if any contact exist, and if not - create one, insert name
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Modify first contact name
    app.contact.mod_first(ContactForm(contact_name="TestModContactName1"))

def test_mod_first_contact_lastname(app):
    # Check if any contact exist, and if not - create one, insert last name
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_lastname="AutocreatedContact"))
    # Modify first contact last name
    app.contact.mod_first(ContactForm(contact_lastname="TestModContactLastName1"))

def test_mod_first_contact_email(app):
    # Check if any contact exist, and if not - create one, insert email
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_email="AutocreatedContact"))
    # Modify first contact email
    app.contact.mod_first(ContactForm(contact_email="TestModContactEmail1"))

def test_mod_first_contact_company(app):
    # Check if any contact exist, and if not - create one, insert company
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_company="AutocreatedContact"))
    # Modify first contact company
    app.contact.mod_first(ContactForm(contact_company="TestModContactCompany1"))

def test_mod_first_contact_mobile(app):
    # Check if any contact exist, and if not - create one, insert mobile
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_mobile="AutocreatedContact"))
    # Modify first contact mobile
    app.contact.mod_first(ContactForm(contact_mobile="TestModContactMobile1"))