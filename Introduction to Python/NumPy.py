import numpy as np
n=np.array((1,2,3))
print(n)
print(type(n))

'''
Import the numpy package as np, so that you can refer to numpy with np.
Use np.array() to create a numpy array from baseball. Name this array np_baseball.
Print out the type of np_baseball to check that you got it right.
'''

# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# NumPy arrays allow vectorized operations, which are faster and more efficient than Python lists.
# import numpy as np → correct way to import NumPy.

# np.array() converts a Python list into a NumPy array.

# NumPy arrays support vectorized operations for efficient computation.

'''
Create a numpy array from height_in. Name this new array np_height_in.
Print np_height_in.
Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
Print out np_height_m and check if the output makes sense.
'''

# Import numpy
import numpy as np
height_in = [74, 74, 72, 75, 75, 73]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254


# Print np_height_m
print(np_height_m)


'''
Create a numpy array from height_in. Name this new array np_height_in.
Print np_height_in.
Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
Print out np_height_m and check if the output makes sense.
'''


# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254


# Print np_height_m
print(np_height_m)


'''
Subset np_weight_lb by printing out the element at index 50.
Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
'''

import numpy as np
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 190, 220, 205, 185]
height_in = [74, 74, 72, 75, 75, 73, 70, 71, 69, 77, 76, 72]
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

# ✅ NumPy makes subsetting faster and more efficient compared to Python lists.