import sys
import os
from string import *
from Bio.Seq import *
from Bio import Translate
from Bio.Alphabet import IUPAC

def Translate(sequence):
	F1 = sequence
	F2 = sequence[1:]
	F3 = sequence[2:]
	F4 = sequence[::-1]
	F5 = sequence[2::-1]
	F6 = sequence[1::-1]

	F1 = translate(F1)
	F2 = translate(F2)
	F3 = translate(F3)
	F4 = translate(F4)
	F5 = translate(F5)
	F6 = translate(F6)
	result = [F1, F2, F3, F4, F5, F6]
	return result


liste = open("tabelle",'r')				# Opening Input-list
output = open("AUSGABE.txt", 'a')			# Opening Output-list

dnas = open('dna_gag', 'r')				# Opening List with DNA-Sequences
dna = dnas.readlines()					# Read DNA-Lines
dna = "".join(dna)					# Convert List into string

proteins = open('protein_gag', 'r')			# Opening List with Protein-Sequences			
protein = proteins.readlines()				# Reading Lines
protein = "".join(protein)				# Convert List into string

for line in liste:
	line = line.rstrip()				# Remove \n from Input-table
	output.write(line+"\n")				# Write name into output-file

	dnaheader = find(dna, line)			# Find sequence
	dnaanfang = find(dna, "\n", dnaheader)		# Find start of sequence
	dnaende = find(dna, ">", dnaheader)		# Find end of sequence
	dnaseq = dna[dnaanfang+1:dnaende-1]		# Write sequence
	dnaseq = replace(dnaseq,'\n',"")		# Remove whitespaces
	dnalen = len(dnaseq)				# Get length
	dnalist = []

	proteinheader = find(protein, line)		
	proteinanfang = find(protein, "\n", proteinheader)		# Find start of protein-sequence
	proteinende = find(protein, ">", proteinheader)			# Find end of proteinsequence
	proteinseq = protein[proteinanfang+1:proteinende-1]		# Write sequence
	proteinseq = replace(proteinseq,"\n","")			# remove whitespaces
	proteinlen = len(proteinseq)					# Get length

	i = 0

	while i < dnalen:
		dnalist.append(dnaseq[i:i+3])				# Make a list with base-triplets 
		i += 3	
	#a = 0
	#protseq2 = ''
	#while a < proteinlen:						# Search for false Aminoacids (e.g. X,J)
		#if proteinseq[a] == 'X' or 'J':
		 	#dnalist.pop(a)
		#else:
			#protseq2 = protseq2 + proteinseq[a]
		#a += 1
	
	#proteinseq = protseq2						# Because we're lazy.	
	#print proteinseq	
	#dnaseq = "".join(dnalist)
	dnatrans = Translate(dnaseq)

	dnatrans1 = str(dnatrans[0])
	dnatrans2 = str(dnatrans[1])
	dnatrans3 = str(dnatrans[2])
	dnatrans4 = str(dnatrans[3])
	dnatrans5 = str(dnatrans[4])
	dnatrans6 = str(dnatrans[5])

	if find(dnatrans1,proteinseq) != -1 :
		m = find(dnatrans1,proteinseq)
		outfile = ""
		while m != proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")

	if find(dnatrans2,proteinseq) != -1:
		m = find(dnatrans2,proteinseq)
		outfile = ""
		while m < proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")

	if find(dnatrans3,proteinseq) != -1:
		m = find(dnatrans3,proteinseq)
		outfile = ""
		while m < proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")

	if find(dnatrans4,proteinseq) != -1:
		m = find(dnatrans4,proteinseq)
		outfile = ""
		while m < proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")

	if find(dnatrans5,proteinseq) != -1:
		m = find(dnatrans5,proteinseq)
		outfile = ""
		while m < proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")
	
	if find(dnatrans6,proteinseq) != -1:
		m = find(dnatrans6,proteinseq)
		outfile = ""
		while m < proteinlen:
			outfile = outfile + dnalist[m]
			m += 1
		output.write(outfile+"\n")

