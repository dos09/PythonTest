import re
print('search and match')
# The re.search() expression scans through a string looking
# for the first location where the regex pattern produces a match.
# returns MatchObject or None
print(bool(re.search(r"ly", "similarly")))
# The re.match() expression only matches at the beginning of the string.
print(bool(re.match(r"ly", "similarly")))
print(bool(re.match(r"ly", "ly in the beginning")))

print('split')
print(re.split('[,.]', '1,2..3'))

print('group')
m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
print(m.group(0))  # the entire match
print(m.group(1))  # the first subgroup
print(m.group(1, 2, 3))  # returns tuple of the matches for the given groups

print('groups')
# A groups() expression returns a tuple containing all
# the subgroups of the match.
print(m.groups())

print('groupdict')
# A groupdict() expression returns a dictionary containing all
# the named subgroups of the match, keyed by the subgroup name.
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)',
             'myname@hackerrank.com')
print(m.groupdict())

# match the first alphanumeric symbols that repeats
print('reference a group in regex by name or index (1-based)')
r1 = re.search(r'(?P<first>[a-zA-Z0-9]).*(?P=first)', '..123asda')
r2 = re.search(r'([a-zA-Z0-9]).*\1', '..123asda')
print(r1, 'match:', 'no match' if r1 is None else r1.group('first'))
print(r2, 'match:', 'no match' if r2 is None else r2.group(1))

# findall and finditer are for non-overlapping matches
print('findall')
text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly", text))
print('finditer')
for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)), m.span())

print('re.sub - replace matches')
# Squaring numbers


def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 haha4 5 6 7 8 9"))

# match as short as possible
s = '1234 56'
print(re.search('\d+', s))
print(re.search('\d+?', s))  # match as short as possible

# surround matched groups with dashes
print(re.sub(r'((a)|(b))', r'-\1-', 'abcd'))

print('don\'t capture group (?:)')
m = re.match('(a)(?:b)', 'ab')
print(m.groups())