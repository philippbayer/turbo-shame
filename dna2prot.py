from string import *
from BioSeq import Translate
import sys, os

def Main()
	input = open('dna_gag','r')
	output = open('dna_gag_bereinigt','a')
	input2 = open('protein_gag','r')
	output2 = open('protein_gag_bereinigt','a')
	dnaseq = input.readlines()
	protseq = input2.readlines()
	dnalen = len(dnaseq)
	protlen = len(protseq)
	dnalist = []
	potlist = []
	while i < dnalen:				# Make me a DNA-Codon-List 
		dnalist.append(dnaseq[i:i+3])
		i += 3
		print dnalist
	while j < protlen
		protlist.append(protseq[j:j+1]		# make me a Protein-List
		j += 1
		print protlist
		
