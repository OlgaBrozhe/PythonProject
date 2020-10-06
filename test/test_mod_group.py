from model.group_form import GroupForm


#def test_mod_first_group(app):
 #   app.session.login("admin", "secret")
  #  app.group.mod_first(GroupForm("TestModGroup", "TestModGroup", "TestModGroup"))
   # app.session.logout()

def test_mod_first_group_name(app):
    # Check if any group exist, and if not - create one, insert name
    if app.group.count() == 0:
        app.group.create(GroupForm(group_name="AutocreatedGroup"))
    # Modify first group name
    app.group.mod_first(GroupForm(group_name="TestModGroupName"))

def test_mod_first_group_header(app):
    # Check if any group exist, and if not - create one, insert header
    if app.group.count() == 0:
        app.group.create(GroupForm(group_header="AutocreatedGroup"))
    # Modify first group header
    app.group.mod_first(GroupForm(group_header="TestModGroupHeader"))

def test_mod_first_group_footer(app):
    # Check if any group exist, and if not - create one, insert footer
    if app.group.count() == 0:
        app.group.create(GroupForm(group_footer="AutocreatedGroup"))
    # Modify first group footer
    app.group.mod_first(GroupForm(group_footer="TestModGroupFooter"))