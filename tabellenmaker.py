import os, sys
from string import *


def get_file():
	os.system('find *.fasta > fastaliste.txt')
	os.system('mkdir done')

def main():
	liste = open('fastaliste.txt', 'r') 		# Opening input-file
	for line in liste:
		string1="".join(line)
		string1 = string1.replace('.fasta\n', '\n')	
		output=open('./done/tab1.txt','a')
		output.write(string1)	
		output.close()	

get_file()	
main()	

