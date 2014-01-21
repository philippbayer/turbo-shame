from string import *

def Main():
	input = open('tree.txt','r')
	output = open('treecleaned.txt','a')
	tree = input.readlines()
	tree = ''.join(tree)	
	counter = 0	
	i = 0

	while i <= len(tree):
		shitbegin = tree.find(')',i)
		print shitbegin
		shitend = tree.find(':',shitbegin)
		tree = tree[:shitbegin+1] + tree[shitend:]
		i += 8
	output.write(tree+';')
Main()
