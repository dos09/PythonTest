import re
#s = 'As Afasd imalosEdno AbcDef'
#s = 'As As'
s = 'AsasfAAs'
pattern = re.compile(r'(([A-Z][a-z])|([A-Z][A-Z][a-z])).*(\1|\2)')
# (?:) - means not to capture that group
# .*? - match any symbols as short as possible 

# res = pattern.match(s)
# print(res)

for m in pattern.finditer(s):
    print(m)
    print(m.groups())