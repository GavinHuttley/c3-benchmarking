import cogent3
from BCBio import GFF
from cogent3.parse.gff import gff_parser
from skbio.io import read

from c3bench import measure


@measure.record_time_and_size
def bp(path):
    with open(path) as in_handle:
        return list(GFF.parse(in_handle))


def _null(**kwargs):
    return kwargs


@measure.record_time_and_size
def c3(path):
    return list(gff_parser(path, make_record=_null))


@measure.record_time_and_size
def c3db(path):
    return cogent3.load_annotations(path=path)


@measure.record_time_and_size
def sb(path):
    return list(read(path, format="gff3"))
