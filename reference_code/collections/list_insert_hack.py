a = [1, 2, 3]
a[0:2] = [8, 9, 10, 11] # replace the slice
print(a)
a[1:1] = [4, 4] # when start index = end index (which is exclusive)
# it inserts before that index
print(a)