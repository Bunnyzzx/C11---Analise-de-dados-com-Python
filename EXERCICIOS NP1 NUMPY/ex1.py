import numpy as np

arr1 = np.ones(8)
arr2 = np.random.randint(0, 10, 8)
arr3 = arr1 + arr2
arr3S = np.sum(arr3)

if arr3S >= 40:
    mtz = arr3.reshape(4,2)
else:
    mtz = arr3.reshape(2,4)

print(mtz)