class Orc:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        #Orc.asd()
        
    def __str__(self):
        return "%s - %s" % (self.name, self.hp)
    
    def __eq__(self,other):
        return (self.name == other.name and
                self.hp == other.hp)
    
    def __hash__(self):
        return hash((self.name, self.hp))
    
    @staticmethod
    def asd():
        print('stattttic')
    
a = Orc('aaa', 100)
print(a.__hash__())
b = Orc('bbb', 200)
dup = Orc('aaa', 100)
print(dup.__hash__())
myset = set()
myset.add(a)
myset.add(b)
myset.add(dup)
for x in myset:
    print(x)
    
print(len(myset))
