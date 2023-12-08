from collections import Counter
import functools
from itertools import cycle
import math
with open("08/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))

instr = data[0]

maps = {}
for line in data[2:]:
    key, rest = line.split(" = ")
    left, right = rest[1:4], rest[6:-1]
    maps[key] = (left, right)


def part_one():
    cur = "AAA"
    for i, c in enumerate(cycle(instr), 1):
        choice = int(c == "R")
        cur = maps[cur][choice]

        if cur == "ZZZ":
            break
    return i


print(part_one())


def part_two():
    # Brute force is too slow, because routes end but not simultaneously.
    # Idea: record amount of steps it takes for each start to end. Then calculate the lcm for all amounts.
    cur_2 = [x for x in maps.keys() if x.endswith("A")]
    ends_with_count = []
    for i, c in enumerate(cycle(instr), 1):
        choice = int(c == "R")
        cur_2 = [maps[x][choice] for x in cur_2]
        for cur in cur_2:
            if cur.endswith("Z"):
                ends_with_count.append(i)
                cur_2.remove(cur)
        if cur_2 == []:
            break

    return math.lcm(*ends_with_count)


print(part_two())
