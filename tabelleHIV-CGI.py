import os,sys
from string import *

def get_file():
	os.system('find *.cgi > cgilist.txt')

def main():
	input = open('cgilist.txt','r')
	output = open('tabellefuercgi.txt','a')
	
	for line in input:
		finder = line.find('_nt')
		line = line[:finder]
		output.write(line+'\n')

get_file()
main()
