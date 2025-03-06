from listechaine import ListeChaine
class File:
    def __init__(self):
        self.__liste = ListeChaine()

    def enfiler(self, entier):
        self.__liste.ajouter(entier, self.__liste.taille+1)

    def defiler(self):
        self.__liste.tete = self.__liste.tete.suivant 

    def __str__(self):
        return str(self.__liste)
        
    
if __name__ == "__main__":
    import random
    maFile = File()
    print("On enfile : ")
    for pos in range (1,11):
        val = random.randint(0,10)
        maFile.enfiler(val)
        print ( maFile )
    print("On defile : ")
    for pos in range (1,11):
        maFile.defiler()
        print ( maFile )