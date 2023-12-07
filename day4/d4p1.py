from aocd import get_data
import re

listInput = re.split('\n', get_data(day=4, year=2023))

total = 0
for item in listInput:
    card, winning, nums = re.split(r':|\|', item)
    winning = re.split(' ', winning)
    nums = re.split(' ', nums)
    # 2^n-1, intersection also has empty string, so n-2
    points = 2 ** (len(set(winning).intersection(set(nums))) - 2)
    if points >= 1:
        total += points
print(total)
