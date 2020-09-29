# -*- coding: utf-8 -*-
from group_form import GroupForm
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(GroupForm(group_name="TestNewGroup", group_header="TestNewGroup", group_footer="TestNewGroup"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(GroupForm(group_name="", group_header="", group_footer=""))
    app.logout()