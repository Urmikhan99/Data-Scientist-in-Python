# 2-Dimensional Array

import numpy as np

arr_2d =np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr_2d)

'''
📌 Short Note – Two-Dimensional Array

Definition:
A 2D array stores data in rows and columns, just like a table or matrix.

Code Explanation:

np.array([[1,2,3],[4,5,6],[7,8,9]]) → creates a 2D array (matrix).

arr_2d looks like:

[[1 2 3]
 [4 5 6]
 [7 8 9]]


Shape → (3, 3) → 3 rows × 3 columns.

Features of 2D Array:
✅ Works like a matrix in mathematics.
✅ Supports row/column access (e.g., arr_2d[0] → [1 2 3], arr_2d[:,1] → [2 5 8]).
✅ Useful for tabular data, images, linear algebra, etc.
✅ Vectorized operations are possible (e.g., arr_2d * 2).
'''