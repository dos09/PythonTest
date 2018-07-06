from all_horde.common import Humanoid, print_file, abs_fname


class Orc(Humanoid):
    TYPE = 'orc'


def run():
    print(Orc('Mogka'))
    print_file(abs_fname(__file__, 'mogka.txt'))
    print_file(abs_fname(__file__, 'mogka.dat'))

if __name__ == '__main__':
    run()
