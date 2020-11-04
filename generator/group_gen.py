from model.group_form import GroupForm
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


# Create random groups
testdata = [GroupForm(group_name=random_string("GN__", 5), group_header=random_string("GH__", 10),
                      group_footer=random_string("GF__", 15)) for i in range(n)]
# Access the file with data.
# <..> from "../data/groups.json" means that we move up from generator file to root in 2 steps.
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# What to do with the opened file:
with open(data_file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))
