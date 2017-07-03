
def test_unpacking_args():
    
    def unpacking_args(one, two, three='3'):
        print(one, two, three)
    
    a = [1, 2]
    # the '*' means the passed it list or tuple and must be unpacked
    unpacking_args(*a)
    a = [4, 5, 6]
    unpacking_args(*a)
    a = (1, 2)
    unpacking_args(*a)
    a = (1, 2, 3)
    unpacking_args(*a)
    

def test_unpacking_kwargs():
    
    def unpacking_kwargs(one='1', two='2', three='3'):
        print(one, two, three)

    unpacking_kwargs()
    a = dict(one='One', two='TWO')
    unpacking_kwargs(**a)
    a = {'one':'Edno', 'three':'Tri'}
    unpacking_kwargs(**a)
    unpacking_kwargs(two='Zwei')
    
def test_documented_func():
    def documented_func():
        """First line is short summary.
        
        This is the description and it comes after a blank line.
        Must be in a multiline string."""
        pass

    print(documented_func.__doc__)

def test_annotated_f():

    def annotated_f(name: str, race: str='orc',) -> str:
        print('Annotations:', annotated_f.__annotations__)
        print('Arguments:', name, race)
        print(name, 'is', race)
        
    annotated_f('Mogka')
    
num = 4
if num == 1:
    test_unpacking_args()
elif num == 2:
    test_unpacking_kwargs()
elif num == 3:
    test_documented_func()
elif num == 4:
    test_annotated_f()
