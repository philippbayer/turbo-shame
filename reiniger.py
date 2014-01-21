from string import *

dna = open("SIV_gag_aa checked", "r")
out3 = open("SIV_gag_aa.fastachecked","a")
eingabe2 = dna.readlines()
leng2 = len(eingabe2)
zwischenstring1 = ""
zwischenstring2 = ""
i = 0
while i < leng2-1:
	zwischenstring1 = eingabe2[i]
	zwischenstring2 = eingabe2[i+1]
	if zwischenstring1.find(">") != -1:
		if zwischenstring2.find(">") == -1:
			out3.write(zwischenstring1+zwischenstring2)
	print zwischenstring1
	i += 1 

