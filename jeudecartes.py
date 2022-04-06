# coding : utf-8

from carte import * # Importation du module Carte 
import random # Importation du module random

class JeuDeCartes :
    """
    Class représentant un jeu de cartes et qui a pour attributs :
    
    -son nombre de cartes
    -son paquet de cartes (défini par la méthode '__CreerPaquet()')
    """
    def __init__(self,nb : int):
        """
        Ici, c'est le constructeur de la class 'JeuDeCartes', self correspond à l'objet en "fabrication"...

        param nb : int

        CU (conditions d'utilisation) : nb est égal à 32 ou à 54 cartes
        
        """
        assert nb == 32 or nb == 54, "nb est égal à 32 ou à 54 !"
        self.__NbCartes = nb
        self.__PaquetdeCartes = self.__CreerPaquet()
        
    def __CreerPaquet(self):
        """
        Méthode qui permet la conception d'un paquet de cartes selon le choix de l'utilisateur, c'est à dire : 32 ou 54 cartes
        """
        couleurs_possibles = ["Trèfle", "Coeur", "Carreau", "Pique"] # 4 couleurs possibles dans un jeu de carte standard
        paquet = [] # on définit une liste vide
        if self.GetNbCartes() == 32 : # Si c'est un jeu de 32 cartes (valeurs de cartes possibles : 7 à 14(as)) :
            for valeur in range(7,15):
                for color in couleurs_possibles :
                       carte = Carte(valeur,color) # On créé une carte avec la classe Carte
                       paquet.append(carte) # On ajoute la carte au paquet
            return paquet
        else : # Sinon, c'est un jeu de 54 cartes (valeurs de cartes possibles : 2 à 14(as)) :
            for valeur in range(2,15):
                for color in couleurs_possibles :
                       carte = Carte(valeur,color)
                       paquet.append(carte)
            return paquet
        
    def GetNbCartes(self):
        """
        Méthode qui renvoie le nombre de cartes d'un paquet de cartes

        return : int
        """
        return self.__NbCartes
    
    def GetPaquet(self):
        """
        Méthode qui renvoie le paquet de cartes

        return : list
        """
        return self.__PaquetdeCartes
    
    def MelangerPaquet(self):
        """
        Méthode qui renvoie le paquet de cartes mélangé

        return : list
        """
        random.shuffle(self.GetPaquet())
        return self.GetPaquet()
        
# Quelques tests (sous forme de fonctions à appeller --> plus net dans l'affichage)

def cartes_paquet():
  mon_jeu = JeuDeCartes(32)
  lepaquet = mon_jeu.GetPaquet()
  for i in range(len(lepaquet)):
      print(lepaquet[i].GetValeur(),lepaquet[i].GetCouleur(), lepaquet[i].GetFigure())

def cartes_paquet_melange():
  mon_jeu.MelangerPaquet()
  for i in range(len(lepaquet)):
      print(lepaquet[i].GetValeur(),lepaquet[i].GetCouleur(), lepaquet[i].GetFigure())




