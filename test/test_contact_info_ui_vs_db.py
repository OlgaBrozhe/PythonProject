from model.contact_form import ContactForm
import re


def test_contact_info(app, db):
    # Check in DB if any contact exist, and if not - create one
    db_contacts_list = db.get_db_contacts_list()
    if not db_contacts_list:
        app.contact.create(ContactForm(contact_name="TestName", contact_lastname="TestLastName",
                                       contact_address="TestAddress", contact_email="TestEmail",
                                       contact_email2="TestEmail2", contact_email3="TestEmail3",
                                       contact_homephone="+14250000000", contact_mobile="+14250000001",
                                       contact_workphone="+14250000002", contact_secondary_phone="+14250000004"))
        db_contacts_list = db.get_db_contacts_list()
    # Get contacts from UI home page
    ui_contacts_list = app.contact.get_contacts_list()
    # Compare len of the lists
    assert len(db_contacts_list) == len(ui_contacts_list)
    # Sort and clear
    db_contacts_list = sorted([clear_object(x) for x in db_contacts_list], key=ContactForm.id_or_max)
    ui_contacts_list = sorted([clear_object(x) for x in ui_contacts_list], key=ContactForm.id_or_max)
    # Compare the lists
    for i in range(len(ui_contacts_list)):
        assert ui_contacts_list[i].contact_name == db_contacts_list[i].contact_name
        assert ui_contacts_list[i].contact_lastname == db_contacts_list[i].contact_lastname
        assert ui_contacts_list[i].contact_address == db_contacts_list[i].contact_address
        merged_phones = get_merged_contact_phones(db_contacts_list[i])
        merged_emails = get_merged_contact_emails(db_contacts_list[i])
        assert ui_contacts_list[i].all_phones_from_home_page == merged_phones
        assert ui_contacts_list[i].all_emails_from_home_page == merged_emails


def get_merged_contact_phones(row):
    merged_db_phones = "\n".join(filter(lambda x: x != "",
                                        map(lambda x: clear(x),
                                            filter(lambda x: x is not None, [row.contact_homephone,
                                                                             row.contact_mobile,
                                                                             row.contact_workphone,
                                                                             row.contact_secondary_phone]))))
    return merged_db_phones


def get_merged_contact_emails(row):
    # 1. Initial list [a,b,c]. 2. Filter - remove all None. 3. Filter - remove empty strings. 5. Join the rest with \n
    merged_db_emails = "\n".join(filter(lambda x: x != "",
                                        filter(lambda x: x is not None, [row.contact_email,
                                                                         row.contact_email2,
                                                                         row.contact_email3])))
    return merged_db_emails


def clear(s):
    return re.sub("[() -]", "", s)


def clear_object(s):
    contact_name_cleared = re.sub("[() -]", "", s.contact_name)
    contact_lastname_cleared = re.sub("[() -]", "", s.contact_lastname)
    contact_address_cleared = re.sub("[() -]", "", s.contact_address)
    s.contact_name = contact_name_cleared
    s.contact_lastname = contact_lastname_cleared
    s.contact_address = contact_address_cleared
    return s

