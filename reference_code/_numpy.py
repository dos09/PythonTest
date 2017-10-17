import numpy  # must pip install it

arr = numpy.array([1, 2, '3'], float)
print(arr)

print('shape as getter')
my_1D_array = numpy.array([1, 2, 3, 4, 5])
print(my_1D_array.shape)  # (5,) -> 5 rows and 0 columns
my_2D_array = numpy.array([[1, 2], [3, 4], [6, 5]])
print(my_2D_array.shape)  # (3, 2) -> 3 rows and 2 columns
print('shape as setter (changes the original array)')
change_array = numpy.array([1, 2, 3, 4, 5, 6])
change_array.shape = (3, 2)
print(change_array)
print('reshape (creates new array)')
my_array = numpy.array([1, 2, 3, 4, 5, 6])
print(numpy.reshape(my_array, (3, 2)))

print('transpose')
my_array = numpy.array([[1, 2, 3],
                        [4, 5, 6]])
print(numpy.transpose(my_array))
print('flatten')
my_array = numpy.array([[1, 2, 3],
                        [4, 5, 6]])
print(my_array.flatten())

print('concatenate')
array_1 = numpy.array([[1, 2, 3], [0, 0, 0]])
array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])
print(numpy.concatenate((array_1, array_2), axis=0))
print(numpy.concatenate((array_1, array_2), axis=1))

print('construct array with given shape and type filled with zeros/ones')
print(numpy.zeros((1, 2)))
print(numpy.zeros((2, 2), int))
print(numpy.ones((1, 2)))

print('identity')
print(numpy.identity(3))
print('eye')
print(numpy.eye(4, 4, k=1))

print('floor, ceil rint')
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))

print('sum')
my_array = numpy.array([[1, 2], [3, 4]])
print(numpy.sum(my_array, axis=0))  # Output : [4 6]
print(numpy.sum(my_array, axis=1))  # Output : [3 7]
print(numpy.sum(my_array, axis=None))  # Output : 10
print(numpy.sum(my_array))  # Output : 10

print('prod')
my_array = numpy.array([[1, 2], [3, 4]])
print(numpy.prod(my_array, axis=0))  # Output : [3 8]
print(numpy.prod(my_array, axis=1))  # Output : [ 2 12]
print(numpy.prod(my_array, axis=None))  # Output : 24
print(numpy.prod(my_array))  # Output : 24

print('min')
my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print(numpy.min(my_array, axis=0))  # Output : [1 0]
print(numpy.min(my_array, axis=1))  # Output : [2 3 1 0]
print(numpy.min(my_array, axis=None))  # Output : 0
print(numpy.min(my_array))  # Output : 0

print('max')
my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print(numpy.max(my_array, axis=0))  # Output : [4 7]
print(numpy.max(my_array, axis=1))  # Output : [5 7 3 4]
print(numpy.max(my_array, axis=None))  # Output : 7
print(numpy.max(my_array))  # Output : 7

print('mean')
my_array = numpy.array([[1, 2], [3, 4]])
print(numpy.mean(my_array, axis=0))  # Output : [ 2.  3.]
print(numpy.mean(my_array, axis=1))  # Output : [ 1.5  3.5]
print(numpy.mean(my_array, axis=None))  # Output : 2.5
print(numpy.mean(my_array))  # Output : 2.5

print('var')
my_array = numpy.array([[1, 2], [3, 4]])
print(numpy.var(my_array, axis=0))  # Output : [ 1.  1.]
print(numpy.var(my_array, axis=1))  # Output : [ 0.25  0.25]
print(numpy.var(my_array, axis=None))  # Output : 1.25
print(numpy.var(my_array))  # Output : 1.25

print('std')
my_array = numpy.array([[1, 2], [3, 4]])
print(numpy.std(my_array, axis=0))  # Output : [ 1.  1.]
print(numpy.std(my_array, axis=1))  # Output : [ 0.5  0.5]
print(numpy.std(my_array, axis=None))  # Output : 1.11803398875
print(numpy.std(my_array))  # Output : 1.11803398875


print('dot')
A = numpy.array([1, 2])
B = numpy.array([3, 4])
print(numpy.dot(A, B))  # Output : 11
print('cross')
A = numpy.array([1, 2])
B = numpy.array([3, 4])
print(numpy.cross(A, B))  # Output : -2

print('inner')  # dot product on vectors
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print(numpy.inner(A, B))

print('outer')
A = numpy.array([2, 1])
B = numpy.array([3, 4])
print(numpy.outer(A, B))
