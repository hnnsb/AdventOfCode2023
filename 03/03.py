from collections import defaultdict
import re


with open("03/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))

data.insert(0, "." * len(data[0]))
data.insert(len(data), "." * len(data[0]))
data = ["."+row+"." for row in data]

stars = defaultdict(list)
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if c == "*":
            stars[(r, c)] = []


res = 0
for r, row in enumerate(data):
    for number in re.findall(r"\d+", row):
        isPartNumber = False
        c = data[r].find(number)
        for r_offset in range(r-1, r+2):
            if isPartNumber:
                break
            for c_offset in range(c-1, c + len(number)+1):
                if isPartNumber:
                    break

                neighbor = data[r_offset][c_offset]
                if neighbor != "." and not neighbor.isdigit():
                    isPartNumber = True

                if neighbor == "*":
                    stars[(r_offset, c_offset)].append(int(number))

        if isPartNumber:
            res += int(number)
        data[r] = data[r].replace(number, "."*len(number), 1)

correct = 528799
print("Part 1", res)

ratios = list(filter(lambda x: len(x) == 2, stars.values()))
ratios = [x[0]*x[1] for x in ratios]
print("Part 2", sum(ratios))
