# one-dimensional array

import numpy as np
ar_1d=np.array([10,20,30,40,50])
print(ar_1d)

'''
📌 Short Note – One-Dimensional Array

Definition:
A 1D array stores data in a single row (linear form).

Code Explanation:

np.array([10,20,30,40,50]) → creates a one-dimensional NumPy array.

ar_1d = [10 20 30 40 50]

Shape → (5,) means 5 elements in one dimension.

Features of 1D Array:
✅ Looks similar to a Python list but faster and optimized.
✅ Supports indexing & slicing (e.g., ar_1d[0] → 10, ar_1d[1:4] → [20 30 40]).
✅ Allows mathematical operations directly (e.g., ar_1d * 2 → [20 40 60 80 100]).
'''