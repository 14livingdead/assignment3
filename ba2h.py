def DistanceBetweenPatternAndStrings(Pattern, Dna):
    #split space delimited string into array
    Dna = Dna.split(' ')
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
print(DistanceBetweenPatternAndStrings("ATTGGC","GAACCCGCCACCCATTGTAACTGTGGCAGTCTACAAGTCCTTACTGATAACACGCAACCGCGTCGGAGCGGTATGAAGATCTGCTTGTAT GACAATCTCTCGGTCTGCAAGACGTTGCTTCCGGAATCGATCGCACCGGGGATTCATGTAAGATCTTCTGGGTCATGCAGAGTAGACATG TAGTGACTTAGCGCGCAACTACGGGCGGGCCCCCGGAGAGCGACATTGGGTGTCCTGACTAAGATCGAAGCTTCTGTTTTAAAGTTCAAG TGGTTATCCTTAGCGTGCCCGACTTTTACCTAAAATTCAAATCCACACATAGGTGTCGCTTAATGCTTCGTGTACATTCTGGCCACCCAA TGCCTGTACAAGGTCGATGCTTCCCGAGTCTGATTCTTAAATCCCTCACGAACAATCCCCCAAAGAATACAGTGCCGCTAAGCCCGCTCT ACCGCGCCTGCATTTTCGAAAGCGAAACTGTGAAATGTATGAAATAGGGTGCCTGTGGGTATTTGTGACAAATAGACCTTTGGCCAGGAC GCGAAGATGCGAGCAGAAAGTCCACGCGCCGTTTCACTATCACTGATAGCTACATACGATGCGGACAAGAGCTTTCGAACAGTGCGTGTT CGGACTTTTAGTTGGAAACCTATCCGTGGTACGAGCTACCCATCCTGCAGAGGCAAGGACATGCGAATGCCTACGCATCTGTGTCGTTAT TAGCGGACACGAAGCGCCGTCTTCTTGACTTTACAAAGTCGTTGACTGTTGGTTAAGTACGAAACAGCCCATCTTCTAGCTGGCTGAGAA CCGTCGGCCAGTCTTATAGTATAATGATTTGAAAGTCGAATCCCTATCCTGAACGAGGTTTTCGTTCAGCGCAAGCGACAGGGATTAGAG CAACTCGTACTTGCGTAACCCGGCACTGCGCATAACATTCTAAATAGGTTTTCTTAGCGGGGTAGGGCTAGTTCCCAGTGTAACTTGTAC GCAGACCGTGCCTGGGATCTGTGGCAGGACCGAGATCTAACATGCGACAACGATATCGGTCGTACGGTCCCTGGGATAGTGATCTCGCGA GGCGACTGCCTGACCAAGCGACAAAGGGGCCAGTTGCCACGTAGATTGTCTGTTGTTTTCAACGCCCTAGAGGAGAGATTCAGCCGAAGA TCGGAGCTGGTGCTAACCATAAACAGCGTGTTAACGAAACGGTTTCATTGACATCCTGCCAATCACCCGAGTCACTCGCCTCAAATCGTC TCCCGCTAATATTCATAGACCCTCGGGGTCGTACCATGTTGCCGGTCACATTTCAAAGACGCTTGTATGGTTCCGGTTACCGGCTCACGA GTGTTGCTATCTGTTCAGGACGTCCGCTAGAACTCTCAAGGTAGACTATCAGCATAGGCATCCCGGAATCAGACGTGGGACGTCTGTCGT CTATAGCCAGTTGTTAATGTTTTTATACTCGAAGCCAGCGAATCCTTATCAGATGACGAGACTTCCGCGAGAGAAGTTAGTCCTAGCCGG AAAGACAGTTGGAACTAGCTAGGTCCTGGTCAATCCGATAGATACATTTCCTCGTTTCGAGTTTCCGGCTTTCGAAATCATGAACGCGCT AGGTAATTCGACTATCCCGGTTTGTGGTGCGTAGGAGCGTAAGGGAAGAGACATACCACGCACTTTCATGTGTAGAGGAGTACATCAGTA GCCCCTAGTACCTTCGAAGATTTAGGGTTAACTCAGCTTCATTCACAGAAGCCATCAGTACATAGGCGGTCCAATGGCAGATGGGTCTTT CCTTCCAGGCGTCCACGCATGCCATTGTCGAGCATGTCCGGTGTTGGGATGCCGCAAAAAAATGCGCCAAACTGGTTGCATGGTCCCTAT CTGGGCTCGTACGATTTGTATCCGCTATCCACGAAAATGCAAGCTCAGTGTATATCTTCTAAACCGAAACACAAACGATAAACCGTTTAT ATCGTAAACTACTTCACTTGCGGCGCGCGCAAGCCCGGAAAAACACATATCGACTGATCCTCCCCTAATAGATGATTCATGCTTCGAAAC ATAATCAGCCCGAGCCACGTAGTTCAATGCTGAAGACTGGCATCCTAAGACGCACATTAAATCGTCGGGAAGACTCCATTATGACCCAGA TTGGAAGCCCCAAAAAGGACGGGGTCAGTGCGAGAGTGTACGATGCACAGAGGTCTGTATGACCACAGGACAGAACCCGCGGGGCTGCTG TATTACGCGTTTTTTGTGCATTAACTAAGTTAGGGTGTGTAAACCTATTGTCGGTCGAATAGGGATTTCAGGTCTCAAGGCCCTGTGAGC ATGAGTGCTCCCGTACTGATTTTTTAAACCTAAGGCCGCAACTACTTGGAAGGGTGCATATAGAACGCGTTCCACTTTTGAGTAACATCC AATGTAAGGTATTGGCTACCGTAGTGTTAGTTAGCTCTACTAGAAATATTCCAAGGTTCAGGCCTAGGGGGGCTGGGATGATGTGTGATC CATAGTTCTAGTATGATGGGGCCCGATACTTCCACGCTCTGCGCGCTCAGAGGGGGTACGTTTACATTTGAGAGTCGCCCTGGTCCTCAC CTAGTCGGCCATGCAGCGATTTAGCCAATTTGTGCAAACCAGCTCGCCTTTCTAAGATGAGGAGATTCTAAGTAAGTAAAGCCGTCCTAG TAGATGAGCGTGCGTCAAAGTCCGGCGTCCCCCTCATGCTAGATGGAGTACCCCGCACGGATAAGCCTCTATTTGAATCTCTCTATGAGC CATCCCGGCCAAATAAAGTCTTAACTTGCGGTTTCGCATCGGTGTAACTAAATAACCGTTTGTTGTCCAATATGTACATGCCGTCCGCAA TACTTATGCTTCTAGGCCTGCTGCGTTGGGGGATGAGCTGTAAACGCGGCCAGTCAACAAAGACTTTCTACTCCATCCGGGCTATAGTAG AGTTGTGTTAGACCTTTTTCCACATCGATCCGCCGCGCCATCGGCACGATCCGGGGCGGGCAAACTTCACGTGCGAACAGAGGATACTGG GTACGGTCCAGGCTGTCGCCGCTTATACGGCACAGAACCTAATCCTCGAAAATCCCGCAAGTGGGAGGCGAGTCCTTATCAATGGGCGAG CTCCTAGGTGGCCAATGGCAATCTGTGGAACAACATTCGATAACCACACGTACAGTCCGGGCAACCGCTTACCTGTCAAGTCGGGAAAAA GTCTTAACACCCAGATCAAACTTAAATGATGAATCCTCTAGAACCCCAGTCCGGGCCCAACGGCTCCTATAGGTCGACGCGACTAGTGAA AAGTCAGTAACACGGACATGTCGAATTAATGCGACTATGCTGGCATAGTACTCCTACCGCCTTTAGAACGATGATCATACGTTCGTCCGA GCGTCGTGTTCCACATCTGGTCTCAATACATCCGGAACAGTTGGTGAAGCTTCGGTCAAGATTGTTGCAATTTGTTCCCTAGGTTTGTCG"))