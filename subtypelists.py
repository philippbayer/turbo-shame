from string import *

def Main():
	inputliste = open('ordered-subtypelist.txt','r')
	inputsequenz = open('env_aa_cleaned','r')
	outputsequenz = open('env_aa_subtyped','a')
	kopiertesequenz = ""
	liste = inputliste.readlines()
	eingabe = inputsequenz.readlines()
	eingabe = "".join(eingabe)

	for i in liste:
		print eingabe.find(i)
 		if eingabe.find(i)!=-1:
			anfangderzukopierendensequenz = eingabe.find(i)
			endederzukopierendensequenz = eingabe.find('>',anfangderzukopierendensequenz)-1
			kopiertesequenz = kopiertesequenz + eingabe[anfangderzukopierendensequenz:endederzukopierendensequenz] 
			

	outputsequenz.write(kopiertesequenz + "\n")

Main()
