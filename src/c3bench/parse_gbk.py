from Bio import SeqIO
from cogent3.parse.genbank import iter_genbank_records
from skbio.io import read

from c3bench import measure


@measure.record_time_and_size
def bp(path):
    return list(SeqIO.parse(path, "genbank"))


@measure.record_time_and_size
def c3(path):
    return list(iter_genbank_records(path))


@measure.record_time_and_size
def sb(path):
    return list(read(path, format="genbank"))
