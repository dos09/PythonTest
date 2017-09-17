import itertools

print('product (cartesian)')

a = [1, 2]
b = [7, 8, 9]
cartesian_product = list(itertools.product(a, b))
print(*cartesian_product)

print('permutations') # order matters

res = list(itertools.permutations([1, 0]))
print(*res)
# permutations are done based on position not on value
# so when there are repeating elements in the input iterable
# there will be repeating permutations
res = list(itertools.permutations([1, 0, 1]))
print(*res)
# permutations with given length
res = list(itertools.permutations([1, 2, 3], r=2))
print(*res)
# if the input element are sorted the permutations will also be sorted

print('combinations') # order doesn't matter

s, k = 'HACK', 2
for r in range(1, int(k) + 1):
    for item in itertools.combinations(sorted(s), r=r):
        print(*item, sep='')
        
print('combinations with replacement') 
# start combining from current element, not from next
# e.g. current is combined with current

s, k = 'HACK', 2
for item in itertools.combinations_with_replacement(sorted(s), r=int(k)):
    print(*item, sep='')