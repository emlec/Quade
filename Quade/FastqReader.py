# -*- coding: utf-8 -*-

# Standard library imports
from gzip import open as gopen

# Local imports
from FastqSeq import FastqSeq


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def FastqReader(fastq_file):
    """ Simple fastq reader returning a generator over a fastq file """
    try:

        # Open the file depending of the compression status
        fastq = gopen(fastq_file, "rb") if fastq_file[-2:] == "gz" else open(fastq_file, "rb")
        i = 0

        # Iterate on the file until the end
        while True:

            # Extract informations from the fastq file
            name, seq, sep, qual = next(fastq), next(fastq), next(fastq), next(fastq)

            # Try to generate a valid FastqSeq object
            try:
                yield FastqSeq(
                    name=str(name.rstrip()[1:].split()[0], 'utf-8'),
                    seq=str(seq.rstrip(), 'utf-8'),
                    qual=str(qual.rstrip(), 'utf-8'))

                i += 1

            except AssertionError as E:
                print(E)
                print("Skipping the sequence")

    except IOError as E:
        print(E)
        print("Error while reading {} file".format(fastq_file))
        exit()

    except StopIteration:
        raise StopIteration("\t{} sequences parsed".format(i))
