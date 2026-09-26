def get_sequence():               #GETS SEQUENCE FROM USER
    sequence = input("enter a DNA sequence: ")
    return sequence

def check_sequence(sequence): 
    if sequence == "":
        print("error:sequence cannot be empty.")
        return False    #checks if the sequence is valid or not
    is_valid = True  
    for letter in sequence:
        if letter not in "ATGC":
            is_valid = False   

    return is_valid    


def read_fasta(file_path):         #reads a fasta file sequence
    combined_sequence=""
    try:
    
        with open(file_path, "r") as file:
            for line in file:
                if not line.startswith(">"):
                    combined_sequence += line.strip()
    except FileNotFoundError:
        print("error : that file was not found. Please check the filname.")
    return combined_sequence
   

