# -*- coding: utf-8 -*-
from model.group_form import GroupForm
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(GroupForm("TestNewGroup", "TestNewGroup", "TestNewGroup"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(GroupForm("", "", ""))
    app.session.logout()