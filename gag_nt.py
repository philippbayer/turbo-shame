import os, sys
from string import *


def get_file():
	os.system('find *.fasta > fastaliste.txt')
	os.system('mkdir done')

def main():
	liste = open('fastaliste.txt', 'r') 		# Opening input-file
	
	for line in liste:
		line = line.rstrip()
		f = open(line, 'r')
		datei = f.readlines()			# Reading all lines of one seq-file into a list
		output=open('./done/gag_nt.fasta','a')
		sub(datei,output,line)
		output.close()	

def sub(datei,output,line):	
	output.write(">"+line)
	seq = "".join(datei)
	counter = seq.find(">pol")
	counter = counter-1
	output.write(seq[4:counter]+"\n")

get_file()
main()		
