class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # Open URL, insert credentials and submit login
        self.app.open_home_page(url_addressbook="http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

  #  def is_logged_in(self):
   #     wd = self.app.wd
        # Check if logged in


    def ensure_login(self, username, password):
        wd = self.app.wd
        # Check if logged in
        if self.is_logged_in():
            # Check if logged in with correct username, if not - logout.
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self):
        wd = self.app.wd
        # Check which credentials are used for login

    def logout(self):
        wd = self.app.wd
        # Just logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd
        # If logged in, do logout
        if self.is_logged_in():
            self.logout()