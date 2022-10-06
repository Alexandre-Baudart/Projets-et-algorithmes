# Création d'une liste aléatoire

import random

def liste_aleatoire(N : int,n : int) -> list :
    """
    fonction qui renvoie une liste aléatoire de taille N et 
    de nombres compris entre 0 et n

    param N : int
    param n : int
    return : list
    
    """
    data = [random.randrange(n) for i in range(N)]
    return data

# Fonction de permutation

def swap(T,i,j):
    """
    fonction qui permet de permuter deux éléments dans une liste
    """
    tmp = T[i]
    T[i] = T[j]
    T[j] = tmp
    return T

# 1/tri par sélection 

def tri_selection(T : list) -> list :
    """
    fonction qui renvoie une liste triée selon la méthode du tri par sélection

    param T : list
    return : list
    
    """
    for i in range(0,len(T)):
        mini = i
        for j in range(i+1,len(T)):
            if T[j] < T[mini] :
                mini = j
        if mini != i :
            swap(T,i,mini)
    return T


# 2/tri par insertion

def tri_insertion(T : list) -> list :
    """
    fonction qui renvoie une liste triée selon la méthode du tri par insertion

    param T : list
    return : list
    
    """ 
    for i in range(1,len(T)):
        j = i
        val = T[i]
        while j > 0 and val < T[j-1] :
            T[j] = T[j-1]
            j -= 1
        T[j] = val
    return T

# 3/tri à bulle

def tri_bulle(T : list) -> list :
    """
    fonction qui renvoie une liste triée selon la méthode du tri à bulle

    param T : list
    return : list
    
    """ 
    permut = True
    while permut :
        permut = False
        for i in range(0,len(T)-1):
            if T[i] > T[i+1] :
                swap(T,i,i+1)
                permut = True
    return T

# 4/tri fusion

from typing import List

def fusion(T1 : List[int], T2 : List[int], T : List[int]) -> None :
    i = 0
    j = 0
    while i + j < len(T) :
        if j == len(T2) or (i < len(T1) and T1[i] < T2[j]) :
            T[i + j] = T1[i]
            i += 1
        else :
            T[i + j] = T2[j]
            j += 1

def tri_fusion(T : List[int]) -> list :
    """
    fonction qui renvoie une liste triée selon la méthode du tri fusion

    param T : list
    return : list
    
    """ 
    n = len(T) 
    if n < 2 :
        return None
    else :
        milieu = n//2
        T1 = T[:milieu]
        T2 = T[milieu:] 

        tri_fusion(T1) 
        tri_fusion(T2) 

        fusion(T1, T2, T)
    return T




        

    







    



