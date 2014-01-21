import os,sys
from string import *

def main(): 
	input = open('tabellefuercgi.txt','r')
	output = open('subtypelist.txt','a')
	failoutput = open('nonote.txt','a')  
	List = []
	i = 0

	for line in input:
		line = line.rstrip()
		cgifile = open(line+'.cgi','r')
		cgifilegedaerm = cgifile.readlines()
		cgifilegedaerm = ''.join(cgifilegedaerm)

		if cgifilegedaerm.find('/note="subtype:') != -1:
			finder = cgifilegedaerm.find('/note="subtype:')
			subtypeend = cgifilegedaerm.find('\n',finder)
			subtypestart = cgifilegedaerm.find(':',finder)	
			nameofgame = cgifilegedaerm[subtypestart+1:subtypeend-2]
	
			List.append((nameofgame,line))
		else:
			failoutput.write(line+'\n')
	List.sort()
	while i < len(List):
		output.write(List[i][0]+': '+List[i][1]+'\n')
		print (List[i][0]+': '+List[i][1])
		i += 1

main()
