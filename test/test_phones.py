import re


def test_contacts_phones_home_page(app):
    # First item from the list of contacts got from table of contacts
    phone_from_contacts_table = app.contact.get_contacts_list()[0]
    # First item from the contacts -> Info from Edit contact page
    phone_from_edit_contact_page = app.contact.get_contact_info_from_edit_page(0)
    # Compare phone numbers from contacts table with those in Edit page, cleared of other characters
    assert phone_from_contacts_table.contact_homephone == clear(phone_from_edit_contact_page.contact_homephone)
    assert phone_from_contacts_table.contact_mobile == clear(phone_from_edit_contact_page.contact_mobile)
    assert phone_from_contacts_table.contact_workphone == clear(phone_from_edit_contact_page.contact_workphone)
    assert phone_from_contacts_table.contact_secondary_phone == clear(phone_from_edit_contact_page.contact_secondary_phone)


def test_contacts_phones_view_page(app):
    # First item from the list of contacts got from table of contacts
    phone_from_view_contact_page = app.contact.get_contact_phones_from_view_page(0)
    # First item from the contacts -> Info from Edit contact page
    phone_from_edit_contact_page = app.contact.get_contact_info_from_edit_page(0)
    # Compare phone numbers from contacts table with those in Edit page, cleared of other characters
    assert phone_from_view_contact_page.contact_homephone == phone_from_edit_contact_page.contact_homephone
    assert phone_from_view_contact_page.contact_mobile == phone_from_edit_contact_page.contact_mobile
    assert phone_from_view_contact_page.contact_workphone == phone_from_edit_contact_page.contact_workphone
    assert phone_from_view_contact_page.contact_secondary_phone == phone_from_edit_contact_page.contact_secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)
