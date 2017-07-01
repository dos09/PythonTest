from lxml import etree

def xml_from_file(filename):
    tree = etree.parse(filename)
    return tree.getroot()

def test_traverse01(root):
    # print('root tag text: "%s"' % (root.text))
    # print(type(root.iterchildren()))
    for child in root.iterchildren():  # root.iter(tag=etree.Element):
        print(etree.tostring(child))
        print('tag name: "%s"' % (child.tag))
        print('tag attributes: "%s"' % (child.attrib))
        print('tag text: "%s"' % (child.text))
        print('type of the tag:', type(child), type(child) == etree._Element)
        print('############################################################')

def test_traverse02(element, num=0):
    for child in element.iterchildren():
        if(type(child) == etree._Element):
            print(num * ' ', child.tag)
            test_traverse02(child, num + 4)

def collect_data(element):
    node = Node()
    node.tagname = element.tag
    node.attrib = dict(element.attrib)
    try:
        text = element.text.strip()
        node.text = text if text else None
    except:
        pass
    
    for child in element.iterchildren():
        if(type(child) == etree._Element):
            child_node = collect_data(child)
            node.children.append(child_node)
    
    return node

class Node:
    def __init__(self):
        self.tagname = None
        self.attrib = {}
        self.text = None
        self.children = []
    
    def print_all(self, num=0):
        offset = num * ' '
        print(offset, self.tagname, self.attrib, self.text)
        for child in self.children:
            child.print_all(num + 4)
            
    def print_structure(self, num=0):
        offset = num * ' '
        print(offset, self.tagname, list(self.attrib.keys()))
        for child in self.children:
            child.print_structure(num + 4)
    
    def attributes_per_tag(self, dict):
        attr_set = dict.get(self.tagname, set())    
        for attr_name in self.attrib.keys():
            attr_set.add(attr_name)
        dict[self.tagname] = attr_set
        for child in self.children:
            child.attributes_per_tag(dict)
            
root = xml_from_file('army_small.xml')
# test_traverse01(root)
# test_traverse02(root)

root_node = collect_data(root)
root_node.print_all()
# root_node.print_structure()

dict = {}
root_node.attributes_per_tag(dict)
for key in sorted(dict):
    print(key, sorted(dict[key]))