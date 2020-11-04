from model.contact_form import ContactForm
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # Picking symbols for random choice: ascii_letters, digits, punctuation and a number spaces
    # Additional options: symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    # Random choice of symbols, generated for cycle of random length, not higher than max length
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


def random_phone(prefix, maxlen):
    # Additional options: symbols = string.digits*10 + string.punctuation + " "*10
    symbols = string.digits * 10 + " " * 10
    list_random_symbols = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    random_string_from_symbols_list = prefix + "".join(list_random_symbols)
    return random_string_from_symbols_list


testdata = [ContactForm(contact_name=random_string("CN__", 10), contact_lastname=random_string("CLN__",15),
                        contact_email=random_string("CE__@", 20), contact_email2=random_string("CE2__@", 20),
                        contact_homephone=random_phone("+", 15), contact_mobile=random_phone("+", 15),
                        contact_workphone=random_phone("+", 15), contact_secondary_phone=random_phone("+", 15))
            for i in range(n)]
# Access the file with data.
# <..> from "../data/<>.json" means that we move up from generator file to root in 2 steps.
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# What to do with the opened file:
with open(data_file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))
