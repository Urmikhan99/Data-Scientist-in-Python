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