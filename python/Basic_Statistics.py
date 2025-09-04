# Average versus median

'''
Create numpy array np_height_in that is equal to first column of np_baseball.
Print out the mean of np_height_in.
Print out the median of np_height_in.
'''

import numpy as np
baseball = [
    [74, 180, 23],
    [72, 215, 25],
    [73, 210, 22],
    [75, 188, 24],
    [78, 220, 26]  # maybe an unusually tall player (outlier)
]
np_baseball = np.array(baseball)
# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print("Mean height:", np.mean(np_height_in))

# Print out the median of np_height_in
print("Median height:", np.median(np_height_in))


'''
Mean = sensitive to extreme values → not always reliable if outliers exist.

Median = robust against outliers → often a better measure of “typical” value.
'''


# Explore the baseball data
'''The code to print out the mean height is already included. Complete the code for the median height.
Use np.std() on the first column of np_baseball to calculate stddev.
Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr.
'''
