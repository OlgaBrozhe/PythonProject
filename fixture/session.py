class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # Open URL, insert credentials and submit login
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        # Just logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    # Checks
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

    def is_logged_in_as(self, username):
        wd = self.app.wd
        # Check which credentials are used for login
        return self.get_logged_username() == username

    def get_logged_username(self):
        wd = self.app.wd
        # Get username from inside the brackets, like (admin)
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]

    def is_logged_in(self):
        wd = self.app.wd
        # Check if logged in - if there are elements with text Logout on the current page
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_logout(self):
        wd = self.app.wd
        # If logged in, do logout
        if self.is_logged_in():
            self.logout()