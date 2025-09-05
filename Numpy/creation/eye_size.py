# creating identify matrices
# eye(size)
import numpy as np
identity_matrix=np.eye(4)
print(identity_matrix)

'''
📌 Short Note – np.eye()

Definition:
np.eye(N) creates a square identity matrix of size N×N.
1 on the main diagonal
0 elsewhere

np.eye(N) → creates N×N identity matrix

Always 1 on diagonal, 0 elsewhere

Used in linear algebra, ML algorithms, initialization, and matrix operations
'''