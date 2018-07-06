import argparse

from all_horde.horde import orc, troll
from all_horde import ogre

ALL = 'all'
ORC = 'orc'
TROLL = 'troll'
OGRE = 'ogre'


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('horde-race', choices=[ALL, ORC, TROLL, OGRE])
    args = parser.parse_args()
    horde = getattr(args, 'horde-race')
    if horde == ALL:
        orc.run()
        troll.run()
        ogre.run()
    elif horde == ORC:
        orc.run()
    elif horde == TROLL:
        troll.run()
    elif horde == OGRE:
        ogre.run()
    else:
        print('FAIL')


if __name__ == '__main__':
    run()

"""
Using absolute import you can have
if __name__ == '__main__': ... 
in each file which eases the testing (especially testing small changes). 
"""