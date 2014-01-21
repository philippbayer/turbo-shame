import os, sys
from string import *


def get_file():
	os.system('find *.fasta > fastaliste.txt')
	os.system('mkdir cleaned')

def main():
	liste = open('fastaliste.txt', 'r') 		# Opening input-file
	
	for line in liste:
		line = line.rstrip()
		f = open(line, 'r')
		datei = f.readlines()			# Reading all lines of one seq-file into a list
		output=open('./cleaned/env_aa.fasta','a')
		sub(datei,output,line)
		output.close()	

def sub(datei,output,line):	
replace('.fasta','')

get_file()
main()		
