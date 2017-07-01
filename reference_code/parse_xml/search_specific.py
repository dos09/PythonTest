from lxml import etree

class Army:
    def __init__(self):
        self.attr_version = None
        self.tag_warriors = []
    
    def print_me(self, offset=0):
        print(offset * ' ', '<army>')
        for war in self.tag_warriors:
            war.print_me(offset + 4)
    
class Warrior:
    def __init__(self):
        self.attr_class = None
        self.attr_rank = None
        self.attr_guardian = None
        self.tag_name = Name()
        self.tag_weapons = []
    
    def print_me(self, offset=0):
        print(offset * ' ', '<warrior>')
        print(offset * ' ', 'attr_class', self.attr_class)
        print(offset * ' ', 'attr_rank', self.attr_rank)
        print(offset * ' ', 'attr_guardian', self.attr_guardian)
        self.tag_name.print_me(offset + 4)
        for wep in self.tag_weapons:
            wep.print_me(offset + 4)
    
class Name:
    def __init__(self):
        self.text = None
    
    def print_me(self, offset=0):
        print(offset * ' ', '<name>')
        print(offset * ' ', 'text:', self.text)
    
class Weapon:
    def __init__(self):
        self.text = None
        
    def print_me(self, offset=0):
        print(offset * ' ', '<weapon>')
        print(offset * ' ', 'text:', self.text)

def xml_from_file(filename):
    tree = etree.parse(filename)
    return tree.getroot()

def collect_data(root):
    army = Army()
    army.attr_version = root.attrib['version']

    for elem_war in root.findall('warrior'):
        war = Warrior()
        war.attr_class = elem_war.attrib.get('class', None)
        war.attr_rank = elem_war.attrib.get('rank', None)
        war.attr_guardian = elem_war.attrib.get('guardian', None)
        war_name = Name()
        tag_name = elem_war.find('name')
        if tag_name is not None:
            war_name.text = tag_name.text
        war.tag_name = war_name
        elem_weapons = elem_war.find('.//weapons')
        if elem_weapons != None:
            for elem_weapon in elem_weapons.findall('weapon'):
                wep = Weapon()
                wep.text = elem_weapon.text
                war.tag_weapons.append(wep)
        army.tag_warriors.append(war)
    
    return army        
    
root = xml_from_file('army_small.xml')
army = collect_data(root)
army.print_me()
