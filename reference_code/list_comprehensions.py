# List comprehensions
##################### 
# provide a powerful way to create and manipulate lists. 
# They consist of an expression followed by a 'for' clause followed by zero or more 'if' or 'for' clauses

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print("lst1: " + str(lst1))
print("lst2: " + str(lst2))
print("[x * y for x in lst1 for y in lst2]: " + str([x * y for x in lst1 for y in lst2]))
print("[x for x in lst1 if 4 > x > 1]: " + str([x for x in lst1 if 4 > x > 1]))
# Check if a condition is true for any of the items.
# 4 % 3 = 1, and 1 is true, so any() returns True
print("any([i % 3 for i in [3, 3, 4, 4, 3]]): " + str(any([i % 3 for i in [3, 3, 4, 4, 3]])))
print("sum(1 for i in [3, 3, 4, 4, 3] if i == 4): " + str(sum([1 for i in [3, 3, 4, 4, 3] if i == 4])))

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([item for row in m for item in row])

def print_row_item(item, row):
    print(row)
    print(item)

[print_row_item(item, row) for row in m for item in row]