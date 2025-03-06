from etudiant import Etudiant
from enseignant import Enseignant

class Cours:
    def __init__(self):
        self.__listeEtudiants = []
        self.__titre = None
        self.__enseignant = None

    def ajouterEtudiant(self, etudiant):
        self.__listeEtudiants.append(etudiant)

    @property
    def listeEtudiants(self):
        return self.__listeEtudiants
    @property
    def titre(self):
        return self.__titre
    
    @titre.setter
    def titre(self, nouveauTitre):
        self.__titre = nouveauTitre

    @property
    def enseignant(self):
        return self.__enseignant
    
    @enseignant.setter
    def enseignant(self, nouveauEnseignant):
        self.__enseignant = nouveauEnseignant

    def __str__(self):
        #etudiant = "\n".join([f" - {etudiant}" for etudiant in self.listeEtudiants])
        liste = []
        for i in self.listeEtudiants:
            if i is not None:
                liste.append(f" - {i}")
        chaine = "\n".join(liste)
        return f"{self.titre}\nEnseignant: {self.enseignant}\nEtudiants : \n{chaine}"
        

def main():
    cours = Cours()
    cours.titre = "INF8414 - Programmation avancée"
    cours.enseignant = Enseignant("Alix","Boc")
    cours.ajouterEtudiant(Etudiant("Paul","Michel","PAUM112345678"))
    cours.ajouterEtudiant(Etudiant("Smith","John","SMIJ02102044"))
    print(cours)

if __name__ == "__main__":
    main()
    