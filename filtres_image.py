import PIL.Image as Image # Importation du module PIL

class Filtre : # Création de la classe 'Filtre'
    """
    Class représentant une série d'outils et de filtres pour image et qui a comme attributs :

    -son fichier(file)
    -l'ouverture de ce fichier, de l'image
    -l'accès aux pixels de l'image 
    """
    def __init__(self, file : str):
        """
        Ici, c'est le constructeur de class, self correspond à l'objet qui est en cours de création
        """
        self.__file = file # .__ permet de mettre l'attribut en privé
        self.__img = Image.open(self.__file)
        self.__pix = self.__img.load()
        
    def size(self): 
        """
        Méthode qui renvoie la taille de l'image
        
        return : tuple
        """
        return self.__img.size
    
    def width(self): 
        """
        Méthode qui renvoie la largeur de l'image
        
        return : int
        """
        return self.__img.size[0] # La largeur de l'image correspond à la première valeur du tuple (indice 0)
    
    def height(self): 
        """
        Métode qui renvoie la hauteur de l'image
        
        return : int
        """
        return self.__img.size[1] # La hauteur de l'image correspond à la deuxième valeur du tuple (indice 1)
    
    def weight(self): 
        """
        Méthode qui renvoie le poids en pixels d'une image'
        
        return : int
        """
        return self.width()*self.height()
    
    def get_pix(self, col : int, row : int):
        """
        Méthode qui renvoie la valeur d'un pixel précis
        
        param col : int
        param row : int
        return : tuple
        """
        assert isinstance(col, int), 'col est un nombre entier !' # Si l'utilisteur ne rentre pas des valeurs entières pour 'col', alors un message d'erreur apparaît
        assert isinstance(row, int), 'row est un nombre entier !' # Idem pour 'row'
        if 0 <= col <= self.width() and 0 <= row <= self.height():
            return self.__pix[col, row]
        else :
            return None
        
    """
    ---------------------------------------------------------------------------------------------------------------------------------------------
    Petite explication concernant le traitement d'un pixel :
    Pour pouvoir parcourir chaque pixel de l'image, on a recourt à deux boucles imbriquées.
    La première parcourt l'axe x(la largeur) et la deuxième parcourt l'axe y(la hauteur), ainsi, le pixel de coordonnées (x,y) peut être traité...
    ----------------------------------------------------------------------------------------------------------------------------------------------
    """
  
    def reverse(self, file: str):
        """
        Méthode qui renvoie l'image avec un filtre négatif et qui la sauvegarde sous 'file'
        
        param file : str
        return : None
        """
        for x in range(self.width()): 
            for y in range(self.height()):
                self.__pix[x,y] = ((255-self.get_pix(x,y)[0]),(255-self.get_pix(x,y)[1]), (255-self.get_pix(x,y)[2])) # Une image négative est obtenue en soustrayant à 255 chaque valeur (rouge, vert ou bleu) du pixel 
        self.__img.save(file)
        
    def red(self, file : str):
        """
        Méthode qui renvoie l'image avec un filtre rouge et qui la sauvegarde sous 'file'
        
        param file : str
        return : None
        """
        for x in range(self.width()):
            for y in range(self.height()):
                self.__pix[x,y] = (self.get_pix(x,y)[0],0,0) # Pour un filtre d'une couleur unique (ici rouge), il suffit de conserver la valeur d'une seule couleur (rouge, vert ou bleu) et attribuer 0 aux deux autres couleurs
        self.__img.save(file)
        
    def color2grey(self, file : str):
        """
        Méthode qui renvoie l'image avec un filtre gris et qui la sauvegarde sosu 'file'
        
        param file : str
        return : None
        """
        for x in range(self.width()):
            for y in range(self.height()):
                self.__pix[x,y] = (self.get_pix(x,y)[0],self.get_pix(x,y)[0], self.get_pix(x,y)[0]) # Le filtre gris s'obtient si les trois valeurs du pixel sont identiques
        self.__img.save(file)
        
    def threshold(self, file : str, limit : int):
        """
        Méthode qui renvoie l'image avec un seuillage défini en fonction d'un seuil 'limit'.
        L'image est sauvegardé sous 'file'
        
        param file : str
        param : limit : int
        return : None
        """
        assert isinstance(limit, int), 'limit est un tuple !'
        for x in range(self.width()):
            for y in range(self.height()):
                if self.get_pix(x,y)[0] < limit : 
                    self.__pix[x,y] = (0,0,0) # Si la valeur du premier canal du pixel est inférieure au seuil, alors le pixel sera noir
                else :
                    self.__pix[x,y] = (255,255,255) # Dans le cas contraire, le pixel sera blanc
        self.__img.save(file) 
        
    def threshold_color(self, file : str, limits : tuple):
        """
        Méthode qui renvoie l'image avec un seuillage spécial pour les images en couleur défini en fonction d'un seuil 'limit'.
        L'image est sauveagrdé sous 'file'
        
        param file : str
        param : limit : int
        return : None
        """
        assert isinstance(limits, tuple), 'limits est un tuple !'
        for x in range(self.width()):
            for y in range(self.height()):
                # Ici, on traite les trois valeurs de chaque canal du pixel en fonction d'un seuil
                if self.get_pix(x,y)[0] < limit[0] : self.__pix[x,y] = (0,self.get_pix(x,y)[1], self.get_pix(x,y)[2])
                else : self.__pix[x,y] = (255,self.get_pix(x,y)[1], self.get_pix(x,y)[2])
                if self.get_pix(x,y)[1] < limit[1] : self.__pix[x,y] = (self.get_pix(x,y)[0],0,self.get_pix(x,y[2]))
                else : self.__pix[x,y] = (self.get_pix(x,y)[0],255,self.get_pix(x,y)[2])
                if self.get_pix(x,y)[2] < limit[2] : self.__pix[x,y] = (self.get_pix(x,u)[0], self.get_pix(x,y)[1],0)
                else : self.__pix[x,y] = (self.get_pix(x,y)[0], self.get_pix(x,y)[1], 255)
        self.__img.save(file)
        
    def brighten(self, file, value : int = 30):
        """
        Méthode qui renvoie l'image avec plus ou moins de luminosité en fonction de 'value'.
        L'image est sauveagrdé sous 'file'
        
        param file : str
        param : value : int = 30 (par défaut)
        return : None
        """
        assert isinstance(value, int), 'value est un nombre entier !'
        for x in range(self.width()):
            for y in range(self.height()):
                # Pour une augmentation de luminosité de +96, la perte d'information est importante et chaque pixel devient blanc
                if value > 96 : 
                    if max(self.__pix[x,y]) > 160 :
                        self.__pix[x,y] = (255,255,255)
                    else :
                        self.__pix[x,y] = (self.get_pix(x,y)[0]+value,self.get_pix(x,y)[1]+value,self.get_pix(x,y)[2]+value)
                # Au contraire, une diminution de la luminosité de -100, entraîne aussi une perte d'information et chaque pixel devient noir
                if value < -100 :
                    if min(self.__pix[x,y]) < 100 :
                        self.__pix[x,y] = (0,0,0)
                    else :
                        self.__pix[x,y] = (self.get_pix(x,y)[0]+value,self.get_pix(x,y)[1]+value,self.get_pix(x,y)[2]+value)
        self.__img.save(file)
        
    def contrast(self, file : str , limit : int = 30):
        """
        Méthode qui renvoie l'image avec plus ou moins de contraste en fonction de 'limit'.
        L'image est sauveagrdé sous 'file'
        
        param file : str
        param : value : int = 30 (par défaut)
        return : None
        """
        assert isinstance(limit, int), 'limit est un nombre entier !'
        for x in range(self.width()):
            for y in range(self.height()):
                # Encore ici, nous travaillons avec les valeurs de chaque canal des pixels
                if self.get_pix(x,y)[0] < 0 + limit : self.__pix[x,y] = (0,self.get_pix(x,y)[1],self.get_pix(x,y)[2])
                elif self.get_pix(x,y)[0] > 255 - limit : self.__pix[x,y] = (255,self.get_pix(x,y)[1],self.get_pix(x,y)[2])
                
                if self.get_pix(x,y)[1] < 0 + limit : self.__pix[x,y] = (self.get_pix(x,y)[0], 0, self.get_pix(x,y)[2])
                elif self.get_pix(x,y)[1] > 255 - limit : self.__pix[x,y] = (self.get_pix(x,y)[0], 255, self.get_pix(x,y)[2])
                
                if self.get_pix(x,y)[2] < 0 + limit : self.__pix[x,y] = (self.get_pix(x,y)[0],self.get_pix(x,y)[1],0)
                elif self.get_pix(x,y)[2] > 255 - limit : self.__pix[x,y] = (self.get_pix(x,y)[0],self.get_pix(x,y)[1],255)
                
                else : self.__pix[x,y] = (int(round((255.0 / 195.0) * (self.get_pix(x,y)[0] -30) + 0.5)),int(round((255.0 / 195.0) * (self.get_pix(x,y)[1] -30) + 0.5)),int(round((255.0 / 195.0) * (self.get_pix(x,y)[2] -30) + 0.5)))
        self.__img.save(file)
    
    def __repr__(self):
        return self
        
        
img = Filtre(str(input('Sur quelle image voulez-vous ajouter un filtre (nom image + extension --> ex : toto.jpg) ? ')))
print('Vous pouvez commencer à ajouter vos filtres sur votre image')




















    


