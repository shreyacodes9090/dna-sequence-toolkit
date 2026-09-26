def compare_sequences(seq1, seq2):
    mutations= []
    position= 0
    for base1, base2 in zip(seq1, seq2):
        if base1 != base2 :
            mutations.append(f"position{position} : {base1} -> {base2}")
        position += 1

    total_positions = position
    match_count= total_positions - len(mutations)
    similarity=(match_count/total_positions) * 100

    return mutations , similarity

