# total number of elemants of array
import numpy as np
arr=np.array([[10,20,30],[40,50,60]])
print(arr.size)

'''
📌 Short Note – .size

Definition:
.size returns the total number of elements in a NumPy array.

Explanation:

For a 2D array with shape (2,3) → total elements = 2 × 3 = 6

Output = 6

Key Points:
✅ Works for 1D, 2D, 3D arrays
✅ Useful to count elements before reshaping or processing
✅ Faster than manually counting elements 
'''