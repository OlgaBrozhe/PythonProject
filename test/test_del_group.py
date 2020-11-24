from model.group_form import GroupForm
import random
import re
import pytest
import allure


def test_del_group(app, db, check_ui):
    # Check if any group exist, and if not - create one
    with allure.step('Given a non-empty group list'):
        old_groups_list = db.get_db_groups_list()
        if not old_groups_list:
            app.group.create(GroupForm(group_name="AutocreatedGroup"))
            old_groups_list = db.get_db_groups_list()
        group = random.choice(old_groups_list)
    with allure.step('When I delete the group %s from the list' % group):
        app.group.del_by_id(group.group_id)
    with allure.step('Then the new group list is equal to the old group list without the deleted group'):
        new_groups_list = db.get_db_groups_list()
        # First check - if group was deleted at all
        assert len(old_groups_list) - 1 == len(new_groups_list)
        # Second check - if remained groups are equal
        old_groups_list.remove(group)
        assert old_groups_list == new_groups_list
        # Check match of UI and DB lists
        if check_ui:
            sorted_db_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
            sorted_ui_new_groups_list = sorted([clear(x) for x in app.group.get_groups_list()], key=GroupForm.id_or_max)
            assert sorted_db_new_groups_list == sorted_ui_new_groups_list

def clear(s):
    group_name_cleared = re.sub("[() -]", "", s.group_name)
    s.group_name = group_name_cleared
    return s
