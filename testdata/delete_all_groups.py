from random import randrange


def test_del_all_groups(app):
    # Check if any group exist, and if not - create one
    while app.group.count() != 0:
        groups_list = app.group.get_groups_list()
        index = randrange(len(groups_list))
        app.group.del_by_index(index)
