# import getpass
# print(getpass.getuser())

from pathlib import Path
import os

def assure_user_dir(dir_name):
    """Creates directory in the user's home directory"""
    home = str(Path.home())
    dir = os.path.join(home, dir_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    return dir
    
# dir = assure_user_dir('asd')
# print(dir)

d = {'key':'value'}
s = "edno {key}".format(key='vallllue')
print(s)

print('@xyz')
    