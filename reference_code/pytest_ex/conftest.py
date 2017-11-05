import pytest

def pytest_addoption(parser):
    parser.addoption("--str_one", default='default value 1')
    parser.addoption("--str_two", default='default value 2')


@pytest.fixture(scope='session')
def str_one(request):
    s = request.config.getoption("--str_one")
    yield s
    # tear-down code (one way to do it)
    print('yielded instance from str_one is not used anymore')


@pytest.fixture(scope='session')
def str_two(request):
    # tear down code (second way to do it)
    # main differences from using yield:
    # 1. can add more than one method
    # 2. registered finalizer functions are called even if exception
    # occurs in the fixture function
    request.addfinalizer(finalizer01)
    return request.config.getoption("--str_two")

# the tear-down code is executed after the produced instance
# from the fixture is not used anymore


@pytest.fixture
def str_united(str_one, str_two):
    return str_one + " - " +str_two

def finalizer01():
    print('finalizer01 called')
    
# when using params, all functions that use "num" parameter will be
# invoked once with each item from params
@pytest.fixture(scope='session', params=[1,2,3,4])
def num(request):
    return request.param


# in to_test.py when finds one of these as parameter:
# str_one, str_two or str_united
# pytest will take them, executing one/or more of the above methods

# a fixture function is called before invocation of 
# function using the given fixture (the default scope is 
# function)