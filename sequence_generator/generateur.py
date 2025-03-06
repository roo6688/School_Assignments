"""
= generateur.py
= Ce programme contient les fonctions de geneteur-sequences.py qui permet de generer un jeu de sequences
= Auteurs : Ronald Sim et Pauline Hughes
= Date : 17 decembre 2024
= Version : 3.0
"""

import os 
import sys 
from random import randint


def initialisation():  
    # Initialiser les entrees par defaut
    
    outputfile = "output.txt" 
    tailleSequences = 10 
    nbSequences = 5
    formatOutput = "fasta"
    nomEspece = "espece"
    
    return (outputfile, tailleSequences, nbSequences, formatOutput, nomEspece)


def extraireArgument(argument):

    separation = argument.split("=") #-formatSortie=phylip -> retourne -formatSortie, phylip
    
    if len(separation) == 2:
        key, value = separation
    else: # S'il y a 0 ou plusieurs "=" par argument -> quitter le programme                         
        quitterProgramme("La valeur saisie pour {} n'est pas valide. Veuillez utiliser un '=' par argument".format(separation[0]))

    return(key, value) 


def valideOutputFile(nomFichier):

    if os.path.exists(nomFichier): # Si le nom de fichier existe deja -> quitter le programme
        return quitterProgramme("Le fichier >{}< existe deja. Veuillez choisir un autre nom.".format(nomFichier))
    elif nomFichier == "": # Si la valeur saisi pour -fichierSortie est "" -> quitter le programme
        quitterProgramme("Aucune valeur n'a ete saisie pour -fichierSortie.")
    else:
        return(nomFichier)
    

def valideEntierPositif(nombre):

    try: # Si la valeur saisi pour -tailleSequences ou -nbSequences n'est pas un entier -> quitter le programme
        nombre = int(nombre) 
    except ValueError:
        return quitterProgramme("La valeur >{}< n'est pas un nombre entier.".format(nombre))

    if nombre >= 0: # Si la valeur saisi pour -tailleSequences ou -nbSequences n'est pas un entier positif -> quitter le programme
        return nombre
    else:
        return quitterProgramme("La valeur >{}< n'est pas un entier positif.".format(nombre))


def valideFormatOutfile(formatFichier):

    format_valide = ["fasta", "phylip"]
    if formatFichier not in format_valide: # Si le format de fichier n'est pas fasta ou phylip -> quitter le programme
        quitterProgramme("Le format >{}< n'est pas valide.".format(formatFichier))
    else:
        return formatFichier 


def valideNomEspece(nomEspece):  

    if nomEspece == "": # Si la valeur saisi pour -nomExpece est "" -> quitter le programme
        quitterProgramme("Aucune valeur n'a ete saisie pour -nomEspece.")
    else:
        return nomEspece
    

def help():

    print("Veuillez preciser les options ci-dessous pour generer un jeu de sequences aleatoire d'ADN.\n\n\
Options : \n\
    fichierSortie= : le nom du fichier de sortie. Ce nom ne peut pas deja existe. Si pas fournit, nom defaut = output.txt\n\
    formatSortie= : le format du ficher de sortie, soit fasta ou phylip. Si pas fournit, format defaut = fasta\n\
    tailleSequence= : la taille des sequences. Si pas fournit, taille defaut = 10\n\
    nbSequence= : le nombre de sequence a generer. Si pas fournit, nombre defaut = 5\n\
    nomEspece= : le nom de l'espece. Si pas fournit, nom defaut = espece\n")


def quitterProgramme(message):
    sys.exit(message)

def genererJeuSequences(taille, nbSequence):
    base= ["A","T","C","G"]
    sequences = []
    for i in range(nbSequence):
        sequence = ""
        for i in range(taille):
            sequence += base[randint(0,3)]  #Faire 1 sequence
        sequences.append(sequence)          #ajout de la sequence nouvellement genere a la liste "sequences"
    return sequences


def presentation():
    print(\
"=====================================================\n\
= generateur-sequences.py\n\
= Ce programme permet de generer un jeu de sequences\n\
= Auteurs : Ronald Sim et Pauline Hughes\n\
= Date    : 17 decembre 2024\n\
= Version : 3.0\n\
=====================================================\n")


def sauvegarderSequences(sequences, nomFichier, formatFichier, nomEspece):

    with open(nomFichier, "w") as fh:   
        if formatFichier == "fasta":
            fh.write(">cat {}\n".format(nomFichier))
            for i, sequence in enumerate(sequences, 1):
                fh.write("> {}{}\n {}\n".format(nomEspece, i, sequence))
        if formatFichier == "phylip":
            fh.write(">cat {}\n{}  {}\n".format(nomFichier, len(sequences), len(sequences[0])))
            for i, sequence in enumerate(sequences, 1):
                fh.write("{}{}  {}\n".format(nomEspece, i, sequence))




