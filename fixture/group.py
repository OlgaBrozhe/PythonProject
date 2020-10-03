class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group_form):
        wd = self.app.wd
        #Create a new group and return to groups page
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_form)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group_form):
        wd = self.app.wd
        #Fill in group info: name, header, footer
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_form.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_form.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_form.group_footer)

    def del_first(self):
        wd = self.app.wd
        #Delete first group and return to groups page
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def mod_first(self, group_form):
        wd = self.app.wd
        #Modify first group and return to groups page
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group_form)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        #Select first group from the group list
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        #Return to groups page after creation, deletion or modification of a group
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        #Open groups page from menu
        wd.find_element_by_link_text("groups").click()