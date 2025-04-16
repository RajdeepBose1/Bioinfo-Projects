import collections

Nucleotide = ["A", "C", "G", "T"] 

def ValidateDNA(dna):
    tmp_seq = dna.upper()
    for i in tmp_seq:
        if i not in Nucleotide:
            return "Not a valid DNA sequence"
    return tmp_seq


def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(collections.Counter(seq))
