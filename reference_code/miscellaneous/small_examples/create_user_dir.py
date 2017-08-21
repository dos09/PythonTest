from pathlib import Path
import os

def assure_user_dir(dir_name):
    """Creates directory in the user's home directory"""
    home = str(Path.home())
    dir = os.path.join(home, dir_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
        print('created directory: %s' % dir)
    return dir
    
assure_user_dir('asd')