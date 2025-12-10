
import numpy as np

A = np.array([10, 20, 30, 40, 50])
M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])


M[:, -1] *= 10

M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])


bloc_vue = M[1:, :2] 
bloc_vue[:] = -1       
print("M après bloc -1 (via vue) :\n", M)

M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])


bloc_copy = M[1:, :2].copy()   
bloc_copy[:] = -1

print("Bloc copy modifié :\n", bloc_copy)
print("M (copie intacte) :\n", M)


A_original = A.copy()

A[1:-1] = 0
print("A modifié :", A)

A = A_original  

print("A restauré :", A)

