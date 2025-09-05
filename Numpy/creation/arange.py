# creating sequence of numbers in numpy
#arange()
#arang(start,stop,step)

import numpy as np
arr=np.arange(1,10,2)
print(arr)






'''
What is np.arange()?

np.arange() is a NumPy function used to create arrays with a sequence of numbers.

It works like Python’s range() but returns a NumPy array instead of a list.
arr = np.arange(1, 10, 2)
start = 1 → sequence starts from 1

stop = 10 → sequence goes up to 10, but not including 10

step = 2 → each number increases by 2
Often used in loops, plotting, data generation, and simulations.
✅ Similar to Python range(), but returns a NumPy array
start → starting number (inclusive)

stop → end number (exclusive)

step → increment between numbers
'''