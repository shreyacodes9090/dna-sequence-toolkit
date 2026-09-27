import logging

from sequence_io import get_sequence , check_sequence , read_fasta 
from analysis import gc_content , transcribe, translate
from mutation import compare_sequences

logging.basicConfig(filename="activity.log" , level=logging.INFO, format ="%(asctime)s - %(message)s")

print("=== DNA sequence analysis toolkit ===")
print ("1. enter/load a sequence and analyze it")
print("2. compare two sequences for mutations")
choice =input ("choose an option:")

if choice =="1":
    input_choice= input("type 1 for manual entry , or 2 to load a FASTA file:")
    if input_choice=="1":
        sequence= get_sequence()
    elif input_choice=="2":
        filename = input("enter the FASTA filename: ") 
        sequence = read_fasta(filename)
    sequence= sequence.upper()   


    logging.info(f"sequence entered: {sequence}")   
    logging.info("sequence validated and analyzed")    
    
    if check_sequence(sequence):
        print("the sequence is valid")
        print("GC content:" , gc_content(sequence), "%")
        rna = transcribe(sequence)
        print("RNA:", rna)
        print("protein:" , translate(rna))
    else:
        print("the sequence is invalid")

    

elif choice=="2":
    seq1 = get_sequence().upper()
    seq2= get_sequence().upper()
    mutations, similarity = compare_sequences(seq1, seq2)
    print("mutations found:", mutations)
    print("similarity:" , similarity, "%")

    logging.info(f"compared two sequences , similarity: {similarity}%")        
else: 
    print("invalid choice")            