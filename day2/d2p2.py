import re

class Game:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def changeColor(self, color, digit):
        if "red" == color and digit > self.red:
            self.red = digit
        if "green" == color and digit > self.green:
            self.green = digit
        if "blue" == color and digit > self.blue:
            self.blue = digit

    def power(self):
        return self.red * self.green * self.blue

with open("inputd2p1.txt", "r") as f:
    tInput = f.read()
lInput = tInput.split("\n")
total = 0
for line in lInput:
    game, results = re.split(':', line)
    results = re.split(';', results)
    gObj = Game()
    for result in results:
        result = re.split(',', result)
        for item in result:
            digit, color = re.split(' ', str.strip(item))
            gObj.changeColor(color, int(digit))
    total += gObj.power()
print(total)