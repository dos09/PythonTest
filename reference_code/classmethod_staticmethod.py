# classmethods are usually used for help initializers
class Warrior:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    @classmethod
    def from_string(cls, warrior_str):
        name, hp = warrior_str.split('-')
        return cls(name, hp)
    
    def __str__(self):
        return "{0} {1}".format(self.name, self.hp)
    
    @staticmethod
    def warrior_codex():
        print('warrior codex:...')
    
war = Warrior.from_string('Mogka-1200')
print(war)
war.warrior_codex()
Warrior.warrior_codex()