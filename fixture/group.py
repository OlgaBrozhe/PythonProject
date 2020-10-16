from model.group_form import GroupForm


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group_form):
        wd = self.app.wd
        # Create a new group and return to groups page
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_form)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group_form):
        wd = self.app.wd
        # Fill in group info
        self.change_field_value("group_name", group_form.group_name)
        self.change_field_value("group_header", group_form.group_header)
        self.change_field_value("group_footer", group_form.group_footer)

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
        # Delete first group and return to groups page
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def mod_first(self, mod_group_data):
        wd = self.app.wd
        # Modify first group and return to groups page
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(mod_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # Select first group from the group list
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # Check if the page is the groups page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            # Return to groups page after creation, deletion or modification of a group
            wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        # Check if the page is the groups page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            # Open groups page from menu
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        # Check if there are any elements to be selected on the current page and how many
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        # Cache handling
        if self.group_cache is None:
            wd = self.app.wd
            # Get list of groups on groups page (name and element id)
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(GroupForm(group_name=text, group_id=id))
        #return groups_list
        return list(self.group_cache)
