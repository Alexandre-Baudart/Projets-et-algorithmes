# coding : utf-8

class Carte : # On definit la class Carte
    """
    Class représentant une carte et qui a pour attributs :
    
    - sa valeur
    - sa couleur
    - sa figure (uniquement si val > 10)
    """
    def __init__(self,val : int ,coul : str):
        """
        Ici, c'est le consteucteur de notre class 'Carte', self représente l'objet en cours de "fabrication"...
        """
        assert isinstance(val,int), "val est un nombre entier"
        assert isinstance(coul,str), "coul est un me chaîne de caractères"
        assert 2 <= val <= 14, "val est compris entre 2 et 14 !"
        
        self.__couleur = coul # .__ permet de mettre en privé un attribut
        self.__valeur = val
        if self.__valeur == 11 :
            self.__figure = 'Valet'
        if self.__valeur == 12 :
            self.__figure = 'Dame'
        if self.__valeur == 13 :
            self.__figure = 'Roi'
        if self.__valeur == 14 :
            self.__figure = 'As'
            
    def GetValeur(self):
        """
        Méthode qui renvoie la valeur d'une carte

        return : int
        """
        return self.__valeur
    
    def GetCouleur(self):
        """
        Méthode qui renvoie la couleur d'une carte

        return : int
        """
        return self.__couleur
    
    def GetFigure(self):
        """
        Méthode qui renvoie la figure d'une carte ou renvoie 'None' si la valeur est strictement
        supérieur à 10

        return : int or None 
        """
        if self.GetValeur() > 10 :
            return self.__figure
        else :
            return None
        
    def __SetFigure(self, val : int):
        """
        Methode qui permet de modifier la figure d'une carte lorsque la valeur que l'on veut ajouter
        à la carte est superieur ou égal à 11
        La méthode est privée pour éviter de pouvoir ajouter des figures trop incohérentes...

        param val : int
        
        CU (conditions d'utilisation) : val est compris entre 2 et 14 au pire (jeu de 54 cartes)
        """
        assert isinstance(val, int), "val est un nombre entier !"
        assert 2 <= val <= 14, "val est compris entre 2 et 14 !"
        
        if val == 11 :
            self.__figure = 'Valet'
        elif val == 12 :
            self.__figure = 'Dame'
        elif val == 13 :
            self.__figure = 'Roi'
        elif val == 14 :
            self.__figure = 'As'
            
    def SetValeur(self, val : int):
        """
        Methode qui permet de modifier la valeur d'une carte
        Lorsque la valeur a bien éte modifiée, 'True' est revoyé, sinon False
        De plus, si c'est val est une valeur comprise entre 11 et 14 alors la mêthode fait appel
        à la méthode __SetFigure pour regler le problème de la nouvelle figure...

        param val : int

        CU (conditions d'utilisation) : val est compris entre 2 et 14 au pire (jeu de 54 cartes)
        """
        assert isinstance(val, int), "val est un nombre entier !"
        assert 2 <= val <= 14, "val est compris entre 2 et 14"
        
        self.__valeur = val
        if self.GetValeur() == val and 2 <= val <= 10 : 
            return True # Si la valeur de la carte actuelle est égale a la nouvelle (donc modifiée) et que val est compris entre 2 et 10 alors 'True' est renvoyé
        if self.GetValeur() == val and 11 <= val <= 14 :
            self.__SetFigure(val) # Idem que précédemment toitefois si val est compris entre 11 et 14 alors la figure est changée et 'True' est renvoyé
            return True
        else :
            return False # Sinon 'False' est retourné
        
    def SetCouleur(self, coul : str):
        """
        Méthode qui modifie la couleur d'une carte
        Ici aussi, 'True' est renvoyé si la couleur est bien changée, sinon False

        param coul : str
        """
        assert isinstance (coul, str), "coul est une chaine de caractères !"
        
        self.__couleur = coul
        if self.GetCouleur() == coul :
            return True
        else :
            return False

# Quelques tests (sous forme de fonctions --> plus net dans l'affichage, + 2 asserts)

def test_class():
  ma_carte = Carte(11, 'Trèfle')
  print(ma_carte)
  print(ma_carte.__doc__)
  print(ma_carte.__init__.__doc__)

def modif_carte():
  ma_carte = Carte(11, 'Trèfle')
  print(ma_carte.GetFigure())
  if ma_carte.SetValeur(13):
      print(ma_carte.GetFigure())

ma_carte = Carte(8, "Pique")
if __name__ == '__main__' :
    assert ma_carte.GetCouleur() == 'Pique'
    assert ma_carte.GetValeur() == 8
    assert ma_carte.GetFigure() == None






