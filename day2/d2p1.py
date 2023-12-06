import re

limits = {
    "red": "12",
    "green": "13",
    "blue": "14"
}
with open("inputd2p1.txt", "r") as f:
    tInput = f.read()
lInput = tInput.split("\n")
total = 0
for line in lInput:
    game, results = re.split(':', line)
    game = str.strip(re.sub('Game ', '', game))
    results = re.split(';', results)
    add = True
    print(game, results)
    for result in results:
        result = re.split(',', result)
        for item in result:
            digit, color = re.split(' ', str.strip(item))
            if int(digit) > int(limits[color]):
                add = False
    if add:
        total += int(game)
print(total)
