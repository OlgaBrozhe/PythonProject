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

    def fill_contact_form(self, contact_form):
        wd = self.app.wd
        #Fill in contact info: first name, last name, email, company, mobile
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_form.contact_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_form.contact_lastname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_form.contact_email)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_form.contact_company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_form.contact_mobile)

    def del_first(self):
        wd = self.app.wd
        #Delete first contact
        self.select_first_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        #Select first contact from the contacts table
        wd.find_element_by_xpath("(//input[@name='selected[]'])").click()

    def mod_first(self, contact_form):
        wd = self.app.wd
        #Modify first contact and return to home page
        self.select_first_contact()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_contact_form(contact_form)
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        #Return to home page after creation or modification of a contact
        wd.find_element_by_link_text("home page").click()