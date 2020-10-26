# Make a decoy database generator

import os.path
from Bio import SeqIO

class Sequence:
    def __init__(self, sequence):
        if not (self.__checkValid(sequence)):
            raise ValueError("This is not a valid sequence")
        else:
            self.__sequence = sequence

    def getAsString(self):
        return str(self.__sequence)

    def __checkValid(self, sequence):
        return True

class ProteinSequence(Sequence):
    def __init__(self, sequence):
        super(ProteinSequence, self).__init__(sequence)

class Entry:
    def __init__(self,
                 description = "",
                 sequence = "",
                 decoy_description = "",
                 decoy_sequence = ""):
        self.description = description
        self.sequence = Sequence(sequence)
        self.decoy_description = decoy_description
        self.decoy_sequence = Sequence(decoy_sequence)

class FastaFile:
    @staticmethod
    def read(path):
        '''
        read a fasta file
        :param path: the path of the fasta file to read
        :return:
        '''
        entries = []
        extension = os.path.splitext(path)[1].strip('.')
        for seq_record in SeqIO.parse(path, extension):
            entry = Entry()
            entry.description = seq_record.description
            entry.sequence = seq_record.seq


if __name__ == "__main__":
    '''path_in = "../databases/protein_rna.fasta"
    path_out = ""
    entries = FastaFile.read(path_in)
    for elements in entries:
        elements = DecoyGenerator.generateDecoy(elements)
    FastaFile.write(entries, path_out)
    '''