# Classes
#########

class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable
    
classinstance = MyClass()
print("classinstance.myfunction(5, 9): " + str(classinstance.myfunction(5, 9)))
classinstance2 = MyClass()
print("classinstance.common: " + str(classinstance.common))
print("classinstance2.common: " + str(classinstance2.common))
MyClass.common = 30
print("classinstance.common: " + str(classinstance.common))
print("classinstance2.common: " + str(classinstance2.common))
# This will not update the variable on the class,
# instead it will bind a new object to the old
# variable name.
classinstance.common = 13
print("classinstance.common: " + str(classinstance.common))
print("classinstance2.common: " + str(classinstance2.common))
MyClass.common = 50
print("classinstance.common: " + str(classinstance.common)) # not changed because 'common' is now an instance variable
print("classinstance2.common: " + str(classinstance2.common))

# This class inherits from MyClass. The example
# class above inherits from "object", which makes
# it what's called a "new-style class".
# Multiple inheritance is declared as:
# class OtherClass(MyClass1, MyClass2, MyClassN)
class OtherClass(MyClass):
    # The "self" argument is passed automatically
    # and refers to the class instance, so you can set
    # instance variables as above, but from inside the class.
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)

classinstance = OtherClass("hello")
print("classinstance.myfunction(5, 9): " + str(classinstance.myfunction(5, 9)))
# This class doesn't have a .test member, but
# we can add one to the instance anyway. Note
# that this will only be a member of classinstance.
classinstance.test = 300
print("classinstance.test: " + str(classinstance.test))
# print("classinstance2.test: " + str(classinstance2.test)) # will give error


class Orc:
    def __call__(self):
        print('the orc instance was called')
        
orc = Orc()
orc()
