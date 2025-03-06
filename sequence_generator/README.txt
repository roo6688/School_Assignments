In this folder, you will find two scripts: generateur.py and generateur-sequences.

generateur.py contains functions used by generateur-sequences to generate a random DNA sequence 
in fasta or phylip format.

generateur-sequences.py is a script written by my professor that imports functions from
generateur.py and generates a DNA sequence.

How to generate random DNA sequences:
In the terminal, type "python generateur.sequences" and add the following:

	-fichierSortie= : Name of output file 			(defaut = output.txt)
	-formatSortie= : output file format (fasta or phylip) 	(default = fasta)
	-tailleSequence= : Number of nucleotides 		(default = 10)
	-nbSequence= : Number of sequences 			(default = 5)
	-nomEspece= : Name of species 				(default = espece)
	
Use help() for instructions.