# coding : utf-8

from turtle import * # on importe le module turtle
speed(0) # on règle la vitesse à 0 car sinon c'est un peu long...
ht() # on cache la tortue, c'est plus net

up() # on lève le stylo
goto(-200,-200) # on se rend au point (-200,-200), pour pouvoir voir un plus grand nombre de figures. N'hésitez pas à encore descendre et reculer plus votre n est grand...
down() # on repose le stylo

def sierpinski(n : int,L : float):
    """
    fonction qui représente le tapis de sierpinski

    param n : int
    param L : float
    return : représentation de la figure

    Conseil d'utilisation : Pour une figure plus nette et agréable à voir, veuillez choisir une taille de L de plus en plus importante, plus votre n est grand (en étant raisonnable quand même...)
    
    """
    assert isinstance (n,int), 'n doit être un entier' # on vérifie que la valeur de n definie par l'utilisateur est bien un nombre entier, sinon message d'erreur
    assert n >= 0, 'n doit être positif ou égal à 0' # on vérifie que n est supérieur ou égal à 0

    # cas de base
    if n == 0 : # si n==0, alors on réalise le cas de base, la fonction dessine un carré, découpé en 9 carrés identiques avec le carré centrale qui est rempli
        for i in range(4) : # pour faire le carré global, on doit dessiner quatre côtés
            for i in range(3): # 3 carrés par côté du carré global
                for i in range(4): # pour faire un carré, on doit dessiner quatre côtés
                    forward(L/3) # on avance de (L/3) pixels
                    left(90) # on s'oriente à gauche de 90 ° (angles d'un carré = 90°)
                forward(L/3)
            left(90)
        # on se rend au carré central pour le remplir de la couleur défini quelques lignes plus bas. On revient ensuite au départ...
        up()
        left(90)
        forward(L/3)
        right(90)
        forward(L/3)
        down()
        fillcolor("#2D8F98") # on définit la couleur de remplissage comme bleu turquoise (code héxadécimal)
        begin_fill() # début du remplissage
        for i in range(4):
            forward(L/3)
            left(90)
        end_fill() # fin du remplissage
        left(180)
        forward(L/3)
        left(90)
        forward(L/3)
        left(90)
    # Partie récursive
    # On va pouvoir découper de façon plus automatique 9 carrés à l'itérieur d'un même carré qui seront eux aussi découpés de l'intérieur en 9 et ainsi de suite... 
    else : # si n!=0, alors on rentre dans la partie récursive
        for i in range(3):
            sierpinski(n-1,L/3) # de façon recursive, on réexecute la fonction sierpinski en soustrayant 1 à n et en divisant la longueur des côtés du carré par 3
            forward(L/3) 
        left(90)
        forward(L/3)
        for i in range(2): 
            for i in range(2) :
                sierpinski(n-1,L/3)
                forward(L/3)
            left(90)
            forward(L/3)
        sierpinski(n-1,L/3)
        forward(L/3)
        left(90)
        forward(L/3)
        fillcolor("darkred") # on définit la couleur de remplissage comme rouge foncé
        begin_fill()
        for i in range(4):
            forward(L/3)
            left(90)
        end_fill()
        left(180)
        forward(L/3)
        left(90)
        forward(L/3)
        left(90)

print(sierpinski(int(input('Quelle niveau (1,2,3,...) ? ')),int(input('Quelle longueur pour les côtés ? '))))
