import itertools


def nwise(sequence, n=2):
    sequences = itertools.tee(sequence, n)
    temp = []
    for index, sequence in enumerate(sequences):
        sequence = itertools.islice(sequence, index, None)
        temp.append(sequence)
    return zip(*temp)
