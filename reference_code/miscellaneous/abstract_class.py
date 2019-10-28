import abc


# class Orc(metaclass=abc.ABCMeta): # same as below
class Orc(abc.ABC):  # same as above

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def attack(self):
        # abstract methods in Python can have implementation and
        # can be invoked with super
        print('%s fist attack' % self.name)


class OrcWarrior(Orc):

    def attack(self):
        super().attack()
        print('%s sword attack' % self.name)


def run():
    obj = OrcWarrior('Mogka')
    obj.attack()


if __name__ == '__main__':
    run()
