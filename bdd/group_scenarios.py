from pytest_bdd import scenario
# This import is required for the tests to run, importing steps. Will fail if removed.
from .group_steps import *


# Scenarios actually implemented in groups_steps and groups.feature, that is why 'pass'
@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass