# full (shape,value)
import numpy as np

filled_array=np.full((2,2),7)
print(filled_array)


'''
🔑 Key Points
np.full((2,2), 7) → 2 rows × 2 columns, all elements = 7
np.full(shape, value) is flexible: can fill any shape with any value.

Works for integers, floats, or even strings.

Useful for initialization, testing, or creating constant arrays.
'''