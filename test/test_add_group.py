from model.group_form import GroupForm
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits and a number spaces
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
testdata = [GroupForm(group_name="GN__ 1", group_header=random_string("GH__", 15),
                      group_footer=random_string("GF__", 20)) for i in range(2)]


# Name of the parameter where to put the testdata, where to take the testdata from, text representation of the testdata
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups_list = app.group.get_groups_list()
    app.group.create(group)
    # First check if group was created
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    # Append old list with new item, sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    list1a = map(lambda x: clear(x), old_groups_list)
    list1 = sorted(list1a, key=GroupForm.id_or_max)
    list2a = map(lambda x: clear(x), new_groups_list)
    list2 = sorted(list2a, key=GroupForm.id_or_max)
    assert list1 == list2
    print(list1 == list2)
    #
    # all_phones_joined = "\n".join(filter(lambda x: x != "",
    #                                      map(lambda x: clear(x),
    #                                          filter(lambda x: x is not None, [all_phones.contact_homephone,
    #                                                                           all_phones.contact_mobile,
    #                                                                           all_phones.contact_workphone,
    #                                                                           all_phones.contact_secondary_phone]))))

def clear(s):
    return re.sub("[() -]", "", s)