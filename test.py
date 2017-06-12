m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([item for row in m for item in row])

def print_row_item(item, row):
    print(row)
    print(item)

[print_row_item(item, row) for row in m for item in row]