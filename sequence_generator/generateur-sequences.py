from random import randint
import sys
import generateur as seqGen

def main(arguments):    
    (outputfile,tailleSequences,nbSequences,formatOutput,nomEspece) = seqGen.initialisation()
    for argument in arguments:
        (key,value) = seqGen.extraireArgument(argument)
        if key == "-fichierSortie":
            outputfile = seqGen.valideOutputFile(value)
        elif key == "-tailleSequences":
            tailleSequences = seqGen.valideEntierPositif(value)
        elif key == "-nbSequences":
            nbSequences = seqGen.valideEntierPositif(value)
        elif key == "-formatSortie":
            formatOutput = seqGen.valideFormatOutfile(value)
        elif key == "-nomEspece":
            nomEspece = seqGen.valideNomEspece(value)
        elif key == "-help":
            seqGen.help()
        else: 
            seqGen.help()
            seqGen.quitterProgramme("Option inconnue : " + key)
    seqGen.sauvegarderSequences(seqGen.genererJeuSequences(tailleSequences,nbSequences),outputfile,formatOutput,nomEspece)


if __name__ == "__main__":
    seqGen.presentation()
    main(sys.argv[1:])
    print("Fin normale du programme, au revoir...\n")