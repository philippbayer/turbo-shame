from string import *

seqliste = open("env_aa_cleaned","r")
identifier = open("subtypes_recombinant","r")
output = open("subtypes_env_recombinant","a")

seqs = seqliste.readlines()
idents = identifier.readlines()
seqs = "".join(seqs)

for i in idents:
	if seqs.find(i) != -1:
		anfang = seqs.find(i)-1
		ende = seqs.find(">",anfang+1)-1
		output.write(seqs[anfang:ende] + "\n")


