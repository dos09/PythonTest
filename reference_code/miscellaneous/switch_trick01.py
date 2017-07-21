from collections import defaultdict

def func_a():
    print('A')

def func_b():
    print('B')

# the default value for the default dict must be callable
# when a missing key is accessed d['missing_key']
# the below method will be invoked and will return the finc_default object
# as value for the missing key
def get_default_func():
    def func_default():
        print('default')
    
    return func_default

switch = defaultdict(
    get_default_func,
    # populate at initialization time
    {
        'a': func_a,
        'b': func_b
    }
)

switch['a']()
switch['b']()
switch['c']()
switch['d']()