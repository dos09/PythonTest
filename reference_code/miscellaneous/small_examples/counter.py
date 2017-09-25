from collections import Counter

c = Counter('abcdabcda')

print(c)

for item in c.elements():
    print(item)
    
most_common = c.most_common(3)
print('most common:')
for item in most_common:
    print(item)

print("a is met %s times" % (c['a']))
print("z is met %s times" % (c['z'])) #doesn't exist