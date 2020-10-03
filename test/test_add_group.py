from model.group_form import GroupForm


def test_add_group(app):
    app.group.create(GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup"))


def test_add_empty_group(app):
    app.group.create(GroupForm("", "", ""))