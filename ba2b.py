def D(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        #the maxium hamming distance is the length of the pattern
        hd = k
        for i in range(0, len(Text) -k):
            # extract current kmer 
            kmer = Text[i:i+k]
            #omnomnonoonmnonoomm
            new_ham = HammingDistance(Pattern, kmer)
            if hd > new_ham:
                hd = new_ham
        distance = distance + hd
    return distance

def HammingDistance(Pattern, kmer):
    hd = 0 
    for i, c in enumerate(Pattern): 
        if c != kmer[i]:
                hd += 1
    return hd
def NumberToSymbol(s):
    if s == 0:
        return "A"
    elif s == 1:
        return "C"
    elif s == 2:
        return "G"
    elif s == 3:
        return "T"
def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index /4
    r = index % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex,k-1)
    return PrefixPattern + symbol

def MedianString(k, Dna):
    #split space delimited string into array
    Dna = Dna.split(' ') 
    #the maximum distance is the maximum hammingdistance(=k) times the numbers of strings in Dna 
    distance = k*len(Dna)
    best_kmer =""
    for i in range(0,(4**k-1)):
        Pattern = NumberToPattern(i,k)
        #dont recompute expenssssive $$$$$
        dist_of_pattern =D(Pattern,Dna)
        #add the equal like rosalinde likes it in her example (ACG vs GAC pick the last one)
        if dist_of_pattern <= distance:
            distance = dist_of_pattern
            best_kmer =Pattern
    return best_kmer
print(MedianString(6,"GTTCCCCCACAGAGCACCTACTGCCCTCGGCGCACAGTGATT CCGTATGTTATTTATACGAGGCCAATAACAACACACCCCCGC TATAGAGGCAAACCCGGGGTCATTTAACGACAAGAAATTAAA TACTCCGTCATTCCTAACTGCCTCCCGCTCAACCGCACCGTC TTCCTCTCGAGCCTTCCGTTATAATATACTGCCCATGTTATT GAGTGTGTAATTCTTAAAATTCTATGAGGCATCACTCTAGGT TGATTACTGTCAATACACGCGACTGCAGTGGTCATTGAAGGA GAAGGTTAGAAAAAAAGGGTCATTACAACGAATAGTTACATA TGGTCGAGGAAAGTTATTTTTTCACATTGCGATAACCCAGAT AATACTGGCACGACGAACGTAATTTACAGTTGGCAACAGCCG"))
