# coding : utf-8

from turtle import * # on importe le module turtle
color(str(input('Quelle couleur ? '))) # on définit la couleur de remplissage et du stylo
shape("turtle") # on donne à la tortue une forme de tortue :)
speed(0) # on règle la vitesse à 0 car sinon c'est un peu long...

up() # on lève le stylo
goto(-200,-200) # on se rend au point de coordonnées(-200,-200) pour voir toute la figure, surtout quand n > 4
down() # on repose le stylo

def sierpinski(n : int,L : float):
    """
    fonction qui reproduit le triangle de sierpinski

    param n : int
    param L : float
    return : représentation de la figure

    Conseil d'utilisation : si vous souhaitez avoir une figure nette à partir de n > 4, nous vous conseillons d'augmenter la taille de L...

    """    
    assert isinstance (n,int), 'n doit être un entier' # on vérifie que n est un entier, sinon message d'erreur
    assert n >= 0, 'n doit être positif ou égal à 0' # on vérifie que n est superieur ou égal à 0
    
    # cas de base
    if n == 0 : # si n==0 alors on réalise le cas de base, la fonction dessine un seul triangle
        for i in range(3): # pour faire un triangle, on doit dessiner trois côtés
            forward(L) # on avance de (L) pixels 
            left(120) # on s'oriente de 120° vers la gauche, on fait donc un triangle avec des angles de 60° (triangle équilatéral)
    # Partie récursive
    # On va pouvoir ainsi faire nos différents triangles de façon plus rapide et automatique
    else : # si n!=0 alors on rentre dans la partie récursive
        begin_fill() # on applique la couleur définie plus haut (jaune)
        sierpinski(n-1,L/2) # de façon récursive, on réexecute la fonction en soustrayant 1 à n et en divisant la longueur par 2 
        end_fill() # on finit d'appliquer la couleur
        forward(L/2) # on avance de (L/2) pixels
        begin_fill() 
        sierpinski(n-1,L/2)
        end_fill()
        backward(L/2) # on recule de (L/2) pixels
        left(60) # on tourne à gauche de 60 °
        forward(L/2)
        right(60) # on tourne à droite de 60 °
        begin_fill()
        sierpinski(n-1,L/2)
        end_fill()
        right(120)
        forward(L/2)
        left(120)

print(sierpinski(int(input('Quelle niveau (1,2,3,...) ? ')),int(input('Quelle longueur pour les côtés ? '))))
