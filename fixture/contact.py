import time
from model.contact_form import ContactForm


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_form):
        wd = self.app.wd
        #Create a new contact and return to home page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_form)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact_form):
        wd = self.app.wd
        #Fill in contact info
        self.change_field_value("firstname", contact_form.contact_name)
        self.change_field_value("lastname", contact_form.contact_lastname)
        self.change_field_value("email", contact_form.contact_email)
        self.change_field_value("company", contact_form.contact_company)
        self.change_field_value("mobile", contact_form.contact_mobile)

    def change_field_value(self, field_title, field_value):
        wd = self.app.wd
        # Check if the field is going to be changed
        if field_value is not None:
            # Change the field value
            wd.find_element_by_name(field_title).click()
            wd.find_element_by_name(field_title).clear()
            wd.find_element_by_name(field_title).send_keys(field_value)

    def del_first(self):
        wd = self.app.wd
        self.navigate_to_home_page()
        #Delete first contact
        self.select_first_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(10)

    def navigate_to_home_page(self):
        wd = self.app.wd
        # Check if the page is the home page
        if not wd.current_url.endswith("addressbook/"):
            #Navigate to home page using menu
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        #Select first contact from the contacts table
        wd.find_element_by_xpath("(//input[@name='selected[]'])").click()

    def mod_first(self, mod_contact_data):
        wd = self.app.wd
        self.navigate_to_home_page()
        #Modify first contact and return to home page
        self.select_first_contact()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_contact_form(mod_contact_data)
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        # Check if the page is the home page
        if not wd.current_url.endswith("addressbook/"):
            #Return to home page after creation or modification of a contact
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Check if there are any elements to be selected on the current page and how many
        return len(wd.find_elements_by_xpath("(//input[@name='selected[]'])"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            # Get list of contacts on home page with contacts (name and element id)
            self.navigate_to_home_page()
            self.contact_cache = []
            # Find rows in table
            for row in wd.find_elements_by_xpath(".//tr[@name='entry']"):
                # Find cell in row
                id = row.find_element_by_name("selected[]").get_attribute("value")
                firstname = row.find_element_by_xpath(".//td[3]").text
                lastname = row.find_element_by_xpath(".//td[2]").text
                self.contact_cache.append(ContactForm(contact_name=firstname, contact_lastname=lastname, contact_id=id))
        return list(self.contact_cache)