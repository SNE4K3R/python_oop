# package reading fasta files (biopython)
import os.path
from Bio import SeqIO
 
class Sequence: # base class #TODO: Unfortunatley the __init__ of the superclass is not automatically used in the superclass
    def __init__(self, sequence):
        if not (self.__checkValid(sequence)):
            raise ValueError('This is not a valid sequece')
        else:
            self.__sequence = sequence

    def getAsString(self):
        return str(self.__sequence)

    def setFromString(self, sequence):
        if not self.__checkValid(sequence):
            raise ValueError('This is not a valid sequece')
        self.__sequence = sequence
        
    def __getitem__(self, item): # needs to be subscriptable (like a list of characters)
         return self.__sequence[item]

    def __str__(self): # gives back string instead of class attribute
        return "%s" %(self.getAsString())

    def __len__(self): # overload of length function for the class
        return len(self.__sequence)
    
    def __checkValid(self, sequence):
        return True

    # returns a reversed the subsequence from start to end (default implemtation)
    @staticmethod
    def reverseSequence(seq):
        seq_string = seq.getAsString()
        return Sequence(seq_string[::-1])

#You need to call the __init__ method of the base class from the __init__ method of the inherited class.
class ProteinSequence(Sequence): #inheritance
    def __init__(self, sequence):
        super(ProteinSequence, self).__init__(sequence)
        if not (self.__checkValid(sequence)):
            raise ValueError("The squence " + sequence + " is not a valid Proteinsequence, please check your database")
        else:
            self.__sequence = sequence

    # constructor must call base init
    def __checkValid(self, sequence):
        for letter in sequence:
            if letter not in "GALMFWKQESPVICYHRNDTUO":
                    return False
        return True

class RNASequence(Sequence): #inheritance
    def __init__(self, sequence):
        super(RNASequence, self).__init__(sequence)
        if not (self.__checkValid(sequence)):
            raise ValueError("The squence " + sequence + " is not a valid RNA-Sequnce, please check your database")
        else:
            self.__sequence = sequence

    # constructor must call base init
    def __checkValid(self, sequence): #overload
        for letter in sequence:
            if letter not in "GUAC":
                return False
        return True

# #class ModifiedRNASequence(Sequence): # inheritance
#     # constructor must call base init
#     def __checkValid(seq): # overload
#         # if only consists of NAs return tre  # now checks for [ ] also allowed
#         return seq

#     def reverseSequence(start, end):
#         pass # do something

class Entry:
    # parameterized constructor - additional add default value if nothing is passed
    def __init__(self, 
                 identifier="",
                 sequence="",
                 decoy_sequence=""):
        self.identifier = identifier #does not need to be encapsulated since it is always valid
        self.sequence = Sequence(sequence)
        self.decoy_sequence = Sequence(decoy_sequence)
        
# works with all subclasses of Sequence
class DecoyGenerator:
    @staticmethod
    def reverseSequence(seq: Sequence):
        rev_seq = Sequence.reverseSequence(seq)
        return rev_seq

# TODO: Difference between Protein / RNA sequence not general,
# since this is checked internally.
class FastaFile:
    @staticmethod
    def read(path):
        entries = []
        extension = os.path.splitext(path)[1].strip('.')
        for seq_record in SeqIO.parse(path, extension):
            entry = Entry(identifier=seq_record.id)
            entry.identifier = seq_record.id
            if entry.identifier.startswith("sp"): #swissprot specific
                entry.sequence = ProteinSequence(seq_record.seq)
            if not entry.identifier.startswith("sp") and "RNA" in entry.identifier:
                entry.sequence = RNASequence(seq_record.seq)
            entries.append(entry)
        return entries
    
    @staticmethod
    def write(entries, path):
        pass

if __name__ == "__main__": 
    
    #path = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/protein_small_test.fasta"
    #path = "/mnt/e/debian_prog/vorkurs_python_oop/protein_small_test.fasta"
    path = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/protein_rna.fasta"
    entries = FastaFile.read(path)
        
    for elements in entries:
        elements.decoy_sequence = DecoyGenerator.reverseSequence(elements.sequence)

        print(elements.identifier)
        print(type(elements.sequence))
        #print(elements.sequence)
        #print(elements.decoy_sequence)
