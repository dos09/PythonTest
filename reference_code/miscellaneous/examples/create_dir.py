from pathlib import Path
import os
import tempfile
import shutil

def assure_user_dir(dir_name):
    """Creates directory in the user's home directory"""
    home = str(Path.home())
    dir = os.path.join(home, dir_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
        print('created directory: %s' % dir)
    return dir
    
assure_user_dir('asd')

def assure_random_dir(location=None):
    if location and (not os.path.exists(location) or 
                     not os.path.isdir(location)):
        raise ValueError('%s must be existing directory')

    dirpath = tempfile.mkdtemp(dir=location)
    print('Created random directory %s', dirpath)

    return dirpath

def test_random_dir():
    dir = assure_random_dir(str(Path.home()))
    # do something with dir
    shutil.rmtree(dir)
    print('Deleted %s' % (dir))
