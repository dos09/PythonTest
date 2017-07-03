# Functions
###########
def inc01 (x): 
    return x + 1

print("inc01(4): " + str(inc01(4)))
inc02 = lambda x : x + 1
print("inc02(20): " + str(inc02(20)))
print('------------------------------------------')
def pass_parameters(_list, _str="default value"):
    _list.append("new item")
    _str = "some val"

mystr = "mystr"
mylist = ["a"]
print("mylist: " + str(mylist))
print("mystr: " + mystr)
pass_parameters(mylist, mystr)
print("after pass_parameters(mylist, mystr)")
print("mylist: " + str(mylist))
print("mystr: " + mystr)
print('------------------------------------------')
print('pass unknown count of arguments to function')
def many_args(*args):
    print(type(args))
    print(args)
    for item in args:
        print(item)
        
def many_key_val_args(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key in kwargs:
        print(kwargs[key])
    for k, v in kwargs.items():
        print(k,'-',v)
    
many_args(1,3,'asda')
many_key_val_args(one='edno', two=2)
print('------------------------------------------')
print('pass function as argument')
def apply_math_operation(op, a, b):
    print(op(a,b))
    
def sum(a, b):
    return a + b

apply_math_operation(sum, 1, 4)