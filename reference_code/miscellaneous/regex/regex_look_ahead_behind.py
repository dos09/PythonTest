import re

# positive lookahead
# matches def if followed by abc, without consuming the abc
print(re.search('def(?=abc)', 'defabc'))
# negative lookahead
# matches def if not followed by abc without consuming the xxx
print(re.search('def(?!abc)', 'defabc'))
print(re.search('def(?!abc)', 'defxxx'))

# positive lookbehind
# matched def if preceded by abc without consuming the abc
print(re.search('(?<=abc)def', 'abcdef'))
# negative lookbehind
# matches def if not preceded by abc without consuming the xxx
print(re.search('(?<!abc)def', 'abcdef'))
print(re.search('(?<!abc)def', 'xxxdef'))
