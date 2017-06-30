class Orc:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def __eq__(self, other):
        return (self.name == other.name and
                self.hp == other.hp)
    
    def __hash__(self):        
        return hash((self.hp, self.name))
    
a = Orc('Gas',44)
b = Orc('Vas',45)
c = Orc('Das',99)
s = set()
s.add(a)
s.add(b)
s.add(c)

for o in sorted(s, key=lambda x: x.hp):
    print(o.name, o.hp)
    

        