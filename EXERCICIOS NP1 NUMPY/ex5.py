import numpy as np

mtz0 = np.zeros([3,3])
mtz1 = np.ones([3,3])

mtz2 = mtz0 + mtz1
mtz3 = mtz2 * 6

arr = mtz3.reshape(9)
print(arr)
