# package reading fasta files (biopython)
import os.path
from Bio import SeqIO
 
class Sequence: # base class
    def __init__(self,
                 sequence):
        if not (self.__checkValid(sequence)):
            raise ValueError('This is not a valid sequece')
        else:
            self.__sequence = sequence

    def getAsString(self):
        return str(self.__sequence) # ensure copy is returned

    # returns a reversed the subsequence from start to end (default implemtation)
    @staticmethod
    def reverseSequence(seq):
        seq_string = seq.getAsString()
        seq_length = len(seq_string)
        return Sequence(seq_string[seq_length::-1])

    def setFromString(sequence):
        if not self.__checkValid(sequence):
            raise ValueError('This is not a valid sequece')
        self.__sequence = sequence
        
    def __getitem__(self, item): # needs to be subscriptable (like a list of characters)
         return self.sequence[item]

    def __str__(self): # gives back string instead of class attribute
        return "%s" %(self.getAsString())

    def __len__(self): # overload of length function for the class
        return len(self.sequence)
    
    def __checkValid(self, sequence): # TODO: check if it is sequence 
        return True

class ProteinSequence(Sequence): # inheritance
    # constructor must call base init
    def __checkValid(self, sequence): # overload
        # if only consists of AAs return true
        return True

class RNASequence(Sequence): # inheritance
    # constructor must call base init
    def __checkValid(self, sequence): # overload
        # if only consists of NAs return tre
        return True

#class ModifiedRNASequence(Sequence): # inheritance
    # constructor must call base init
    def __checkValid(seq): # overload
        # if only consists of NAs return tre  # now checks for [ ] also allowed
        return seq

    def reverseSequence(start, end):
        pass # do something TODO

class Entry:
    # parameterized constructor - additional add default value if nothing is passed
    def __init__(self, 
                 identifier="",
                 sequence="",
                 decoy_sequence=""):
        self.identifier = identifier # immer valide muss nicht gekapselt werden 
        self.sequence = Sequence(sequence)
        self.decoy_sequence = decoy_sequence        
        
        # works with all subclasses of Sequence
class DecoyGenerator:
    @staticmethod
    def reverseSequence(seq: Sequence):
        rev_seq = Sequence.reverseSequence(seq)
        return rev_seq

class FastaFile: #Factory?
    @staticmethod
    def read(path):
        entries = [] # TODO:would you do it this way? 
        extension = os.path.splitext(path)[1].strip('.')
        for seq_record in SeqIO.parse(path, extension):
            entry = Entry(identifier=seq_record.id)
            entry.identifier = seq_record.id
            # check if Protein #TODO
            entry.sequence = ProteinSequence(seq_record.seq)
            # check if RNA? #TODO
            #entry.sequence = RNASequence(seq_record.seq)
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
        elements.decoy_sequence = DecoyGenerator.reverseSequence(elements.sequence)

        print(elements.identifier)
        print(type(elements.sequence))
        print(elements.sequence)
        print(elements.decoy_sequence)
        