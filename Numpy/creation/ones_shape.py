# ones(shape)
import numpy as np
ones_array =np.ones((2,3))

print(ones_array)

'''
📌 Short Note – np.ones()

Definition:
np.ones(shape) creates an array filled with ones (1.0).

Code Explanation:

np.ones((2,3)) → makes a 2D array with 2 rows × 3 columns.

Stored as:

[[1. 1. 1.]
 [1. 1. 1.]]


By default, dtype = float.

Features:
✅ Useful for initializing arrays with default values of 1.
✅ Works with any dimension (1D, 2D, 3D, …).
✅ Can specify data type → np.ones((2,3), dtype=int) → integer ones.

Output:

[[1. 1. 1.]
 [1. 1. 1.]]

👉 Use np.ones() when:

You need an array full of 1s for testing, initialization, or math operations.

You want a uniform array to scale into any value (by multiplying).

You are working in machine learning, linear algebra, image processing where such matrices are required.
 

'''