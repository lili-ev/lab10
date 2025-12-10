
import numpy as np

A = np.array([10, 20, 30, 40, 50])
M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])

print("Tableau 1D A :", A)
print("Tableau 2D M :\n", M)

element_3 = A[2]     
element_fin = A[-1]   

print("A[2] =", element_3)
print("A[-1] =", element_fin)

valeur_12 = M[1, 2]      
valeur_dernier = M[-1, -1] 

print("M[1, 2] =", valeur_12)
print("M[-1, -1] =", valeur_dernier)

segment = A[1:4]
print("A[1:4] =", segment)  

print("A[:3]  =", A[:3])   
print("A[::2] =", A[::2])  

print("A[:-1] =", A[:-1])  
print("A[-3:] =", A[-3:]) 

sous_bloc = M[0:2, 1:]
print("M[0:2, 1:] =\n", sous_bloc)

ligne_2 = M[1, :]
print("Ligne 2 :", ligne_2)  

colonne_3 = M[:, 2]
print("Colonne 3 :", colonne_3) 

bloc_central = M[0:3, 1:3]
print("Bloc central :\n", bloc_central)

colonnes_alternées = M[:, ::2]  
print("Colonnes 0 et 2 :\n", colonnes_alternées)

vue = M[0:2, 1:3]
print("Vue initiale :\n", vue)

vue[0, 0] = 999
print("Vue modifiée :\n", vue)

print("M après modification via la vue :\n", M)

M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])
print("M réinitialisée :\n", M)

sous_copie = M[0:2, 1:3].copy()
print("Copie avant modification :\n", sous_copie)

sous_copie[0, 0] = 999
print("Copie modifiée :\n", sous_copie)

print("M restée intacte :\n", M)


