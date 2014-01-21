from string import *

def Main():
	gagliste = open("gag_subtype_recombinant","r")		# Opening all those fancy input-files
	polliste = open("pol_subtype_recombinant","r")
	envliste = open("env_subtype_recombinant","r")	
	outputliste = open("subtypes_recombinant","a")		# Same for the output-file
	gag = gagliste.readlines()				# Getting all those beautiful lines into a list
	pol = polliste.readlines()
	env = envliste.readlines()
	polstring = "".join(pol)				# converting lists into strings
	envstring = "".join(env)

	for i in gag:						# Start searching for Subtypes
		subtype = i
		print subtype.find("SUBTYPE")		
		if subtype.find("SUBTYPE")!=-1:			# Is this a new Subtype? 
			outputliste.write(i)			# If so write subtypename into new list

		else:						# If not it should be an identifier

			if envstring.find(i) != -1:		# Now lets check if we got a env-proteinseq. 
				if polstring.find(i) != -1: 	# Oh, and a pol-proteinseq. should be there too
					outputliste.write(i)	# Great, we got all 3 sequences, so write this identifier down

Main()
