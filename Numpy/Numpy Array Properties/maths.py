import numpy as np
arr=np.array([11000,20,30])
print(arr+5)
print(arr * 2)
print(arr ** 2)


'''
Explanation (short):

arr + 5 → Adds 5 to every element.

arr * 2 → Multiplies every element by 2.

arr ** 2 → Squares every element.

Vectorized operations in NumPy apply the operation to all array elements at once, no need for loops.
'''