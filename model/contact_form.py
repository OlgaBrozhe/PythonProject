from sys import maxsize


class ContactForm:

    def __init__(self, contact_id=None, contact_name=None, contact_midname=None, contact_lastname=None,
                 contact_nick=None, contact_company=None, contact_title=None, contact_address=None,
                 contact_homephone=None, contact_mobile=None, contact_workphone=None, contact_fax=None,
                 contact_email=None, contact_email2=None, contact_email3=None, contact_homepage=None,
                 contact_birthday=None, contact_anniversary=None, contact_secondary_address=None,
                 contact_secondary_phone=None, contact_secondary_notes=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_midname = contact_midname
        self.contact_lastname = contact_lastname
        self.contact_nick = contact_nick
        self.contact_company = contact_company
        self.contact_title = contact_title
        self.contact_address = contact_address
        self.contact_homephone = contact_homephone
        self.contact_mobile = contact_mobile
        self.contact_workphone = contact_workphone
        self.contact_fax = contact_fax
        self.contact_email = contact_email
        self.contact_email2 = contact_email2
        self.contact_email3 = contact_email3
        self.contact_homepage = contact_homepage
        self.contact_birthday = contact_birthday
        self.contact_anniversary = contact_anniversary
        self.contact_secondary_address = contact_secondary_address
        self.contact_secondary_phone = contact_secondary_phone
        self.contact_secondary_notes = contact_secondary_notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    # Methods for contacts lists representation and comparison

    def __repr__(self):
        return "{}:{}:{}".format(self.contact_id, self.contact_name, self.contact_lastname)

    def __eq__(self, other):
        # Compare logically, not to use physical address of variables, thus just writing all lists variables
        # should be equal. Also when describing adding of an item, it doesn`t come with id, so it is taken
        # from "init" and is None, whereas in the new list it already has the id.
        check_is_none = self.contact_id is None or other.contact_id is None
        return (check_is_none or self.contact_id == other.contact_id) and (self.contact_name == other.contact_name) \
               and (self.contact_lastname == other.contact_lastname)

    def id_or_max(self):
        # To be able to sort lists by id if there is no id, such as "" or None
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
