from model.group_form import GroupForm


def test_del_first_group(app):
    # Check if any group exist, and if not - create one
    if app.group.count() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Delete first group
    app.group.del_first()
