def mRNAtranscription(dna_template):
    dna2rna = {'A':'U','T':'A','C':'G','G':'C' }
    mRNA = ''
    for base in dna_template:
    	if base in dna2rna.keys():
    		mRNA+=(str(dna2rna[base]))
    return mRNA
dna_template="ATCGATTG"
print(mRNAtranscription(dna_template))