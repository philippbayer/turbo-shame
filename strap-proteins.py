import os, sys
from string import *


def get_file():
	os.system('find *.fasta > fastaliste.txt')
	os.system('mkdir proteins')
	os.system('mkdir ./proteins/problems')

def main():
	input = open('fastaliste.txt', 'r') 		# Opening input-file
	
	for line in input:
		line = line.rstrip()
		f = open(line, 'r')
		datei = f.readlines()			# Reading all lines into a list
		laenge = len(datei)			# Getting number of lines
		i = 0
		output=open('./proteins/'+line,'w')
		sub(datei,laenge,i,output,line)
		output.close()	
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
	search = open('./proteins/'+line,'r')
	suche = search.readlines()
	suche2 = "".join(suche)
	print suche2
	if suche2.count(">gag") == 1:			
		counter += 1
	if suche2.count(">pol") == 1:
		counter += 1
	if suche2.count(">env") == 1:
		counter += 1
	if counter != 3 :
		print counter
		os.system('mv ./proteins/'+line+' ./proteins/problems/'+line)
	search.close()			
get_file()
main()		
