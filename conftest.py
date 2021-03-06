# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.db import DbFixture


fixture = None
cfg_target = None


# Load configuration file
def load_config(file):
    global cfg_target
    if cfg_target is None:
        # Get the path, where the file is located - dirname. Join the directory path with the file path
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file_to_use:
            cfg_target = json.load(file_to_use)
    return cfg_target


# Load web configuration from the configuration file
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--cfg_target"))["web"]
    # Create fixture 1. if it is not initialised or 2. if it is initialised but invalid, e.g. browser failed
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"],
                              username=web_config["username"], password=web_config["password"])
    # Login, if not currently logged in
    fixture.session.ensure_login()
    return fixture


# Load DB configuration from the configuration file
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--cfg_target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"],
                          user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


# Destroy/stop the fixture
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # Logout, if not currently logged out
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# Define if check_ui option is requested
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# Parse test run options
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--cfg_target", action="store", default="cfg_target.json")
    parser.addoption("--check_ui", action="store_true")


# Load test data from JSON file
def pytest_generate_tests(metafunc):
    # To load test data - form fixture, use parameters with prefix "data_", but remove the prefix (first 5 symbols)
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[10:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{}.json".format(file))) as file_in_use:
        return jsonpickle.decode(file_in_use.read())
