import itertools

# the input iterable must be sorted with the same key_func
# used in the group by

key_func = lambda x: x % 2 == 0
arr = [1,2,3,4,6]
arr.sort(key=key_func)
print(arr)
for key, it in itertools.groupby(arr, key=key_func):
    print('key', key)
    for item in it:
        print(item)