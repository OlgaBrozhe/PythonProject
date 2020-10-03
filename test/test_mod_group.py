from model.group_form import GroupForm


#def test_mod_first_group(app):
 #   app.session.login("admin", "secret")
  #  app.group.mod_first(GroupForm("TestModGroup", "TestModGroup", "TestModGroup"))
   # app.session.logout()

def test_mod_first_group_name(app):
    app.group.mod_first(GroupForm(group_name="TestModGroupName"))

def test_mod_first_group_header(app):
    app.group.mod_first(GroupForm(group_header="TestModGroupHeader"))

def test_mod_first_group_footer(app):
    app.group.mod_first(GroupForm(group_footer="TestModGroupFooter"))