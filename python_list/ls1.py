import numpy as np

ls = [1, 2, 3, 4]
ls2 = [5, 9, 10, 21]
print(ls + ls2)
print(ls + np.array([4])) #be hameye azaye ls oon meghdar ezafe shode
# print(ls + np.array([5, 5]))
print(2 * ls)
arr2 = np.array([1, 2, 3, 4])
print(2 * arr2)
print(arr2 ** 2)
print(arr2 - 10)
print(np.sqrt(arr2))
print(np.tanh(arr2))
arr3 = np.array([2, 4, 6, 9])
dot = 0
for e, f in zip(arr3, arr2):
    dot += e * f
print(dot)
print((arr2 * arr3).sum())
print(np.linalg.norm(arr2))
x1 = [2, 2]
x2 = [3, 3]
print(np.linalg.norm(x1))

