from model.group_form import GroupForm
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list

# Options of testdata
# testdata = [
#     GroupForm(group_name=random_string("group_name_", 10), group_header=random_string("group_header_", 15),
#               group_footer=random_string("group_footer_", 20)),
#     GroupForm("", "", "")]
# testdata = \
#     [GroupForm("", "", "")] + \
#     [GroupForm(group_name=random_string("group_name_", 10), group_header=random_string("group_header_", 15),
#                group_footer=random_string("group_footer_", 20)) for i in range(5)]
# testdata = [
#     GroupForm(group_name=group_name, group_header=group_header, group_footer=group_footer)
#     for group_name in ["", random_string("group_name", 10)]
#     for group_header in ["", random_string("group_header", 15)]
#     for group_footer in ["", random_string("group_footer", 20)]
#     ]
testdata = [GroupForm(group_name=random_string("GN__", 5), group_header=random_string("GH__", 10),
                      group_footer=random_string("GF__", 15)) for i in range(5)]

# Name of the parameter where to put the test data, where to take it from and its text representation
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups_list = app.group.get_groups_list()
    app.group.create(group)
    # First check if group was created
    var1 = len(old_groups_list) + 1
    var2 = app.group.count()
    assert var1 == var2
    new_groups_list = app.group.get_groups_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    var3 = sorted([clear(x) for x in old_groups_list], key=GroupForm.id_or_max)
    var4 = sorted([clear(x) for x in new_groups_list], key=GroupForm.id_or_max)
    assert var3 == var4


def clear(s):
    group_name_cleared = re.sub("[() -]", "", s.group_name)
    s.group_name = group_name_cleared
    return s

