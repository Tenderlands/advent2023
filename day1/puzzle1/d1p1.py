import re

tInput = ""
dMap = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"

}
with open("input.txt", "r") as f:
    tInput = f.read()
lInput = tInput.split("\n")
total = 0
for line in lInput:
    for digit in dMap:
        line = re.sub(digit, dMap[digit], line)
    tempLine = re.sub('[\D]', '', line)
    if len(tempLine) >= 2:
        first = tempLine[0]
        last = tempLine[len(tempLine) - 1]
        total += int(first) * 10 + int(last)
    elif len(tempLine) == 1:
        total += int(tempLine[0]) * 11
print(total)
