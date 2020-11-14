from model.group_form import GroupForm
import random
import re


def test_mod_group_name(app, db, check_ui):
    # Check if any group exist, and if not - create one, insert name
    if db.get_db_groups_list() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Modify random group name
    old_groups_list = db.get_db_groups_list()
    group_selected = random.choice(old_groups_list)
    group = GroupForm(group_name="TestModGroupName")
    # Ensure the id of the modified item will remain
    group.group_id = group_selected.group_id
    app.group.mod_by_id(group.group_id, group)
    new_groups_list = db.get_db_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # # Change the item in old list with new item, sort lists ascending and check if they are still equal
    # for item in old_groups_list:
    #     if item.group_id == group.group_id:
    #         item.group_name = group.group_name
    # sorted_old_groups_list = sorted(old_groups_list, key=GroupForm.id_or_max)
    # sorted_new_groups_list = sorted(new_groups_list, key=GroupForm.id_or_max)
    # assert sorted_old_groups_list == sorted_new_groups_list
    # Check match of UI and DB lists
    if check_ui:
        sorted_db_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
        sorted_ui_new_groups_list = sorted([clear(x) for x in app.group.get_groups_list()], key=GroupForm.id_or_max)
        assert sorted_db_new_groups_list == sorted_ui_new_groups_list


def clear(s):
    group_name_cleared = re.sub("[() -]", "", s.group_name)
    s.group_name = group_name_cleared
    return s


def test_mod_group_header(app, db, check_ui):
    # Check if any group exist, and if not - create one, insert header
    if db.get_db_groups_list() == 0:
        app.group.create(GroupForm(group_header="AutocreatedGroup"))
    # Modify random group header
    old_groups_list = db.get_db_groups_list()
    group_selected = random.choice(old_groups_list)
    group = GroupForm(group_header="TestModGroupHeader")
    # Ensure the id and name of the modified item will remain
    group.group_id = group_selected.group_id
    group.group_name = group_selected.group_name
    app.group.mod_by_id(group.group_id, group)
    new_groups_list = db.get_db_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # Check match of UI and DB lists
    if check_ui:
        sorted_db_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
        sorted_ui_new_groups_list = sorted([clear(x) for x in app.group.get_groups_list()], key=GroupForm.id_or_max)
        assert sorted_db_new_groups_list == sorted_ui_new_groups_list


def test_mod_group_footer(app, db, check_ui):
    # Check if any group exist, and if not - create one, insert footer
    if db.get_db_groups_list() == 0:
        app.group.create(GroupForm(group_footer="AutocreatedGroup"))
    # Modify random group footer
    old_groups_list = db.get_db_groups_list()
    group_selected = random.choice(old_groups_list)
    group = GroupForm(group_footer="TestModGroupFooter")
    # Ensure the id and name of the modified item will remain
    group.group_id = group_selected.group_id
    group.group_name = group_selected.group_name
    app.group.mod_by_id(group.group_id, group)
    new_groups_list = db.get_db_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # Check match of UI and DB lists
    if check_ui:
        sorted_db_new_groups_list = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
        sorted_ui_new_groups_list = sorted([clear(x) for x in app.group.get_groups_list()], key=GroupForm.id_or_max)
        assert sorted_db_new_groups_list == sorted_ui_new_groups_list