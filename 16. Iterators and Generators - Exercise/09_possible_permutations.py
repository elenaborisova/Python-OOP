from itertools import permutations


def possible_permutations(seq: list):
    for p in permutations(seq):
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]
