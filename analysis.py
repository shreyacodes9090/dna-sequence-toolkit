codon_table = {
    "AUA":"Ile", "AUC":"Ile", "AUU":"Ile", "AUG":"Met",
    "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
    "AAC":"Asn", "AAU":"Asn", "AAA":"Lys", "AAG":"Lys",
    "AGC":"Ser", "AGU":"Ser", "AGA":"Arg", "AGG":"Arg",
    "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",
    "CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro",
    "CAC":"His", "CAU":"His", "CAA":"Gln", "CAG":"Gln",
    "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
    "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
    "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
    "GAC":"Asp", "GAU":"Asp", "GAA":"Glu", "GAG":"Glu",
    "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
    "UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
    "UUC":"Phe", "UUU":"Phe", "UUA":"Leu", "UUG":"Leu",
    "UAC":"Tyr", "UAU":"Tyr", "UAA":"Stop", "UAG":"Stop",
    "UGC":"Cys", "UGU":"Cys", "UGA":"Stop", "UGG":"Trp"
}    


def gc_content(sequence):
    g_count= sequence.count("G")
    c_count=sequence.count("C")
    gc_total = g_count+ c_count
    sequence_length= len(sequence)
    gc_percentage = ( gc_total /sequence_length) * 100
    return gc_percentage




def transcribe(sequence):
   rna_sequence=  sequence.replace("T" , "U")
   

   return rna_sequence



def translate (rna_sequence):
    protein=""
    for i in range(0,len(rna_sequence), 3):
        codon= rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid=codon_table[codon]
            protein += amino_acid + " "
    return protein

print(translate("AUGUUUAA"))

#TEST BLOCK
test_seq= "ATTGCA"
print(gc_content(test_seq))
print(transcribe(test_seq))
print(translate(transcribe(test_seq)))