from personne import Personne
class Etudiant(Personne):

    def __init__(self, prenom, nom, codePerm):
        super().__init__(prenom, nom)
        self.__codePerm = codePerm
    
    @property
    def codePerm(self):
        return self.__codePerm
    
    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.codePerm}"

if __name__ == "__main__":

    p = Etudiant("a","b","asdfasd")
    print(p)