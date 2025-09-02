'''
Import the math package.
Use math.pi to calculate the circumference of the circle and store it in C.
Use math.pi to calculate the area of the circle and store it in A.
'''


# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Imports the entire math module.
# You can use pi directly without the math. prefix.


'''
Perform a selective import from the math package where you only import the pi function.
Use pi to calculate the circumference of the circle and store it in C.
Use pi to calculate the area of the circle and store it in A.
'''


# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))