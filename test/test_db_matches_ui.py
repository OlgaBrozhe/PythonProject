from model.group_form import GroupForm
# Measure the response time
# from timeit import timeit


def test_groups_list(app, db):
    ui_groups_list = app.group.get_groups_list()
    #print(timeit(lambda: ui_groups_list, number=1))
    def clean(group):
        return GroupForm(group_id=group.group_id, group_name=group.group_name.strip())
    db_groups_list = map(clean, db.get_db_groups_list())
    #print(timeit(lambda: db_groups_list, number=1000))
    #assert False
    assert sorted(ui_groups_list, key=GroupForm.id_or_max) == sorted(db_groups_list, key=GroupForm.id_or_max)