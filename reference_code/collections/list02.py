a = [1, 2, 3, 1]
a.insert(0, 10)
print(a)
a.remove(1) # by element
print(a)
a.append(22)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.pop())
print(a.pop(2)) # by index
print(a)

arr = [('abc', 121),('abc', 231),('abc', 148), ('abc',221)]
#arr = sorted(arr, key=lambda x: x[1]) # creates new list
arr.sort(key=lambda x: x[1]) # in place sort (modifies the list)
print(arr)
