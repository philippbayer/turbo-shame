from string import *

Codon ={'ttt':'F','ttc':'F','tta':'L','ttg':'L','ctt':'L','ctc':'L','cta':'L','ctg':'L','att':'I','atc':'I','ata':'I','atg':'M','gtt':'V','gtc':'V','gta':'V','gtg':'V','tct':'S','tcc':'S','tca':'S','tcg':'S','cct':'P','ccc':'P','cca':'P','ccg':'P','act':'T','acc':'T','aca':'T','acg':'T','gct':'A','gct':'A','gcc':'A','gca':'A','gcg':'A','tat':'Y','tac':'Y','taa':'*','tag':'*','cat':'H','cac':'H','caa':'Q','cag':'Q','aat':'N','aac':'N','aaa':'K','aag':'K','gat':'D','gac':'D','gaa':'E','gag':'E','tgt':'C','tgc':'C','tga':'*','tgg':'W','cgt':'R','cgc':'R','cga':'R','cgg':'R','agt':'S','agc':'S','aga':'R','agg':'R','ggt':'G','ggc':'G','gga':'G','ggg':'G','ttr':'L','tcr':'S','tar':'*','ctr':'L','ccr':'P','car':'Q','cgr':'R','acr':'T','aar':'K','agr':'R','gtr':'V','gcr':'A','gar':'E','ggr':'G','tra':'*','acn':'T','tcn':'S','ctn':'L','ccn':'P','gtn':'V','ggn':'G','gcn':'A','cgn':'R','acv':'T','tcv':'S','ctv':'L','ccv':'P','gtv':'V','ggv':'G','gcv':'A','cgv':'R','acw':'T','tcw':'S','ctw':'L', 'ccw':'P','gtw':'V','ggw':'G','gcw':'A','cgw':'R','acs':'T','tcs':'S','cts':'L','ccs':'P','gts':'V','ggs':'G','gcs':'A','cgs':'R','acm':'T','tcm':'S','ctm':'L','ccm':'P','gtm':'V','ggm':'G','gcm':'A','cgm':'R','atm':'I','ack':'T','tck':'S','ctk':'L','cck':'P','gtk':'V','ggk':'G','gck':'A','cgk':'R', 'acy':'T','tcy':'S','cty':'L','ccy':'P','gty':'V','ggy':'G','gcy':'A','cgy':'R','tty':'F','aty':'I','tay':'Y','cay':'H','aay':'N','gay':'D','tgy':'C','agy':'S','yua':'L','yug':'L'}

def Main():
	global dnaout
	global proteinout
	liste = open("tabelle",'r')				# Opening Input-list
	namelist = liste.readlines()
	dnaout = open("HIVSIV env DNA checked", 'a')		# Opening Output-list
	proteinout = open("HIVSIV env Prot checked", "a")
	
	dnas = open('SIV_env_nt.fasta', 'r')			# Opening List with DNA-Sequences
	dna = dnas.readlines()					# Read DNA-Lines
	dna = "".join(dna)					# Convert List into string
	dnalist = []	

	proteins = open('SIV_env_aa.fasta', 'r')		# Opening List with Protein-Sequences			
	protein = proteins.readlines()				# Reading Lines
	protein = "".join(protein)				# Convert List into string
	proteinlist = []
	global z
	for z in namelist:
		z = z.replace('\n','')
		dnaout.write('>'+z+'\n')			# Write name into output-file
		proteinout.write('>'+z+'\n')
		dnaheader = dna.find(z)				# Find sequence	
		dnaanfang = find(dna, "\n", dnaheader)		# Find start of sequence
		dnaende = find(dna, ">", dnaheader)		# Find end of sequence
		dnaseq = dna[dnaanfang+1:dnaende-1]		# Write sequence
		dnaseq = replace(dnaseq,'\n','')		# Remove whitespaces
		dnalist.append(dnaseq)

		proteinheader = find(protein, z)		
		proteinanfang = find(protein, "\n", proteinheader)		# Find start of protein-sequence
		proteinende = find(protein, ">", proteinheader)			# Find end of proteinsequence
				
		proteinseq = protein[proteinanfang+1:proteinende-1]		# Write sequence
		if proteinseq.find('\r\n') != -1:
			proteinseq = proteinseq.replace("\r\n","")		# Remove whitespace
			proteinseq = proteinseq.replace("\n","")
		else:
			proteinseq = proteinseq.replace('\n','')
		compare(dnaseq,proteinseq)

def translator(dna):
	dna = lower(dna)					# Because the Dictionary is in lower case 	

	frame1 = dna
	f1len = len(frame1)
	frame2 = dna[1:]					# Create 6 Frames
	f2len = len(frame2)
	frame3 = dna[2:]
	f3len = len(frame3)
	dnar = dna[::-1]
	frame4 = dnar
	f4len = len(frame4)
	frame5 = dnar[1:]
	f5len = len(frame5)
	frame6 = dnar[2:]
	f6len = len(frame6)

	x = "X"

	i = 0
	f1 = ""

	while i <= f1len-3:
		codi = frame1[i:i+3]				# Get triplets
		test = Codon.has_key(codi)

		if test == 1:					# Is the triplet in the dictionary?
			f1 = f1 + Codon[codi]			# If it is, append AA to the frame
		else:
			f1 = f1 + x				# Else append the "X"-Acid
		i += 3

	i = 0
	f2 = ""
	while i <= f2len-3:
		codi = frame2[i:i+3]
		test = Codon.has_key(codi)
		
		if test == 1:
			f2 = f2 + Codon[codi]
		else:
			f2 = f2 + x
		i += 3

	i = 0
	f3 = ""
	while i <= f3len-3:
		codi = frame3[i:i+3]
		test = Codon.has_key(codi)

		if test == 1:
			f3 = f3+ Codon[codi]
		else:
			f3 = f3 + x
		i += 3

	i = 0
	f4 = ""
	while i <= f4len-3:
		codi = frame4[i:i+3]
		test = Codon.has_key(codi)
	
		if test == 1:
			f4 = f4 + Codon[codi]
		else: 
			f4 = f4 + x
		i += 3

	i = 0
	f5 = ""
	while i <= f5len-3:
		codi = frame5[i:i+3]
		test = Codon.has_key(codi)

		if test == 1:
			f5 = f5 + Codon[codi]
		else:
			f5 = f5 + x
		i += 3

	i = 0
	f6 = ""
	while i <= f6len-3:
		codi = frame6[i:i+3]
		test = Codon.has_key(codi)

		if test == 1:
			f6 = f6 + Codon[codi]
		else:
			f6 = f6 + x
		i += 3
	

	Frames = [f1,f2,f3,f4,f5,f6]					# Create list with all 6 frames
	return Frames
	


def compare(dna,protein):
	Transprot = translator(dna)
	protein = protein.rstrip()
	dnalen = len(dna)
	f1 = []
	f2 = []
	f3 = []
	f4 = []
	f5 = []
	f6 = []
	dnaframes = [f1,f2,f3,f4,f5,f6]
	dnarev = dna[::-1]
	i = 0							
	k = 0
	while i < len(Transprot):
		if i < 3:
			y = 0
			while y <= dnalen:
				dnaframes[i].append(dna[i+y:i+y+3])
				y += 3
		else:			
			y = 0
			while y <= dnalen:
				dnaframes[i].append(dnarev[i+y-3:i+y])
				y += 3
		i += 1

	for j in Transprot:
		Transprot[k] = Transprot[k].rstrip()
		transstring = Transprot[k]				# Make a string out of list
		transstring = transstring.replace("\n","")
		protein = protein.rstrip()
		
		if find(transstring,protein) != -1:			# Are translated and actual protein the same?
			x = find(transstring,protein)		
			dnaframes[k] = dnaframes[k][x:]			# Beginning dnastring with beginning of translated protein
			while x < len(protein):
				if protein[x] == "X":			# Is there a X?
					protein = protein[:x] + protein[x+1:]	# Then cut it out.
					del dnaframes[k][x]			# And the corresponding DNA-triplet, too please.
				x += 1
			dnalist = "".join(dnaframes[k])
			dnaout.write(dnalist + "\n")
			proteinout.write(protein + "\n")
		k += 1 
	
Main()
