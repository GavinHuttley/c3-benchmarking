from Bio import AlignIO
from cogent3 import load_aligned_seqs
from skbio import DNA, TabularMSA

from c3bench import measure


@measure.record_time_and_size
def bp(path):
    return AlignIO.read(path, "fasta")


@measure.record_time_and_size
def c3(path):
    return load_aligned_seqs(path, moltype="dna")


@measure.record_time_and_size
def c3h5s(path):
    return load_aligned_seqs(path, moltype="dna", storage_backend="c3h5s")


@measure.record_time_and_size
def sb(path):
    return TabularMSA.read(path, constructor=DNA, format="fasta", lowercase=True)
