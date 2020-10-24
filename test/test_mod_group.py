from model.group_form import GroupForm
from random import randrange


def test_mod_group_name(app):
    # Check if any group exist, and if not - create one, insert name
    if app.group.count() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Modify random group name
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    group = GroupForm(group_name="TestModGroupName")
    # Ensure the id of the modified item will remain
    group.group_id = old_groups_list[index].group_id
    app.group.mod_by_index(index, group)
    new_groups_list = app.group.get_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    old_groups_list[index] = group
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)


def test_mod_group_header(app):
    # Check if any group exist, and if not - create one, insert header
    if app.group.count() == 0:
        app.group.create(GroupForm(group_header="AutocreatedGroup"))
    # Modify random group header
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    group = GroupForm(group_header="TestModGroupHeader")
    # Ensure the id and name of the modified item will remain
    group.group_id = old_groups_list[index].group_id
    group.group_name = old_groups_list[index].group_name
    app.group.mod_by_index(index, group)
    new_groups_list = app.group.get_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    old_groups_list[index] = group
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)


def test_mod_group_footer(app):
    # Check if any group exist, and if not - create one, insert footer
    if app.group.count() == 0:
        app.group.create(GroupForm(group_footer="AutocreatedGroup"))
    # Modify random group footer
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    group = GroupForm(group_footer="TestModGroupFooter")
    # Ensure the id and name of the modified item will remain
    group.group_id = old_groups_list[index].group_id
    group.group_name = old_groups_list[index].group_name
    app.group.mod_by_index(index, group)
    new_groups_list = app.group.get_groups_list()
    # First check if group was modified meaning len is the same
    assert len(old_groups_list) == len(new_groups_list)
    # Change the item in old list with new item, sort lists ascending and check if they are still equal
    old_groups_list[index] = group
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)