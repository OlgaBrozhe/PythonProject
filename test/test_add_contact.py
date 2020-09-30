# -*- coding: utf-8 -*-
from model.contact_form import ContactForm
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(ContactForm("TestUserName1", "TestUserLastName1", "TestUserEmail1", "TestUserCompany", "TestUserTelephoneMobile1"))
    app.session.logout()
