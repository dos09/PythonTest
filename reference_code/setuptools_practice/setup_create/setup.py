import os

from setuptools import setup, find_packages

VERSION = '0.0.1'
NAME = 'practice-setuptools'
ENTRY_POINTS = {
    'console_scripts': [
        'horde = all_horde.run:run',
        'orc = all_horde.horde.orc:run',
        'troll = all_horde.horde.troll:run',
        'ogre = all_horde.ogre:run',
        'p1 = p1.p:run'
    ]
}
DEPENDENCIES = (
    'python-dateutil >= 2.7.0',
)


def run():
    setup(
        name=NAME,
        version=VERSION,
        packages=find_packages(),
        include_package_data=True,  # see the MANIFEST.in,
        entry_points=ENTRY_POINTS,
        install_requires=DEPENDENCIES
    )

if __name__ == '__main__':
    run()

"""
Useful setup kwargs:

- include_package_data: If set to True, this tells setuptools to automatically 
include any data files it finds inside your package directories that are 
specified by your MANIFEST.in file
!!! the order of the commands in the MANIFEST matters 
MANIFEST.in (all commands):
    include pat1 pat2 ...    include all files matching any of the listed patterns
    exclude pat1 pat2 ...    exclude all files matching any of the listed patterns
    recursive-include dir pat1 pat2 ...    include all files under dir matching any of the listed patterns
    recursive-exclude dir pat1 pat2 ...    exclude all files under dir matching any of the listed patterns
    global-include pat1 pat2 ...    include all files anywhere in the source tree matching - & any of the listed patterns
    global-exclude pat1 pat2 ...    exclude all files anywhere in the source tree matching - & any of the listed patterns
    prune dir    exclude all files under dir
    graft dir    include all files under dir

- exclude_package_data: A dictionary mapping package names to lists of glob 
patterns that should be excluded from your package directories. You can use 
this to trim back any excess files included by include_package_data.

- package_data: A dictionary mapping package names to lists of glob patterns.
This can be used instead of "include_package_data" + MANIFEST.in

- install_requires: A string or list of strings specifying what other 
distributions need to be installed when this one is. 

- entry_points: A dictionary mapping entry point group names to strings or 
lists of strings defining the entry points. 

- extras_require: A dictionary mapping names of "extras" 
(optional features of your project) to strings or lists of strings specifying 
what other distributions must be installed to support those features.

- setup_requires: A string or list of strings specifying what other 
distributions need to be present in order for the setup script to run.
(Note: projects listed in setup_requires will NOT be automatically 
installed on the system where the setup script is being run. They are simply 
downloaded to the ./.eggs directory if they're not locally available already. 
If you want them to be installed, as well as being available when the setup 
script is run, you should add them to install_requires and setup_requires.)

- tests_require: If your project's tests need one or more additional packages 
besides those needed to install it, you can use this option to specify them. 
It should be a string or list of strings specifying what other distributions 
need to be present for the package's tests to run

-------------------------------------------------------------------------------

find_packages()

Has two keywords "include" and "exclude". First includes packages described
in the "include" then, uses the "exclude" to remove from the matched packages.
The default for "include" is the directory where the setup.py file is.

For directory structure:
setup_create
    all_horde (package)
        horde (package)
    p1 (package)

This code:
a = find_packages()
b = find_packages(include=['*'])
c = find_packages(include=['all_horde*', 'p1'])
d = find_packages(include=['all_horde', 'p1'])
print('a = %s\nb = %s\nc = %s\nd = %s' % (a, b, c, d))

Will give:
a = ['all_horde', 'p1', 'all_horde.horde']
b = ['all_horde', 'p1', 'all_horde.horde']
c = ['all_horde', 'p1', 'all_horde.horde']
d = ['all_horde', 'p1']

"""
