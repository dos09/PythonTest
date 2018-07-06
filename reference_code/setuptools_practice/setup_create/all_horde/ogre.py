from all_horde.common import Humanoid, print_file, abs_fname


class Ogre(Humanoid):
    TYPE = 'ogre'


def run():
    print(Ogre('Shrek'))
    print_file(abs_fname(__file__, 'shrek.txt'))
    print_file(abs_fname(__file__, 'shrek.dat'))


if __name__ == '__main__':
    run()
