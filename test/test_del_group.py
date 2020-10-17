from model.group_form import GroupForm
from random import randrange


def test_del_group(app):
    # Check if any group exist, and if not - create one
    if app.group.count() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Delete group
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    app.group.del_by_index(index)
    new_groups_list = app.group.get_groups_list()
    # First check - if group was deleted at all
    assert len(old_groups_list) - 1 == len(new_groups_list)
    # Second check - if remained groups are equal
    old_groups_list[index:index+1] = []
    assert old_groups_list == new_groups_list
