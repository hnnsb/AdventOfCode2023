import re


with open("04/input.txt") as file:
    # with open("04/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))

res = 0
for line in data:
    game, numbers = line.split(":")
    game = int(re.findall(r"\d+", game)[0])
    picks, winning = numbers.split("|")
    picks = re.findall(r"\d+", picks)
    winning = re.findall(r"\d+", winning)
    picks = [int(x) for x in picks]
    winning = [int(x) for x in winning]

    points = 0
    for number in picks:
        if number in winning:
            if points == 0:
                points = 1
            else:
                points *= 2

    res += points

print(res)

with open("04/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))

cards = []
for idx, line in enumerate(data):
    game, numbers = line.split(":")
    game = int(re.findall(r"\d+", game)[0])
    picks, winning = numbers.split("|")
    picks = re.findall(r"\d+", picks)
    winning = re.findall(r"\d+", winning)
    picks = [int(x) for x in picks]
    winning = [int(x) for x in winning]
    cards.append((game, picks, winning))

amount = [1]*len(cards)
for game, picks, winning in cards:

    matches = set(picks).intersection(set(winning))
    score = len(matches)
    for i in range(score):
        amount[game + i] += 1 * amount[game-1]

print(sum(amount))
