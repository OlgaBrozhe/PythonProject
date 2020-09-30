class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_form):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        #Fill in the contact info
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
        #Submit and return to Home page
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()