empty = ''
val1 = 'val 1'
val2 = 'val 2'
print(empty or val1)
print((empty and val1) or val2)
print(val1 and val2)
print("'%s'" % (empty or False))
print("'%s'" % (None and False))

# The Boolean operators 'and' and 'or' are so-called short-circuit operators: 
# their arguments are evaluated from left to right, 
# and evaluation stops as soon as the outcome is determined.