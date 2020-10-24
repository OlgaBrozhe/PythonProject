import re


def test_contacts_phones_home_page(app):
    # First item from the list of contacts got from table of contacts
    phone_from_contacts_table = app.contact.get_contacts_list()[0]
    # First item from the contacts -> Info from Edit contact page
    phone_from_edit_contact_page = app.contact.get_contact_info_from_edit_page(0)
    # Compare phone numbers from contacts table with those in Edit page
    assert phone_from_contacts_table.all_phones_from_home_page == \
           merge_phones_like_on_home_page(phone_from_edit_contact_page)


def test_contacts_phones_view_page(app):
    phone_from_view_contact_page = app.contact.get_contact_phones_from_view_page(0)
    phone_from_edit_contact_page = app.contact.get_contact_info_from_edit_page(0)
    # Compare phone numbers from View page with those in Edit page
    assert phone_from_view_contact_page.contact_homephone == phone_from_edit_contact_page.contact_homephone
    assert phone_from_view_contact_page.contact_mobile == phone_from_edit_contact_page.contact_mobile
    assert phone_from_view_contact_page.contact_workphone == phone_from_edit_contact_page.contact_workphone
    assert phone_from_view_contact_page.contact_secondary_phone == phone_from_edit_contact_page.contact_secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(all_phones):
    # 1. Initial list [a,b,c,d]. 2. Filter - remove all None. 3. Clear unnecessary characters.
    # 4. Filter - remove empty strings. 5. Join the rest with \n
    all_phones_joined = "\n".join(filter(lambda x: x != "",
                                         map(lambda x: clear(x),
                                             filter(lambda x: x is not None, [all_phones.contact_homephone,
                                                                              all_phones.contact_mobile,
                                                                              all_phones.contact_workphone,
                                                                              all_phones.contact_secondary_phone]))))
    return all_phones_joined
