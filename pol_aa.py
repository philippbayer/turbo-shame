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
		output=open('./done/pol_aa.fasta','a')
		sub(datei,output,line)
		output.close()	

def sub(datei,output,line):	
	output.write(">"+line)
	seq = "".join(datei)
	counter1 = seq.find(">pol")
	counter1 = counter1+4
	counter2 = seq.find(">env")
	output.write(seq[counter1:counter2-1]+"\n")

get_file()
main()		
