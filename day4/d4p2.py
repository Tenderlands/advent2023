from aocd import get_data
import re

listInput = re.split('\n', get_data(day=4, year=2023))

total = 0
instanceList = [1] * len(listInput)

for item in listInput:
    card, winning, nums = re.split(r':|\|', item)
    winning = re.split(' ', winning)
    nums = re.split(' ', nums)
    cardNo = int(re.sub('Card ', '', card))
    points = (len(set(winning).intersection(set(nums))) - 1)
    currentInstances = instanceList[cardNo - 1]
    for i in range(0, points):
        if cardNo + i <= len(instanceList) - 1:
            instanceList[cardNo + i] += currentInstances
    total += currentInstances
print(total)
