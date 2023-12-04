from functools import reduce

with open("02/input.txt") as file:
    data = file.readlines()

data = [x.split(":") for x in data]
data = [(int(x[0][5:]), x[1].strip().split("; ")) for x in data]


max_dict = {"red": 12, "green": 13, "blue": 14}
sum = 0
for id, game in data:
    possible = True
    for round in game:
        drawn = round.split(", ")
        for c in drawn:
            count_str, color = c.split(" ")
            if max_dict[color] < int(count_str):
                possible = False
                break
        if not possible:
            break
    if possible:
        sum += id

print(sum)

with open("02/input.txt") as file:
    data = file.readlines()

data = [x.split(":") for x in data]
data = [(int(x[0][5:]), x[1].strip().split("; ")) for x in data]
sum = 0
for id, game in data:
    min_dict = {"blue": 0, "red": 0, "green": 0}
    for round in game:
        drawn = round.split(", ")
        for c in drawn:
            count_str, color = c.split(" ")
            min_dict[color] = max(min_dict[color], int(count_str))
    product = reduce(lambda x, y: x*y, min_dict.values())
    sum += product

print(sum)
