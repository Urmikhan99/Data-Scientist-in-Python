# default value (zeros).
# np.zeros(shape)(3) for id,(3,3),2d

import numpy as np
zeros_array=np.zeros(3)
print(zeros_array)

'''
📌 Short Note – np.zeros()

Definition:
np.zeros(shape) creates an array filled with zeros by default.

Code Explanation:

np.zeros(3) → creates a 1D array with 3 elements: [0. 0. 0.]

np.zeros((3,3)) → creates a 2D array (matrix) with shape 3×3:

[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]


By default, dtype = float.

Features:
✅ Useful for initializing arrays before filling with values.
✅ Works with any shape (1D, 2D, 3D, …).
✅ Fast & memory efficient.

Output (for np.zeros(3)):

[0. 0. 0.]
'''