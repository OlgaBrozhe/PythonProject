from model.contact_form import ContactForm
from random import randrange
import re


def test_contact_info(app):
    # Check if any contact exist, and if not - create one
    if app.contact.count() == 0:
        app.contact.create(ContactForm(contact_name="TestName", contact_lastname="TestLastName",
                                       contact_address="TestAddress", contact_email="TestEmail",
                                       contact_email2="TestEmail2", contact_email3="TestEmail3",
                                       contact_company="TestCompany", contact_homephone="+14250000000",
                                       contact_mobile="+14250000001", contact_workphone="+14250000002",
                                       contact_fax="+14250000003", contact_secondary_phone="+14250000004"))
    # Choose random contact from contacts table
    contacts_table_list = app.contact.get_contacts_list()
    index = randrange(len(contacts_table_list))
    # Get contact info from contacts table
    contact_info_from_table = app.contact.get_contacts_list()[index]
    # Get contact info from Edit contact page
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # Compare contact info from contacts table to those on Edit page, plus hidden id
    assert contact_info_from_table.contact_id == contact_info_from_edit_page.contact_id
    assert contact_info_from_table.contact_name == contact_info_from_edit_page.contact_name
    assert contact_info_from_table.contact_lastname == contact_info_from_edit_page.contact_lastname
    assert contact_info_from_table.contact_address == contact_info_from_edit_page.contact_address
    # Compare emails and phone numbers from contacts table with those in Edit page, merged
    all_emails_from_home_page = contact_info_from_table.all_emails_from_home_page
    all_phones_from_home_page = contact_info_from_table.all_phones_from_home_page
    all_emails_from_edit_page = merge_emails_like_on_home_page(contact_info_from_edit_page)
    all_phones_from_edit_page = merge_phones_like_on_home_page(contact_info_from_edit_page)
    assert all_emails_from_home_page == all_emails_from_edit_page
    assert all_phones_from_home_page == all_phones_from_edit_page


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


def merge_emails_like_on_home_page(all_emails):
    # 1. Initial list [a,b,c]. 2. Filter - remove all None. 3. Filter - remove empty strings. 5. Join the rest with \n
    all_emails_joined = "\n".join(filter(lambda x: x != "",
                                         filter(lambda x: x is not None, [all_emails.contact_email,
                                                                          all_emails.contact_email2,
                                                                          all_emails.contact_email3])))
    return all_emails_joined


def clear(s):
    return re.sub("[() -]", "", s)
