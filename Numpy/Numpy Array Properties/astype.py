import numpy as np

arr=np.array([1.2,2.5,3.8])
int_arr=arr.astype(int)

print(int_arr)
print(int_arr.dtype)

'''
📌 Short Note – .astype()

Definition:
.astype() is used to convert the data type of a NumPy array into another type.

Explanation:

arr.astype(int) → converts all elements from float to int

Decimal part is truncated, not rounded

Original array remains unchanged; a new array is created

Key Points:
✅ Common conversions: int, float, str, bool
✅ Useful for type consistency in calculations or ML models
✅ Always returns a new array 
'''
