# -*- coding: utf-8 -*-
from contact_form import ContactForm
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(ContactForm("TestUserName1", "TestUserLastName1", "TestUserEmail1", "TestUserCompany", "TestUserTelephoneMobile1"))
    app.logout()
