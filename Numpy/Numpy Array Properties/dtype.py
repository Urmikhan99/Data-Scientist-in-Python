import numpy as np 
arr=np.array([10,20,30.5,40])
print(arr.dtype)


'''
📌 Explanation – .dtype

What is .dtype?

.dtype means data type of elements inside a NumPy array.

NumPy automatically chooses the best common type for all elements.

In your code:

Values: [10, 20, 30.5, 40]

Since one value is float (30.5) → NumPy converts all elements to float64 (to maintain same type).

Output:

float64


Key Points:
✅ .dtype tells whether array elements are int32, float64, complex, bool, etc.
✅ NumPy arrays must have same data type for all elements.
✅ You can set data type manually:

arr = np.array([1,2,3], dtype=float)
print(arr.dtype)  # float64
'''