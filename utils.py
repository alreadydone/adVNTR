from settings import *
from Bio import SeqIO


def get_min_number_of_copies_to_span_read(pattern, read_length=150):
    return int(round(float(read_length) / len(pattern) + 0.499))


def get_gc_content(s):
    res = 0
    for e in s:
        if e == 'G' or e == 'C':
            res += 1
    return float(res) / len(s)


def is_low_quality_read(quality_scores):
    low_quality_base_pairs = [q for q in quality_scores if q < QUALITY_SCORE_CUTOFF]
    if low_quality_base_pairs >= LOW_QUALITY_BP_TO_DISCARD_READ:
        return True
    return False


def get_chromosome_reference_sequence(chromosome):
    ref_file_name = HG19_DIR + chromosome + '.fa'
    fasta_sequences = SeqIO.parse(open(ref_file_name), 'fasta')
    ref_sequence = ''
    for fasta in fasta_sequences:
        name, ref_sequence = fasta.id, str(fasta.seq)
    return ref_sequence
