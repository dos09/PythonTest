# option 1 ##################
# import mypackage
# from mypackage import mymodule  
# mymodule.func()
#############################

# option 2 ##################
# import mypackage.mymodule
# mypackage.mymodule.func()
#############################

# option 3 ##################
# from mypackage import mymodule
# mymodule.func()
#############################

# option 4 ##################
from mypackage.mymodule import func
func()
#############################

# option 5 ##################
# from mypackage.mymodule import *
# func()
#############################