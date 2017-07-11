import pytest

# If this file is invoked like that: pytest to_test.py
# all methods starting with 'test' (case-insensitive) will be invoked.
# If the test methods are in a class, the class must not have __init__ method

# ways to run it:
# pytest to_test.py
# pytest to_test.py --str_one "A B C" --str_two "P L A"
# pytest to_test.py -s -v -k "test_B"
# options:
# -v : verbosity
# -s : show print statements
# -k "test_B" : invoke only methods starting with test_B 

def test_A(str_one, str_two):
    print("str one: %s" % str_one)
    print("str two: %s" % str_two)
    assert 1 == 1
    
def test_B1():
    assert 3 == 3
    
def test_B2(str_united):
    print("str united: %s" % str_united)
    assert 3 == 3    

# this test method will be skipped
@pytest.mark.skip    
def test_C():
    assert 3 == 3
    
    