import pytest

# THIS MUST BE IN conftest.py OR IT WILL NOT WORK
def pytest_addoption(parser):
    parser.addoption('--race', default='orc')

@pytest.fixture
def mogka():
    return 'Mogka'

@pytest.fixture(scope='session')
def race(request):
    return request.config.getoption('--race')