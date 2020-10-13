from sys import maxsize


class ContactForm:

    def __init__(self, contact_name=None, contact_lastname=None, contact_email=None, contact_company=None, contact_mobile=None, contact_id=None):
        self.contact_name = contact_name
        self.contact_lastname = contact_lastname
        self.contact_email = contact_email
        self.contact_company = contact_company
        self.contact_mobile = contact_mobile
        self.contact_id = contact_id

    # Methods for contacts lists representation and comparison

    def __repr__(self):
        return "{}:{}:{}".format(self.contact_id, self.contact_name, self.contact_lastname)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and self.contact_name == other.contact_name
               # self.contact_lastname == other.contact_lastname

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
