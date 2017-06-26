from lxml import etree
import re
# class A:
#     def __init__(self):
#         self.a = 'shrek'
# 
# obj = A()
# print(obj.a)
# print(getattr(obj, 'a'))
# try:
#     print(getattr(obj, 'b'))
# except AttributeError as ae:
#     print("getattr(obj, 'b') results in AttributeError:", ae)
# print(getattr(obj, 'b', 'donkey'))

# num = 1234567
# str = '{:,}'.format(num)
# print(type(str)) # <class 'str'>
# print(str) # 1,234,567

# print('failed ips ({:,}):'.format(4444, 1234))

# TODO: practice setdefault
# d = {}
# d.setdefault('a',1)
# print(d['a'])

def read_node_text(node):
    text = None
    
    try:
        text = node.text.strip()
        text = text if text else None
    except:
        pass
    print(node.tag)
    print("'%s'" % (text))
    return text

def read_node_text_clear_space(node):
    text = ''
    regex = re.compile('\s{2,}')
    try:
        text = node.text.strip()
        text = re.sub(regex, ' ', text)
    except:
        pass
#     print(node.tag)
#     print("'%s'" % (text))
    return text

def fix_whitespace(text):
    if text == None:
        text = ''
        
    regex = re.compile('\s{2,}')
    try:
        text = text.strip()
        text = re.sub(regex, ' ', text)
    except:
        pass
    
    return text

def _parse_all_text(elem, offset=0):
    # Text before the first subelement
    elem_text = fix_whitespace(elem.text)
    # Text after the element's end tag, but before the next sibling element's start tag
    elem_tail = fix_whitespace(elem.tail)
    elem_tagname = elem.tag.lower()
    offset_newline = (elem_tagname == 'paragraph' or 
                      elem_tagname == 'listitem')
    
    if elem_text:
        if offset_newline:
            text = (offset * ' ') + elem_text
        else:
            text = elem_text
    else:
        text = '' 
    
    # add url link in parentheses
    if elem_tagname == 'urllink':
        text = ' ' + text
        url = elem.attrib.get('LinkURL', '')
        if not url:
            url = elem.attrib.get('href', '')
        if text and url:
            text += ' ({0})'.format(url)
        
    if text:
        offset += 4
        
    for child in elem.iterchildren():
        if(type(child) == etree._Element):
            child_text = _parse_all_text(child, offset)
            if child_text:
                if text and not (child.tag.lower() == 'urllink'):
                    text += '\n' + child_text
                else:
                    text += child_text  
                    
    return text + elem_tail

def xml_from_file(filename):
    tree = etree.parse(filename)
    return tree.getroot()

# root = xml_from_file('vuln.xml')
# print(etree.tostring(root))
# text = _parse_all_text(root)
# print("'%s'" % (text))

d = {}
l = d.setdefault('a', [])
l.append(505)
l.append(4)
print(d)