# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json


fixture = None
cfg_target = None


@pytest.fixture
def app(request):
    global fixture
    global cfg_target
    browser = request.config.getoption("--browser")
    if cfg_target is None:
        with open(request.config.getoption("--cfg_target")) as config_file:
            cfg_target = json.load(config_file)
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    # Create fixture 1. if it is not initialised or 2. if it is initialised but invalid, e.g. browser failed
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=cfg_target["baseUrl"],
                              username=username, password=password)
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
    parser.addoption("--cfg_target", action="store", default="cfg_target.json")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")
