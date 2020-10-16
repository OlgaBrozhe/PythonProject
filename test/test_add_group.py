from model.group_form import GroupForm


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    group = GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup")
    app.group.create(group)
    # First check if group was created
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    # Append old list with new item, sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)


# def test_add_empty_group(app):
#     old_groups_list = app.group.get_groups_list()
#     group = GroupForm("", "", "")
#     app.group.create(group)
#     new_groups_list = app.group.get_groups_list()
#     # First check if group was created
#     assert len(old_groups_list) + 1 == len(new_groups_list)
#     # Append old list with new item, sort lists ascending and check if they are still equal
#     old_groups_list.append(group)
#     assert sorted(old_groups_list, key=GroupForm.id_or_max) == sorted(new_groups_list, key=GroupForm.id_or_max)