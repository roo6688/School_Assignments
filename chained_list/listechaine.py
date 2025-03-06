from noeud import Noeud

class ListeChaine:

    def __init__(self):
        self.__tete = None
        self.__taille = 0

    @property
    def taille(self):
        return self.__taille
    @taille.setter
    def taille(self, valeur):
        self.__taille = valeur
    @property
    def tete(self):
        return self.__tete
    
    @tete.setter
    def tete(self, valeur):
        self.__tete = valeur
    

    #POSITION COMMENCE A 1
    def ajouter(self, valeur, pos):
        newNoeud = Noeud(valeur)

        if pos ==1: #Si position == 1 (debut)
            newNoeud.suivant = self.__tete
            self.__tete = newNoeud
        
        else:
            tmp = self.__tete

            for i in range(1, pos-1):
                tmp = tmp.suivant
            newNoeud.suivant = tmp.suivant
            tmp.suivant = newNoeud
        self.__taille += 1


    def supprimer(self, pos):
        if 1 <= pos <= self.__taille+1: #Si position == 1 (debut)
            self.__tete = self.__tete.suivant

        else:
            tmp = self.__tete
            for i in range(1, pos-1):
                tmp = tmp.suivant
            tmp.suivant = tmp.suivant.suivant
        self.__taille -= 1


    def lire(self, pos):
        if 1<= pos <= self.__taille+1:
            tmp = self.__tete
            for i in range(1, pos):
                tmp = tmp.suivant
            return tmp.valeur
        return None
    
    def rechercher(self, valeur):
        for pos in range(1, self.__taille+1):
            if self.lire(pos) == valeur:
                return pos
        return None
    

    def __getitem__(self, pos):
        return self.lire(pos)
    
    def __str__(self):
        ''' Affichage de la liste dans le format [1,2,3,4,5] '''
        chaine = "["
        tmp = self.__tete
        if tmp is None:
            return ""
        while tmp != None:
            chaine += str(tmp)
            tmp = tmp.suivant
            if tmp != None:
                chaine += ","
        chaine += "]"
        return chaine

class ListeChaineBonifie(ListeChaine):
    def __init__(self):
        super().__init__()

    #Not efficient 
    #Use trierV2
    def trier(self):
        for i in range(1, self.taille):
            positionMin = i
            for j in range(i+1, self.taille+1):
                if self.lire(j) < self.lire(i):
                    positionMin = j
                    self.echange(i,positionMin)
                    
    
    def echange(self, pos1, pos2):
        if pos1>pos2:
            pos1,pos2 = pos2, pos1

        prev1, prev2 = None, None
        noeud1, noeud2 = self.tete, self.tete

        for i in range(1,pos1):
            prev1 = noeud1
            noeud1 = noeud1.suivant
        for i in range(1,pos2):
            prev2 = noeud2
            noeud2 = noeud2.suivant
        
        if noeud1.suivant == noeud2:
            noeud1.suivant = noeud2.suivant
            noeud2.suivant = noeud1
            if prev1:
                prev1.suivant = noeud2
            else:
                self.tete = noeud2
            return
        
        if prev1:
            prev1.suivant = noeud2
        else:
            self.tete = noeud2

        if prev2:
            prev2.suivant = noeud1
        else:
            self.tete = noeud1
        
        #noeud1.suivant, noeud2.suivant = noeud2.suivant, noeud1.suivant
        
        tmp = noeud2.suivant
        noeud2.suivant = noeud1.suivant
        noeud1.suivant = tmp

        

    def convertionListe(self, list, name):
        name = ListeChaine()
        position = 1
        for i in list:
            name.ajouter(i, position)
            position+=1
        return name
    
    def trierV2(self):
        current = self.tete
        while current:
            noeudMin = current
            noeudSuivant = current.suivant
            while noeudSuivant:
                if noeudSuivant.valeur < noeudMin.valeur:
                    noeudMin = noeudSuivant
                noeudSuivant = noeudSuivant.suivant
            if noeudMin != current:
                noeudMin.valeur, current.valeur = current.valeur, noeudMin.valeur
            current = current.suivant
            
def main():
    maListe = ListeChaineBonifie()
    number = [5,2,8,7,1,7,7,8,10,7]
    i=0
    for pos in range(1,11):
        maListe.ajouter(number[i],pos)
        i+=1
    print(maListe)
    maListe.trierV2()
    print(maListe)
if __name__ == "__main__":
    main()