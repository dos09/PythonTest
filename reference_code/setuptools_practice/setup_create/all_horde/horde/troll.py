from all_horde.common import Humanoid


class Troll(Humanoid):
    TYPE = 'troll'


def run():
    print(Troll('Mofo'))

if __name__ == '__main__':
    run()
