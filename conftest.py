# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    # Initialise fixture, if it is valid:
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, username=username, password=password)
    # Initialise fixture, if it is invalid, e.g. browser failed
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, username=username, password=password)
    # Login, if not currently logged in
    fixture.session.ensure_login()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # Logout, if not currently logged out
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")
