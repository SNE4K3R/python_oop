# fasta -> read() -> class xxx -> DecoyGenerator -> prot/rna seq -> decoysequene -> write() 

# class FastaFile    
    #identifier # label 
    #Sequence
    #DecoySequence
    #read()  # biopython
    #write() # biopython

#class DecoyGenerator
    #method reverse_protein_seq() - check internally if protein or RNA
    #method reverse_rna_seq()
    
#class Sequence 
   #method checkValid

# class Protein_seq
    #method checkValid
        
# RNA Sequence (modifications in the code -> can not do a reverse string)
   #method checkValid
    # prases everything within bracets as asingle unit

# package reading fasta files (biopython)
import os.path
from Bio import SeqIO
 

class Sequence: # base class
    def __init__(self,
                 sequence=""):
        self.sequence = sequence

    def __str__(self): # gives back string instead of class attribute
        return "%s" %(self.sequence)
    
    def checkValid():
        pass

class ProteinSequence(Sequence): # inheritance
    def checkValid(): # overload
        pass

class RNASequence(Sequence): # inheritance
    def checkValid(): # overload
        pass

class Entry:
    # parameterized constructor - additional add default value if nothing is passed
    def __init__(self, 
                 identifier="",
                 sequence=Sequence(),
                 decoy_sequence=""):
        self.identifier = identifier
        self.sequence = Sequence(sequence)
        self.decoy_sequence = decoy_sequence
        
class DecoyGenerator:
    def reverseSequence():
         # check which sequence? 
        pass

class FastaFile:
   
    @staticmethod
    def read(path):
        entries = [] # TODO:would you do it this way? 
        extension = os.path.splitext(path)[1].strip('.')
        for seq_record in SeqIO.parse(path, extension):
            entry = Entry(identifier=seq_record.id)
            entry.identifier = seq_record.id
            entry.sequence = Sequence(seq_record.seq)
            entries.append(entry)
        return entries
    
    @staticmethod
    def write(entries, path):
        pass

if __name__ == "__main__": 
    
    #path = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/protein_small_test.fasta"
    path = "/mnt/e/debian_prog/vorkurs_python_oop/protein_small_test.fasta"
    entries = FastaFile.read(path)
        
    for elements in entries:
        print(elements.identifier)
        print(type(elements.sequence))
        print(elements.sequence)