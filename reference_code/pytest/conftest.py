import pytest

def pytest_addoption(parser):
    parser.addoption("--str_one", default='default value 1')
    parser.addoption("--str_two", default='default value 2')


@pytest.fixture(scope='session')
def str_one(request):
    return request.config.getoption("--str_one")


@pytest.fixture(scope='session')
def str_two(request):
    return request.config.getoption("--str_two")


@pytest.fixture
def str_united(str_one, str_two):
    return str_one + " - " +str_two

# in to_test.py when finds one of these as parameter:
# str_one, str_two or str_united
# pytest will take them, executing one/or more of the above methods