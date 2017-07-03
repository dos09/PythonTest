import json

class Orc:
    def __init__(self, name, kills):
        self.name = name
        self.kills = kills
        self.weapons = ['2hsword', '2haxe']
    
    @classmethod
    def from_dict(cls, dict):
        orc = Orc(None, 0)
        orc.__dict__.update(dict)
        return orc
    
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.kills, self.weapons)

def json_builin_types():
    print('### json with built-in types ###')
    
    a = ['adasd', 'asfasfas']
    b = {'Asen':'Sliven', 'Ivan':'selo'}
    
    # json.dumps - for built-in types
    
    json_a = json.dumps(a) # the trailing 's' is for string
    json_b = json.dumps(b)
    print(json_a)
    print(json_b)
    a = json.loads(json_a) # the trailing 's' is for string
    print(type(a), a)
    b = json.loads(json_b)
    print(type(b), b)

def json_custom_types():
    print('### json with custom types ###')

    orc = Orc('Ra', 210)
    json_orc = json.dumps(orc.__dict__)
    print('json_orc:', json_orc)
    orc_dict = json.loads(json_orc)
    orc.name = 'Scrappy'
    print(orc)
    orc.__dict__.update(orc_dict)
    print(orc)
    new_orc = Orc.from_dict(orc_dict)
    print('new_orc:', new_orc)

def json_file_read_write():
    orc1, orc2 = Orc('Mogka', 140), Orc('Ra', 103)
    fname = 'some_file'

    with open(fname, 'w') as f:
        f.write(json.dumps(orc1.__dict__) + "\n")
        f.write(json.dumps(orc2.__dict__) + "\n")
    with open(fname, 'r') as f:
        for line in f:
            stripped = line.strip()
            print("'%s'" % stripped)
            orc = Orc.from_dict(json.loads(stripped))
            print(orc)
    

# json_builin_types()
# json_custom_types()
json_file_read_write()