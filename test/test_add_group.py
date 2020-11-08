from model.group_form import GroupForm
import re


# Name of the parameter where to put the test data, where to take it from and its text representation
# import pytest
# from data.data_groups import testdata
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_add_group(app, db, json_data_groups):
    group = json_data_groups
    old_groups_list = db.get_db_groups_list()
    app.group.create(group)
    # First check if group was created - haching
    # assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = db.get_db_groups_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    sorted_old_groups_list = sorted([clear(x) for x in old_groups_list], key=GroupForm.id_or_max)
    sorted_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
    assert sorted_old_groups_list == sorted_new_groups_list


def clear(s):
    group_name_cleared = re.sub("[() -]", "", s.group_name)
    s.group_name = group_name_cleared
    return s
