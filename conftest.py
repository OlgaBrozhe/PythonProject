# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    #If fixture is valid:
    if fixture is None:
        fixture = Application()
        fixture.session.login("admin", "secret")
    #If fixture is invalid, e.g. browser failed
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login("admin", "secret")
    return fixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture