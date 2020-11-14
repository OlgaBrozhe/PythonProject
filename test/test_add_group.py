from model.group_form import GroupForm
import re


# Name of the parameter where to put the test data, where to take it from and its text representation
# import pytest
# from data.data_groups import testdata
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_add_group(app, db, json_data_groups, check_ui):
    group = json_data_groups
    old_groups_list = db.get_db_groups_list()
    app.group.create(group)
    new_groups_list = db.get_db_groups_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    # Check match of UI and DB lists
    if check_ui:
        sorted_db_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
        sorted_ui_new_groups_list = sorted([clear(x) for x in app.group.get_groups_list()], key=GroupForm.id_or_max)
        assert sorted_db_new_groups_list == sorted_ui_new_groups_list


def clear(s):
    group_name_cleared = re.sub("[() -]", "", s.group_name)
    s.group_name = group_name_cleared
    return s

