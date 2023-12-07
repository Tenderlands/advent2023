from aocd import get_data
listInput = get_data(day=7, year=2023)

# listInput = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
listInput = listInput.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A").split(
    "\n")
print(listInput)
handDict = {
    "FiveOfAKind": [],
    "FourOfAKind": [],
    "FullHouse": [],
    "ThreeOfAKind": [],
    "TwoPairs": [],
    "OnePair": [],
    "HighCard": [],
}

maxRank = len(listInput)
curRank = maxRank


def determine_type(hand, bid):
    hList = [*hand]
    cardList = {}
    for card in hList:
        if card not in cardList.keys():
            cardList[card] = 1
        else:
            cardList[card] += 1
    numberList = []
    for value in cardList:
        numberList.append(cardList[value])
    numberList.sort(reverse=True)
    handType = ""
    if len(numberList) == 1:
        handType = "FiveOfAKind"
    elif len(numberList) == 2:
        if numberList[0] == 4:
            handType = "FourOfAKind"
        else:
            handType = "FullHouse"
    elif len(numberList) == 3:
        if numberList[0] == 3:
            handType = "ThreeOfAKind"
        else:
            handType = "TwoPairs"
    elif len(numberList) == 4:
        handType = "OnePair"
    elif len(numberList) == 5:
        handType = "HighCard"
    handDict[handType].append({"hand": hand, "bid": bid, "rank": 0})

total = 0
def sort_by_high_card(type):
    global curRank, total
    handDict[type] = sorted(handDict[type], key=lambda x: x["hand"], reverse=True)
    for item in handDict[type]:
        item['rank'] = curRank
        total += curRank*int(item["bid"])
        curRank -= 1


for line in listInput:
    hand, bid = line.split()
    determine_type(hand, bid)
print(handDict)

for key in handDict:
    sort_by_high_card(key)
print(handDict)
print(total)
