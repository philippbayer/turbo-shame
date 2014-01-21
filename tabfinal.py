from string import *
import os,sys

def Main():
	input = open('gag_nt_cleaned.fasta','r')
	output = open('gag_nt_tabellefinal.txt','a')
	dna = input.readlines()
	dna = ''.join(dna)
	nameend = 0
	namestart = 0

	for line in dna:
		if line.find('>') != -1:
			namestart = dna.find('>',nameend)
			nameend = dna.find('\n',namestart)
			output.write(dna[namestart:nameend]+'\n')
			print dna[namestart:nameend]
	
Main()		
