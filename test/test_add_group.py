from model.group_form import GroupForm


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(GroupForm("", "", ""))
    app.session.logout()