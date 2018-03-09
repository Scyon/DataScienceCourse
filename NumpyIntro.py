import numpy as np


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = np.array(list)
print(array)

print('-'*40)

list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = np.array(list2)
print(array2)

print('-'*40)

array3 = np.arange(10)
print(array3)

print('-'*40)

array4 = np.ones((3, 4))
print(array4)

print('-'*40)

array5 = np.linspace(0, 10, 5)
print(array5)

print('-'*40)

array6 = np.eye(4)
print(array6)

print('-'*40)

array7 = np.random.rand(4, 4)
print(array7)

print('-'*40)
# random values from random normal distribution centered at 0
array7 = np.random.randn(4, 4)
print(array7)

print('-'*40)

array8 = np.random.randint(0, 100, 5)
print(array8)