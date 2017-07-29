items = [1, 2, 4, 4, 2, 3]
print('items', items)
print('even items', list(filter(lambda x: x % 2 == 0, items)))
print('doubled items', list(map(lambda x: x * 2, items)))
print('min', min(items))
print('max', max(items))
print('set of items', set(items))
print('sorted items', sorted(items))
print('sum', sum(items))
print('tuple', tuple(items))
a = [1, 2, 3]
b = [8, 9]
print('zip of %s and %s = %s' % (a, b, list(zip(a, b))) )
print('1 in a:', 1 in a)
print('5 not in a:', 5 not in a)
# all elements must evaluate to True
print('all', all([1, 'asd', True]))
# at least one of the elements evaluates to True
print('any', any([0, False, None]))
