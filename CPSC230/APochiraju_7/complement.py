#Gabriel and Zach
def complement(sequence):
    sequence = sequence.upper()
    notvalid = "BDEFHIJKLMNOPQRSUVWXYZ"
    nogo = 0
    comSequence = []
    for element in sequence:
        if (element in notvalid): #if element isn't ACTG
            nogo = 1
        if (element == "A"):
            comSequence.append("T")
        if (element == "T"):
            comSequence.append("A")
        if (element == "C"):
            comSequence.append("G")
        if (element == "G"):
            comSequence.append("C")
    if (nogo != 0):
        print("Could not calculate.  Only enter A, C, T, or G.")
        return " "
    else:
        comSequence = "".join(comSequence)
        return comSequence

def revComplement(sequence):
    sequence = complement(sequence)
    sequence = list(sequence)
    sequence.reverse()
    sequence = "".join(sequence)
    return sequence

com = input("Enter in a DNA sequence: " ,)
print("The complement of your DNA is:", complement(com), "\nThe reverse complement of your DNA is:", revComplement(com))
