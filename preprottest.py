from string import *

tab = open('tabelle','r')
aain = open('pol_aa_MSA.fasta','r')
aaout = open('pol_aa_MSA.prottest','a')
aain2 = aain.readlines()
aain2 = ''.join(aain2)

for line in tab:
	if aain2.find(line) != -1:
		anfang = aain2.find(line)
		ende = aain2.find('>',anfang)
		aaout.write('>'+aain2[anfang:ende])
