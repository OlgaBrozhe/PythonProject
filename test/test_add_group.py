from model.group_form import GroupForm


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    app.group.create(GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup"))
    new_groups_list = app.group.get_groups_list()
    # Check if group was created
    assert len(old_groups_list) + 1 == len(new_groups_list)


def test_add_empty_group(app):
    old_groups_list = app.group.get_groups_list()
    app.group.create(GroupForm("", "", ""))
    new_groups_list = app.group.get_groups_list()
    # Check if group was created
    assert len(old_groups_list) + 1 == len(new_groups_list)