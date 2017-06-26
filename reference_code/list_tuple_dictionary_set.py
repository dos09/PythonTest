# List, Tuple, Dictionary, Set
##############################
mylist = [31, "value", 3.44]
print("mylist: " + str(mylist))
mytuple = (66, 2, "asd", 0.4)  # immutable array
print("mytuple: " + str(mytuple))
mydictionary = {1:3, "a" : "valA", 44: "some"}
print("mydictionary: " + str(mydictionary))
print("mylist[0]: " + str(mylist[0]))
print("mytuple[0]: " + str(mytuple[0]))
print("mydictionary[\"a\"]: " + mydictionary["a"])
mylist.append("asda")
print("mylist: " + str(mylist))
print("mylist[:]: " + str(mylist[:]))  # from first to last. When omit start index = first, when omit end index = last
print("mylist[0:len(mylist)]: " + str(mylist[0:len(mylist)]))  # end index is exclusive
print("mylist[-3:-1]: " + str(mylist[-3:-1]))
print("mylist[:2]: " + str(mylist[:2]))
print("mylist[::2]: " + str(mylist[::2]))  # specify step
myset = {1, 2, 3, 3, 3, 4, 4, 1, 2}
print(myset)
print('dictionary traversing:')
dict = { 'a' : 'letter a', 'b' : 'letter b'}

for key in dict:
    print(key, dict[key])
for k, v in dict.items():
    print(k, v)
