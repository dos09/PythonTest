#  imports should be each on new line
#  
#  import x
#  import y
#  from z import a, b, c #this is counted as one import
#  
#  Imports should be grouped in the following order:
# 
#     standard library imports
#     related third party imports
#     local application/library specific imports
# 
# You should put a blank line between each group of imports. 

class Orc:
    def __init__(self):
        pass
    
    def method_orc(self):
        pass
    

class Troll:
    def method_troll_A(self):
        pass
    
    def method_troll_B(self):
        pass


def method_A():
    pass


def method_B():
    # this is OK
    a = (some_variable_with_long_name
         + another_one_with_long_name_really_long_name
         - and_another_one_with_long_name
         + something_else)

# 1.global method/class definitions should be separated from other code
#   using two blank lines
# 2.methods in a class definition should be separated with one blank line
# 3.the +-*/% operators such as in method_B should break the line before,
#   not after their appearance. If after, the operators are scattered, 
#   depending on the line length