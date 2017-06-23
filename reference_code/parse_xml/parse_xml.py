from lxml import etree

def make_xml_structure():
    root = etree.Element("warriors")
    print(etree.tostring(
        etree.Element("orc",
                      attrib={ 
                          'strength': '1000',
                          'description' : 'one bad orc!' 
                      }
    )))
    print('>> tag name:', root.tag)
    child1 = etree.SubElement(root, "warrior")
    child2 = etree.SubElement(root, "archer")
    print('>> first child:', root[0].tag)
    print('>> count of child tags:', len(root))
    print(">> for c in root: print(c.tag):")
    for c in root:
        print(c.tag)
    root.set('type', 'horde')
    child1.set('name', 'Mogka')
    child1.set('armor', 'heavy')
    print(">> child1.get('name'):", child1.get('name'))
    print(">> for c in root: print(c.tag, c.attrib):")
    for c in root:
        print(c.tag, c.attrib)
    print('>> child1.keys()', child1.keys())
    print(">> for name, value in root.items(): print(name, value)")
    for name, value in root.items():
        print(name, value)
    child2.text = 'Gosho'
    print('>> child2:', etree.tostring(child2))
    print('child2.getparent():', child2.getparent().tag)
    return root

def get_test_xml_structure():
    root = etree.Element("root")
    root.append(etree.Comment("some comment"))
    c1 = etree.SubElement(root, "child")
    c1.text = "Child 1"
    c1.set('attr_1', 'attr_1_value')
    c1.set('attr_2', 'attr_2_value')
    c2 = etree.SubElement(root, "child")
    c2.text = "Child 2"
    c3 = etree.SubElement(root, "another")
    c3.text = "Child 3"
    
    print(etree.tostring(root, pretty_print=True))
    return root

def traverse_tree(root):
    # print without Comments. Entities, ProcessingInstructions
    for e in root.iter(tag=etree.Element):
        print(etree.tostring(e))
    
def xml_from_string():
    some_xml_data = "<root><child1 attr='value'>Gosho</child1></root>"
    root = etree.fromstring(some_xml_data)
    print(etree.tostring(root))
    
def xml_from_file(filename):
    tree = etree.parse('army.xml')
    root = tree.getroot()
    print(etree.tostring(root))
    

print('>>> make_xml_structure() <<<###################')
root = make_xml_structure()
print(etree.tostring(root))
print('>>> get_test_xml_structure <<<#################')
root = get_test_xml_structure()
print('>>> traverse_tree <<<##########################')
traverse_tree(root)
print('>>> xml_from_string <<<########################')
xml_from_string()
print('>>> xml_from_file <<<########################')
xml_from_file('army.xml')