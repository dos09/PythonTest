# Functions
###########
def inc01 (x): return x + 1

print("inc01(4): " + str(inc01(4)))
inc02 = lambda x : x + 1
print("inc02(20): " + str(inc02(20)))

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
