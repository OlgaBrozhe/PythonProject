from sys import maxsize


class GroupForm:

    # Group representation

    def __init__(self, group_name=None, group_header=None, group_footer=None, group_id=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer
        self.group_id = group_id

    # Methods for groups lists representation and comparison

    def __repr__(self):
        return "{}:{}:{}:{}".format(self.group_id, self.group_name, self.group_header, self.group_footer)

    def __eq__(self, other):
        # Compare logically, not to use physical address of variables, thus just writing all lists variables
        # should be equal. Also when describing adding of an item, it doesn`t come with id, so it is taken
        # from "init" and is None, whereas in the new list it already has the id.
        check_is_none = self.group_id is None or other.group_id is None
        return (self.group_id == other.group_id or check_is_none) and self.group_name == other.group_name

    def id_or_max(self):
        # To be able to sort lists by id if there is no id, such as "" or None
        if self.group_id:
            return int(self.group_id)
        else:
            return maxsize
