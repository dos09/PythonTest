mylist = [31, "value", 3.44]
print("mylist: " + str(mylist))
print("mylist[0]: " + str(mylist[0]))
mylist.append("asda")
print("mylist: " + str(mylist))
# from first to last. When omit start index = first, when omit end index = last
print("mylist[:]: " + str(mylist[:]))
# end index is exclusive
print("mylist[0:len(mylist)]: " + str(mylist[0:len(mylist)]))
print("mylist[-3:-1]: " + str(mylist[-3:-1]))
print("mylist[:2]: " + str(mylist[:2]))
print("mylist[::2]: " + str(mylist[::2]))  # specify step

squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)

for i, v in enumerate(['b','a', 'e']):
    print(i, v)
    
letters = ['A', 'B']
fruits = ['Apple', 'Banana']

for l, f in zip(letters, fruits):
    print('Fruit with letter %s: %s' % (l, f))