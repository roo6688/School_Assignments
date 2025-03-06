class Personne:

    def __init__(self, prenom, nom):
        self.__prenom = prenom
        self.__nom = nom
        
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nouveauNom):
        self.__nom = nouveauNom

    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self,nouveauPrenom):
        self.__prenom = nouveauPrenom

    def __str__(self):
        return f"{self.prenom} {self.nom}"





