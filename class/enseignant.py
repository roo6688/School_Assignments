from personne import Personne
class Enseignant(Personne):
    
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)

    def __str__(self):
        return super().__str__()
    

if __name__ == "__main__":

    p = Enseignant("a","b")
    print(p)