import numpy as np
arr_np=np.array([[1,2,3],
                 [4,5,6]])
print(arr_np.shape)

'''
📌 Short Note – array.shape

Definition:
.shape attribute returns the dimensions of a NumPy array as a tuple.

Explanation:

arr_np is a 2D array with 2 rows and 3 columns

Output of .shape: (2, 3)

Key Points:
✅ 1D array → (number_of_elements,)
✅ 2D array → (rows, columns)
✅ 3D array → (blocks, rows, columns)
✅ Useful to check size and structure of arrays before operations
'''