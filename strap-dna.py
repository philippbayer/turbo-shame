import os, sys
from string import *


def get_file():
	os.system('find *.fasta > fastaliste.txt')
	os.system('mkdir dna')
	os.system('mkdir ./dna/problems')

def main():
	input = open('fastaliste.txt', 'r') 		# Opening input-file
	
	for line in input:
		line = line.rstrip()
		f = open(line, 'r')
		datei = f.readlines()			# Reading all lines into a list
		laenge = len(datei)			# Getting number of lines
		i = 0
		output=open('./dna/'+line,'w')
		sub(datei,laenge,i,output,line)
		output.close()	
		codon(line)		
		failsafe(line)
		
def sub(datei,laenge,i,output,line):	
	while i != laenge:
		zeile = datei[i]			# Getting line
		if zeile == ">gag\n":			# Checking for relevant gene #1
			output.write(zeile)		# Write gene-name into output file
			j = i+1
			
			while datei[j] != "\n":		# Write sequence starting next line into output file
				zeile = datei[j]	# as long as the line is NOT empty
				output.write(zeile)
				j += 1	
				

		elif zeile == ">pol\n":
			output.write(zeile)
			k = i+1

			while datei[k] != "\n":		# Write sequence starting next line into output file
				zeile = datei[k]	# as long as the line is NOT empty
				output.write(zeile)
				k += 1	

		
		elif zeile == ">env\n":	
			output.write(zeile)
			l = i + 1

			while datei[l] != "\n":		# Write sequence starting next line into output file
				zeile = datei[l]	# as long as the line is NOT empty
				output.write(zeile)
				l += 1	
			
		i += 1


def failsafe(line):
	counter=0
	search = open('./dna/'+line,'r')
	suche = search.readlines()
	suche2 = "".join(suche)
	if suche2.count(">gag") == 1:			
		counter += 1
	if suche2.count(">pol") == 1:
		counter += 1
	if suche2.count(">env") == 1:
		counter += 1
	if counter != 3 :
		os.system('mv ./dna/'+line+' ./dna/problems/'+line)
	search.close()		

def codon(line):
	codonsearch = open('./dna/'+line, 'r')
	codons = codonsearch.readlines()
	codons = "".join(codons)

	finder = codons.find('>pol')				# Looking for stopcodons in >gag and delete it
	if codons[finder-4:finder-1] == 'tag':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'ta\ng':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\nag':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2
	elif codons[finder-4:finder-1] == 'taa':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'ta\na':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\naa':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-4:finder-1] == 'tga':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'tg\na':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\nga':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2


	finder = codons.find('>env')				# Looking for stopcodons in >pol and delete it
	if codons[finder-4:finder-1] == 'tag':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'ta\ng':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\nag':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2
	elif codons[finder-4:finder-1] == 'taa':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'ta\na':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\naa':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-4:finder-1] == 'tga':
		codons1 = codons[:finder-3]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 'tg\na':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2	
	elif codons[finder-5:finder-1] == 't\nga':
		codons1 = codons[:finder-5]
		codons2 = codons[finder:]
		codons = codons1 + '\n' + codons2


	if codons[-4:] == 'tag\n':				# Looking for stopcodons in >env and delete it
		codons = codons[:-4]
	elif codons[-5:] == 'ta\ng\n':
		codons = codons[:-5]
	elif codons[-5:] == 't\nag\n':
		codons = codons[:-5] 

	elif codons[-4:] == 'taa\n':
		codons = codons[:-4]
	elif codons[-5:] == 'ta\na\n':
		codons = codons[:-5]
	elif codons[-5:] == 't\naa\n':
		codons = codons[:-5]

	elif codons[-4:] == 'tga\n':
		codons = codons[:-4]
	elif codons[-5:] == 'tg\na\n':
		codons = codons[:-5]
	elif codons[-5:] == 't\nga\n':
		codons = codons[:-5]

	codonsearch.close()
	codonsearch = open('./dna/'+line,'w')
	codonsearch.write(codons)
	codonsearch.close()
	
get_file()
main()		
