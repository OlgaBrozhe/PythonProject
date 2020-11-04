from model.group_form import GroupForm
import random
import string


# constant = [
#         GroupForm(group_name="GN_"+str(1), group_header="GH_"+str(1), group_footer="GF_"+str(1)),
#         GroupForm(group_name="GN_"+str(2), group_header="GH_"+str(2), group_footer="GF_"+str(2)),
#         GroupForm(group_name="GN_"+str(3), group_header="GH_"+str(3), group_footer="GF_"+str(3))
#     ]


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


# # Random options of test data
# # Create 2 groups, 1 random and 1 empty
# testdata = [
#     GroupForm(group_name=random_string("group_name_", 10),
#               group_header=random_string("group_header_", 15),
#               group_footer=random_string("group_footer_", 20)),
#     GroupForm("", "", "")]
# # Create 1 empty group and several random
# testdata = \
#     [GroupForm("", "", "")] + \
#     [GroupForm(group_name=random_string("group_name_", 10), group_header=random_string("group_header_", 15),
#                group_footer=random_string("group_footer_", 20)) for i in range(5)]
# # Create groups randomly, including empty
# testdata = [
#     GroupForm(group_name=group_name, group_header=group_header, group_footer=group_footer)
#     for group_name in ["", random_string("group_name", 10)]
#     for group_header in ["", random_string("group_header", 15)]
#     for group_footer in ["", random_string("group_footer", 20)]
#     ]
# Create random groups
testdata = [GroupForm(group_name=random_string("GN__", 5), group_header=random_string("GH__", 10),
                      group_footer=random_string("GF__", 15)) for i in range(5)]
