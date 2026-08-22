import numpy as np

arr = np.ones(8)
arr2 = np.random.randint(0, 10, 8)

print(arr)
print('')
print(arr2)
print('')


arr3 = arr + arr2

if arr3.sum() >= 40:
    print(arr3.reshape(4,2))
else:
    print(arr3.reshape(2,4))

