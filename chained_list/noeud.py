class Noeud:

    def __init__(self, valeur, noeud = None):
        self.__valeur = valeur 
        self.__suivant = noeud

    @property
    def valeur(self):
        return self.__valeur
    
    @valeur.setter
    def valeur(self, contenu):
        self.__valeur = contenu

    
    @property
    def suivant(self):
        return self.__suivant
    
    @suivant.setter
    def suivant(self, noeud):
        self.__suivant = noeud


    def __str__(self):
        return str(self.__valeur)
