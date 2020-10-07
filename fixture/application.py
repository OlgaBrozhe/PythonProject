from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
    # Check if fixture is valid or invalid, e.g. browser failed
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self, url_addressbook):
        wd = self.wd
        wd.get(url_addressbook)

    def destroy(self):
        self.wd.quit()
