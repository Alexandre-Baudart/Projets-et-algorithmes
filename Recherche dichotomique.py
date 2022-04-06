def recherche_dichotomique(tab : list, x : int) -> int :
    """
    fonction qui renvoie la position d'une valeur 'x' dans un tableau selon
    la méthode de la recherche dichotomique

    param tab : list
    param x : int
    return : int

    CU(conditions d'utilisation) : la liste 'tab' doit être triée avant
    d'utiliser la fonction 'recherche_dichotomique'

    """
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite :
        milieu = (gauche + droite)//2
        if tab[milieu] < x :
            gauche = milieu + 1
        elif tab[milieu] > x :
            droite = milieu - 1
        else :
            return milieu

if __name__ == '__main__' :
    assert recherche_dichotomique([1,4,6,8],6) == 2
    assert recherche_dichotomique([5,11,13,32,32],5) == 0
