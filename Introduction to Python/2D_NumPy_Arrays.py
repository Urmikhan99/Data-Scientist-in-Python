import numpy as np

np_2d = np.array([
    [1.73, 1.68, 1.71, 1.89, 1.79],   
    [65.4, 59.2, 63.2, 88.4, 65.7]    
])

print(np_2d)

'''
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the type of np_baseball.
Print out the shape attribute of np_baseball. Use np_baseball.shape.
'''

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)


'''
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the shape attribute of np_baseball.
'''
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

'''
Print out the 50th row of np_baseball.
Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
Select the height (first column) of the 124th baseball player in np_baseball and print it out.
'''

import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print("All weights:",np_weight_lb)

# Print out height of 124th player
print("Height of 124th player:", np_baseball[123, 0])

# 2D Arithmetic
'''
You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
Multiply np_baseball with conversion and print out the result.
'''
import numpy as np

np_baseball = np.array(baseball)
updated = np.array([
    [0, 2, 0],
    [1, 3, 1],
    [0, 0, 0],
    [2, 1, 0]
])
# Print out addition of np_baseball and updated
print("Addition of np_baseball and updated:\n", np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print("np_baseball converted to metric units:\n", np_baseball * conversion)