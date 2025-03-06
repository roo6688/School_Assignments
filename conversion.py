# conversion.py
# Description: Déterminer si un nombre saisi est dans une base valide (2, 10 ou 16) et le convertir dans les deux autres bases. 
#              Afficher le nombre dans toutes les bases.
# Auteurs: Ronald Sim et Pauline Hughes
# Date: 17 octobre 2024
# Version: 3.0

from math import pow
import sys

nombre = (input("Saisir le nombre:"))

liste_binaire = ['0','1']
liste_decimal = ['0','1','2','3','4','5','6','7','8','9']
liste_hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

##VALIDATION BINAIRE
nombre_binaire = True
i=0
while i < len(nombre):
    if nombre[i] not in liste_binaire:
        nombre_binaire = False
    i+=1

##VALIDATION DECIMALE
nombre_decimal = True
i=0
while i < len(nombre):
    if nombre[i] not in liste_decimal:
        nombre_decimal = False
    i+=1

##VALIDATION HEXA
nombre_hexa = True
i=0
while i < len(nombre):
    if nombre[i] not in liste_hexa:
        nombre_hexa = False
    i+=1

##NOMBRE INVALIDE
if nombre_binaire == False and nombre_decimal == False and nombre_hexa == False or nombre == "":
    sys.exit("Le nombre saisie > {} < n'est pas valide.".format(nombre))

##CONVERSION D'UN NOMBRE BINAIRE
if nombre_binaire == True:

    #Conversion Binaire - Decimal
    bi_deci = 0
    puissance = (len(nombre)) - 1 

    for chiffre in nombre:
        bi_deci = bi_deci + (int(chiffre) * pow(2,puissance))
        puissance = puissance - 1

    #Conversion Binaire - Hexadecimal
    nombre_inv = "" #inversion du nombre
    position = len(nombre)-1
    while position >= 0:
        nombre_inv += nombre[position]
        position -= 1

    while len(nombre_inv)%4 != 0: #Ajout de "0" pour completer le nombre (nombre de chiffre : multiple de 4)
        nombre_inv += '0'

    binaire_complet = "" #inversion du nombre inverse pour obtenir le nombre complete dans le bon ordre
    position = len(nombre_inv)-1
    while position >= 0:
        binaire_complet += nombre_inv[position]
        position -= 1

    binaire_hexa=""
    i = 0
    while i < len(binaire_complet): #parcourir tout les chiffres
        groupe = ""                 #creation d'une chaine pour regroupement des 4 chiffres
        j = 0                       #compteur pour regroupement des 4 chiffres
        while j < 4:                #parcourir 4 chiffres et les ajouter dans groupe
            groupe += binaire_complet[i]
            j+=1
            i+=1
        if groupe == "0000":      #conversion de binaire a hexadecimal
            groupe = "0"
        elif groupe =="0001":
            groupe = "1"
        elif groupe =="0010":
            groupe = "2"
        elif groupe =="0011":
            groupe = "3"
        elif groupe =="0100":
            groupe = "4"
        elif groupe =="0101":
            groupe = "5"
        elif groupe =="0110":
            groupe = "6"
        elif groupe =="0111":
            groupe = "7"
        elif groupe =="1000":
            groupe = "8"
        elif groupe =="1001":
            groupe = "9"
        elif groupe =="1010":
            groupe = "A"
        elif groupe =="1011":
            groupe = "B"
        elif groupe =="1100":
            groupe = "C"
        elif groupe =="1101":
            groupe = "D"
        elif groupe =="1110":
            groupe = "E"
        elif groupe =="1111":
            groupe = "F"
        binaire_hexa += groupe  

    print("{} (2) -> {} (10) -> {} (16)".format(nombre, int(bi_deci), binaire_hexa))
   
##CONVERSION D'UN NOMBRE DECIMAL
if nombre_decimal == True:
    
    #Conversion Decimal - Hexadecimal
    nombre_hexa_inv = ""  #Initialiser le nombre hexadecimal inversé
    dividende = int(nombre)

    if dividende == 0:
        nombre_hexa_inv = "0"

    while dividende != 0:   #Créer une chaîne de caractères composé des résultats de divisions modulo successive par 16
        reste = str(dividende%16)
        if reste == '10':   #Conversion des restes 10-16 en lettres A-F
            reste = 'A'
        elif reste == '11':
            reste = 'B'
        elif reste == '12':
            reste = 'C'
        elif reste == '13':
            reste = 'D'
        elif reste == '14':
            reste = 'E'
        elif reste == '15':
            reste = 'F'
        nombre_hexa_inv += reste 
        dividende = dividende//16

    deci_hexa = ""                         #Inverser "nombre_hexa_inv" pour obtenir le nombre hexadécimal
    position_inv = len(nombre_hexa_inv)-1  #Commencer index de la chaîne avec la dernière position
    while position_inv >= 0:               #Parcourir la chaîne de la dernière position jusqu'à position 0
        deci_hexa += nombre_hexa_inv[position_inv]
        position_inv -= 1

    #Conversion decimal - binaire
    deci_bi_inv = "" #Initialiser le nombre binaire inversé
    dividende = int(nombre)

    if dividende == 0:
        deci_bi_inv  = "0"

    while dividende!=0: #Créer une chaîne de caractères composé des résultats de divisions modulo successive par 2
        reste = str(dividende%2)
        deci_bi_inv += reste
        dividende = dividende//2

    deci_bi= "" #inversion du nombre "deci_bi_inv"
    position_inv = len(deci_bi_inv)-1
    while position_inv >= 0:
        deci_bi += deci_bi_inv[position_inv]
        position_inv -= 1

    print("{} (10) -> {} (16) -> {} (2)".format(int(nombre), deci_hexa, deci_bi))

##CONVERSION D'UN NOMBRE HEXADECIMAL
if nombre_hexa == True:

    #Conversion hexadecimal - binaire
    hexa_bi = ""

    for i in nombre:
        if i == "0":
            hexa_bi += "0000"
        elif i == "1":
            hexa_bi += "0001"
        elif i == "2":
            hexa_bi += "0010"  
        elif i == "3":
            hexa_bi += "0011"
        elif i == "4":
            hexa_bi += "0100"
        elif i == "5":
            hexa_bi += "0101"
        elif i == "6":
            hexa_bi += "0110"  
        elif i == "7":
            hexa_bi += "0111"
        elif i == "8":
            hexa_bi += "1000"
        elif i == "9":
            hexa_bi += "1001"  
        elif i == "A" or i == "a":
            hexa_bi += "1010"
        elif i == "B" or i == "b":
            hexa_bi += "1011"
        elif i == "C" or i == "c":
            hexa_bi += "1100"
        elif i == "D" or i == "d":
            hexa_bi += "1101"
        elif i == "E" or i == "e":
            hexa_bi += "1110"
        elif i == "F" or i == "f":
            hexa_bi += "1111"

    #Conversion hexadecimal - decimal
    hexa_deci = 0
    puissance = (len(nombre)) - 1
    for chiffre in nombre:
        if chiffre == 'A' or chiffre == "a": 
            chiffre = '10'
        elif chiffre == 'B' or chiffre == "b":
            chiffre = '11'
        elif chiffre == 'C' or chiffre == "c":
            chiffre = '12'
        elif chiffre == 'D' or chiffre == "d":
            chiffre = '13'
        elif chiffre == 'E' or chiffre == "e":
            chiffre = '14'
        elif chiffre == 'F' or chiffre == "f":
            chiffre = '15'
        hexa_deci = hexa_deci + (int(chiffre) * pow(16,puissance))
        puissance = puissance - 1

    print("{} (16) -> {} (2) -> {} (10)".format(nombre, hexa_bi, int(hexa_deci)))

print("Fin normale du script conversion.py !") 