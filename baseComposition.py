def baseComposition(dna_seq): 
	dict1 = {'A': 0, 'C': 0, 'T': 0,  'G': 0 }
	for i in dna_seq:
		if i in dict1.keys():
			dict1[i]+=1
	return dict1
dna_seq="CTATCGGCACCCTTTCAGCA"
print(baseComposition(dna_seq))