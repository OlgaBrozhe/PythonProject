from model.contact_form import ContactForm


def test_del_first_contact(app):
    # Check if any contact exist, and if not - create one
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="AutocreatedContact"))
    # Delete first contact
    app.contact.del_first()