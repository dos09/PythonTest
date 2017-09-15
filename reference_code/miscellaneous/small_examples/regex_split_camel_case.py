import re
    
def check(s):
    pattern = re.compile(r'([a-z][^A-Z]+)|([A-Z][^A-Z]+)|(.+?)')
    for m in pattern.finditer(s):
        print("'%s'" % m.group(0))

data = ['AsadAf', 'fasAafa', 'asdAdaaFFas', 'onceUponATime', 'BaNan']
for d in data:
    print('---')
    check(d)