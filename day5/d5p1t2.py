import sys
from aocd import get_data


def translate(mapping, pairs):
    for start, end in pairs:
        for a1, a2, d in mapping:
            yield (start, min(a1, end))
            yield (max(a1, start) + d, min(a2, end) + d)
            start = max(start, min(a2, end))
            yield (start, end)


def solve(mappings, seed):
    for mapping in mappings:
        seed = [(a, b) for a, b in translate(mapping, seed) if a < b]
        return min(a for a, b in seed)


def parse(T, i=3):
    while i < len(T):
        current = []
        while i < len(T) and T[i] != '':
            s2, s1, length = (int(x) for x in T[i].split())
            current.append([s1, s1 + length, s2 - s1])
            i += 1
        yield sorted(current)
        i += 2

T = get_data(day=5, year=2023).splitlines()
print(T)
seeds = [int(x) for x in T[0].split(':')[1].split()]
mappings = list(parse(T))
answer1 = solve(mappings, ((x, x + 1) for x in seeds))
print(answer1)
