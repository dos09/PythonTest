import random
import sys
import logging

import pytest

LOG = logging.getLogger(__name__)


def init_logging(log_level=logging.DEBUG):
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)8s] - %(message)s", "%Y-%m-%d %H:%M:%S"))
    ch.setLevel(log_level)
    logging.basicConfig(handlers=[ch], level=log_level)

SKIP_ALPHA_TESTS = True
skip_xx = pytest.mark.skipif(1 == 1, reason='1 == 1 for xx')

#####################################################################
# functions to test


def inc(x):
    return x + 1


def raise_exception():
    raise ValueError('Tralala')


#####################################################################
# test functions

def test_inc():
    assert inc(4) == 5


def test_raise():
    with pytest.raises(ValueError):
        raise_exception()


class TestOrc():

    def test_mogka(self):
        assert True

    @pytest.mark.skip(reason='Testing @pytest.mark.skip')
    def test_ra(self):
        assert 1 == 3 - 2


def test_skip_inside_alpha():
    if SKIP_ALPHA_TESTS:
        pytest.skip('skipped due to condition')

#@pytest.mark.skipif("SKIP_ALPHA_TESTS") # no reason needed


@pytest.mark.skipif(SKIP_ALPHA_TESTS, reason='Testing @pytest.mark.skipif')
def test_skip_decorator_alpha():
    assert 3 == 3


@skip_xx
def test_xx_a():
    pass


@skip_xx
def test_xx_b():
    pass


@pytest.mark.xfail
def test_xfail():
    raise Exception()

#####################################################################
# using fixtures

# the default behavior is to invoke the fixture
# once per test function


@pytest.fixture
def rand_num():
    print('rand_num fixture invoked * * * * * * * * *')
    return random.randint(1, 10)

# invoked once per module
@pytest.fixture(scope='module')
def num_3():
    print('num_3 fixture invoked | | | | | | | | | | |')
    return 3

@pytest.fixture
def big_stone(scope='session'):
    print('resource that needs some cleanup (big stone)')
    yield 'big stone'
    print('big stone is out of scope, cleaning up')

def test_rand_int(rand_num, num_3, big_stone):
    print('test_rand_int received: %s, %s, %s' %
           (rand_num, num_3, big_stone))


def test_rand_int2(rand_num, num_3):
    print('test_rand_int2 received: %s, %s' % (rand_num, num_3))


def test_mogka_fixture(mogka):
    print('This is %s' % (mogka,))
    assert mogka == 'Mogka'
    
def test_cli_option(race):
    print('race: %s' % (race,))
    
    
#####################################################################
# using custom marks

@pytest.mark.fruits
def test_banana():
    print('banana banana banana banana banana banana banana banana')

@pytest.mark.fruits
def test_mango():
    print('mango mango mango mango mango mango mango mango mango')

@pytest.mark.vegetables
def test_carrot():
    print('carrot carrot carrot carrot carrot carrot carrot carrot') 

@pytest.mark.system
def test_system():
    print('SYSTEM')

"""

### How to run:

To run one file: pytest /path/to/file.py
To run all files: pytest /path/to/dir
Commonly used options:
-s (show print, logging)
-v (increase verbosity)
-q (quiet, decrease verbosity)
-r chars    show extra test summary info as specified by chars
            (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
            (p)passed, (P)passed with output, (a)all except pP.
            Warnings are displayed at all times except when
            --disable-warnings is set
-x stop on first failure
            
pytest practice.py -rs
will show the reasons, why the tests are skipped (summary)
pytest practice.py -ra
will show failed, skipped... (summary)

### fixture

conftest.py: sharing fixture functions
If during implementing your tests you realize that you want to use a 
fixture function from multiple test files you can move it to a conftest.py 
file. You don't need to import the fixture you want to use in a test, 
it automatically gets discovered by pytest. The discovery of fixture 
functions starts at test classes, then test modules, then conftest.py 
files and finally builtin and third party plugins.

The fixtures are by default invoked once per test function, to change that
the scope param can be used.
Possible values for scope are: function, class, module, package or session.

### custom markers

pytest practice_pytest.py -vs -m "fruits or vegetables"
will run test methods that are marked with fruits or vegetables
(can use boolean expressions: and, or, not)
pytest practice_pytest.py -vs -m "not (fruits or vegetables)"

"""
