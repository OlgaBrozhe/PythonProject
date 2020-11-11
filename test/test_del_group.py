from model.group_form import GroupForm
import random


def test_del_group(app, db, check_ui):
    # Check if any group exist, and if not - create one
    if db.get_db_groups_list() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Delete random group
    old_groups_list = db.get_db_groups_list()
    group = random.choice(old_groups_list)
    app.group.del_by_id(group.group_id)
    new_groups_list = db.get_db_groups_list()
    # First check - if group was deleted at all
    assert len(old_groups_list) - 1 == len(new_groups_list)
    # Second check - if remained groups are equal
    old_groups_list.remove(group)
    assert old_groups_list == new_groups_list
    # Check match of UI and DB lists
    if check_ui:
        assert sorted(new_groups_list, key=GroupForm.id_or_max) == \
               sorted(app.group.get_groups_list(), key=GroupForm.id_or_max)
