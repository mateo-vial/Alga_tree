from functions import *

arbre = [1, [2, [5], [6]], [3], [4, [7, [10], [11]], [8], [9]]]
sous_arbre = [100, [1000, [3000]], [2000]]

print(arbre)

ajouter_branche(arbre, [3, 1], sous_arbre)

print(arbre)

supprimer_branche(arbre, [3,1,3])

print(arbre)