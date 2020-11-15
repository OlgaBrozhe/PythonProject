import time
from model.contact_form import ContactForm
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_form):
        wd = self.app.wd
        # Create a new contact and return to home page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_form)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact_form):
        wd = self.app.wd
        # Fill in contact info
        self.change_field_value("firstname", contact_form.contact_name)
        self.change_field_value("lastname", contact_form.contact_lastname)
        self.change_field_value("address", contact_form.contact_address)
        self.change_field_value("email", contact_form.contact_email)
        self.change_field_value("company", contact_form.contact_company)
        self.change_field_value("home", contact_form.contact_homephone)
        self.change_field_value("mobile", contact_form.contact_mobile)
        self.change_field_value("work", contact_form.contact_workphone)
        self.change_field_value("phone2", contact_form.contact_secondary_phone)
        self.change_field_value("fax", contact_form.contact_fax)

    def change_field_value(self, field_title, field_value):
        wd = self.app.wd
        # Check if the field is going to be changed
        if field_value is not None:
            # Change the field value
            wd.find_element_by_name(field_title).click()
            wd.find_element_by_name(field_title).clear()
            wd.find_element_by_name(field_title).send_keys(field_value)

    def del_by_index(self, index):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Delete contact
        self.select_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(10)

    def del_by_id(self, contact_id):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Delete contact
        self.select_by_id(contact_id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(10)

    def del_first(self):
        self.del_by_index(0)

    def del_all(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        time.sleep(10)

    def navigate_to_home_page(self):
        wd = self.app.wd
        # Check if the page is the home page
        if not wd.current_url.endswith("addressbook/"):
            # Navigate to home page using menu
            wd.find_element_by_link_text("home").click()

    def select_by_index(self, index):
        wd = self.app.wd
        # Select contact from the contacts table
        wd.find_elements_by_xpath("//input[@name='selected[]']")[index].click()

    def select_by_id(self, contact_id):
        wd = self.app.wd
        # Find element, where value=contact_id and select it
        wd.find_element_by_css_selector("input[value='{}']".format(contact_id)).click()

    def select_first(self):
        self.select_by_index(0)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.navigate_to_home_page()
        self.select_by_id(contact_id)
        # Select_group
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='{}'])[2]".format(group_id)).click()
        # Click "add to"
        wd.find_element_by_name("add").click()

    def remove_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.navigate_to_home_page()
        self.show_contacts_in_group(group_id)
        self.select_by_id(contact_id)
        wd.find_element_by_name("remove").click()

    def show_contacts_in_group(self, group_id):
        wd = self.app.wd
        # Filter the contacts presented in the contacts table page (home page) by the group
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='{}']".format(group_id)).click()

    def mod_by_index(self, index, mod_contact_data):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Modify contact and return to home page
        self.select_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(mod_contact_data)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def mod_by_id(self, contact_id, mod_contact_data):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Modify contact and return to home page
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_element_by_xpath("//a[@href='edit.php?id={}']".format(str(contact_id))).click()
        self.fill_contact_form(mod_contact_data)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def mod_first(self):
        self.mod_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        # Check if the page is the home page
        if not wd.current_url.endswith("addressbook/"):
            # Return to home page after creation or modification of a contact
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.navigate_to_home_page()
        # Check if there are any elements to be selected on the current page and how many
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            # Get list of contacts on home page
            self.navigate_to_home_page()
            self.contact_cache = []
            # Find rows in table
            for row in wd.find_elements_by_name("entry"):
                # Find cell in row
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(ContactForm(contact_id=id, contact_name=firstname, contact_lastname=lastname,
                                                      contact_address=address, all_emails_from_home_page=all_emails,
                                                      all_phones_from_home_page=all_phones))
        contacts_list = list(self.contact_cache)
        return contacts_list

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # Navigate to the Edit icon in the table
        self.navigate_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        # Navigate to the View icon in the table
        self.navigate_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return ContactForm(contact_name=firstname, contact_lastname=lastname, contact_address=address,
                           contact_email=email, contact_email2=email2, contact_email3=email3,
                           contact_homephone=homephone, contact_mobile=mobile, contact_workphone=workphone,
                           contact_secondary_phone=secondary_phone, contact_id=id)

    def get_contact_phones_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return ContactForm(contact_homephone=homephone, contact_mobile=mobile, contact_workphone=workphone,
                           contact_secondary_phone=secondary_phone)