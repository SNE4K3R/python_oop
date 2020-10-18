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
                 description="",
                 decoy_description="",
                 sequence="",
                 decoy_sequence=""):
        self.description = description #does not need to be encapsulated since it is always valid
        self.decoy_description = decoy_description
        self.sequence = Sequence(sequence)
        self.decoy_sequence = Sequence(decoy_sequence)
        
# works with all subclasses of Sequence
# TODO: not optimal, since it sets the DECOY_ in front of the identifier
class DecoyGenerator:
    @staticmethod
    def generateDecoyID(description):
        decoy_description = "Decoy_" + description
        return decoy_description

    @staticmethod
    def reverseSequence(seq: Sequence):
        rev_seq = Sequence.reverseSequence(seq)
        return rev_seq

    @staticmethod
    def generateDecoy(entry: Entry):
        entry.decoy_description = DecoyGenerator.generateDecoyID(entry.description)
        entry.decoy_sequence = DecoyGenerator.reverseSequence(entry.sequence)

# TODO: Difference between Protein / RNA sequence not general,
# since this is checked internally.
class FastaFile:

    # the fasta format standarization has a newline every 60 characters
    # for better readability.
    @staticmethod
    def insert_newlines(string, every=60):
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

    @staticmethod
    def read(path):
        entries = []
        extension = os.path.splitext(path)[1].strip('.')
        for seq_record in SeqIO.parse(path, extension):
            entry = Entry()
            entry.description = seq_record.description
            if entry.description.startswith("sp"): #swissprot specific
                entry.sequence = ProteinSequence(seq_record.seq)
            if not entry.description.startswith("sp") and "RNA" in entry.description:
                entry.sequence = RNASequence(seq_record.seq)
            entries.append(entry)
        return entries
    
    @staticmethod
    def write(entries, path):
        f = open(path, "w")
        for elements in entries:
            f.writelines(">" + elements.description + "\n")
            writeable_seq = FastaFile.insert_newlines(elements.sequence.getAsString())
            f.writelines(writeable_seq + "\n")
            f.writelines(">" + elements.decoy_description + "\n")
            writeable_decoy_seq = FastaFile.insert_newlines(elements.decoy_sequence.getAsString())
            f.writelines(writeable_decoy_seq + "\n")
        f.close()


if __name__ == "__main__": 
    
    #path_in = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/protein_small_test.fasta"
    #path_in = "/mnt/e/debian_prog/vorkurs_python_oop/protein_small_test.fasta"
    path_in = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/protein_rna.fasta"
    path_out = "/Users/alka/Documents/work/teaching/20SS/VK/python_oop/decoydatabase.fasta"
    entries = FastaFile.read(path_in)

    for elements in entries:
        elements = DecoyGenerator.generateDecoy(elements)

    FastaFile.write(entries, path_out)
