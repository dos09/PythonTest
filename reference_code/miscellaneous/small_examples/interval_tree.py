from intervaltree import IntervalTree

itree = IntervalTree()
itree[1:3] = '1-3'  # end range is exclusive
itree[6:10] = '6-10'
s = list(itree[2])  # set of Interval objects is returned
# now s = [Interval(1, 3, '1-3')]
test_interval = s[0]
print(test_interval.data)


itree = IntervalTree()
itree[int(1).to_bytes(16, 'big'):int(3).to_bytes(16, 'big')] = '1-3'
itree[int(6).to_bytes(16, 'big'):int(10).to_bytes(16, 'big')] = '6-10'
s = list(itree[int(6).to_bytes(16, 'big')])
if s:
    test_interval = s[0]
    print(test_interval.data)
else:
    print(s)

for i in itree:
    print(i)
