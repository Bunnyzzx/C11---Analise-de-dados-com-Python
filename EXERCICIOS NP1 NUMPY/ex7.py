import numpy as np
np.random.seed(7)

arr0 = np.random.randint(1,11,(5))
arr1 = np.random.randint(1,11,(5))
arr3 = np.concatenate((arr0,arr1))
mtz = arr3.reshape(2,5)
print(mtz)