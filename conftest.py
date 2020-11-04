# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json
import jsonpickle
import os.path
import importlib


fixture = None
cfg_target = None


@pytest.fixture
def app(request):
    global fixture
    global cfg_target
    browser = request.config.getoption("--browser")
    if cfg_target is None:
        # Get the path, where is the file located - dirname. Join the directory path with the file path
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--cfg_target"))
        with open(config_file) as file_to_use:
            cfg_target = json.load(file_to_use)
    # Create fixture 1. if it is not initialised or 2. if it is initialised but invalid, e.g. browser failed
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=cfg_target["baseUrl"],
                              username=cfg_target["username"], password=cfg_target["password"])
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


