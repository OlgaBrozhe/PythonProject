from model.group_form import GroupForm


def test_mod_first_group(app):
    app.session.login("admin", "secret")
    app.group.mod_first(GroupForm("TestModGroup", "TestModGroup", "TestModGroup"))
    app.session.logout()