# multi-Dimensional Array
# matrix

import numpy as np
matrix=np.array([[2,4,6],
                 [8,9,12]
                 ])
print(matrix)


'''
📌 Short Note – Multi-Dimensional Array (Matrix)

Definition:
A multi-dimensional array has more than one dimension.

1D → single row (linear)

2D → rows & columns (matrix)

Higher dimensions → arrays inside arrays (like 3D cubes).

Code Explanation:

np.array([[2,4,6],[8,9,12]]) → creates a 2D matrix with 2 rows × 3 columns.

Shape → (2, 3) → 2 rows, 3 columns.

Features of Multi-Dimensional Arrays:
✅ Efficient for handling large data (e.g., images, datasets).
✅ Indexing by row & column (e.g., matrix[0,1] → 4, matrix[1,2] → 12).
✅ Can perform matrix operations (addition, multiplication, transpose, etc.).


'''