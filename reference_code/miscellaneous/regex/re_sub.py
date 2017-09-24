import re

def convert(match):
    if match.group(0) == '&&':
        return 'and'
    return 'or'

s = 'A && || && || B || C'
print(re.sub(r'(?<= )((&&)|(\|\|))(?= )', convert, s))