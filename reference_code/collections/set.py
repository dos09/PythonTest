myset = {1, 2, 3, 3, 3, 4, 4, 1, 2}
print(myset)

s1 = set("a b c".split())
s2 = set("b x y".split())
print('s1:', s1)
print('s2:', s2)
print('s1 - s2:', s1 - s2)  # difference
print('s1 | s2:', s1 | s2)  # union
print('s1 & s2:', s1 & s2)  # intersection
# letters in s1 or s2 but not in both
print('s1 ^ s2:', s1 ^ s2)  # symmetric difference

# set comprehension
s = {x for x in 'abcdabcdabcd' if x not in 'bd'}
print(s)
