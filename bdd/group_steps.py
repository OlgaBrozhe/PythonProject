from pytest_bdd import given, when, then
from model.group_form import GroupForm
import random


# To add a group
@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_db_groups_list()


@given('a group with <name>, <header> and <footer>', target_fixture='new_group')
def new_group(name, header, footer):
    return GroupForm(group_name=name, group_header=header, group_footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_db_groups_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=GroupForm.id_or_max) == sorted(new_groups, key=GroupForm.id_or_max)


# To delete a group
@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_db_groups_list()) == 0:
        app.group.create(GroupForm(group_name="TestGroup"))
    result = db.get_db_groups_list()
    return result


@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    old_groups = non_empty_group_list
    return random.choice(old_groups)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.del_by_id(random_group.group_id)


@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_db_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups