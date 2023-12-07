from aocd import get_data
lines = get_data(day=5, year=2023).strip().split('\n')


seeds = list(map(int, lines[0].split(" ")[1:]))

maps = []

i = 2
while i < len(lines):
    catA, _, catB = lines[i].split(" ")[0].split("-")
    maps.append([])
    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1
    i += 1


def findloc(s):
    curNum = s

    for m in maps:
        for dstStrt, srcStrt, rngeLen in m:
            if srcStrt <= curNum < srcStrt + rngeLen:
                curNum = dstStart + (curNum - srcStart)
                break
    return curNum


locs = []

for seed in seeds:
    loc = findloc(seed)
    locs.append(loc)
print(f'Part 1 answer: {min(locs)}')
#
# locs.clear()
# new_seeds = []
# seed_ranges = list(zip(seeds[0::2], seeds[1::2]))
# for s_range in seed_ranges:
#     start , length = s_range
#     for i in range(0, length):
#         new_seeds.append(start+i)
# print(new_seeds)
#
# for seed in new_seeds:
#     loc = findloc(seed)
#     locs.append(loc)
# print(locs)
# print(f'Part 2 answer: {min(locs)}')