from model.group_form import GroupForm


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    group = GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup")
    app.group.create(group)
    new_groups_list = app.group.get_groups_list()
    # First check if group was created
    assert len(old_groups_list) + 1 == len(new_groups_list)
    # Second check, lists comparison
    old_groups_list.append(group)
    # Compare lists sorted by id ascending
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)


def test_add_empty_group(app):
    old_groups_list = app.group.get_groups_list()
    group = GroupForm("", "", "")
    app.group.create(group)
    new_groups_list = app.group.get_groups_list()
    # First check if group was created
    assert len(old_groups_list) + 1 == len(new_groups_list)
    # Second check, just training lists comparison
    old_groups_list.append(group)
    # Compare lists sorted by id ascending
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)