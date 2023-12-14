from collections import Counter
import copy


with open("./14/input.txt", "r") as file:
    data = file.read()
data = data.split("\n")
data = [[c for c in x]for x in data]


def print_field(field):
    for row in field:
        print("".join(row))


def roll(field, dir: tuple):
    """
        dir: (-1, 0): north,
             ( 0,-1): west
    """
    R = len(field)
    C = len(field[0])
    dir_r, dir_c = dir
    r_range = range(R) if dir_r <= 0 else range(R-1, -1, -1)
    c_range = range(C) if dir_c <= 0 else range(C-1, -1, -1)
    for r in r_range:
        for c in c_range:
            if field[r][c] == 'O':
                field[r][c] = '.'
                dr = 0
                dc = 0
                while 0 <= c+dc < C and 0 <= r+dr < R and field[r+dr][c+dc] == ".":
                    dr += dir_r
                    dc += dir_c

                field[r+dr-dir_r][c+dc-dir_c] = 'O'

    return field


def calc_load(field):
    res = 0
    for i, row in enumerate(field):
        rocks = Counter(row)['O']
        res += (len(field)-i)*rocks
    return res


def part1():
    rolled = roll(copy.deepcopy(data), (-1, 0))
    print(calc_load(rolled))


def part2():
    seen = {}
    field = copy.deepcopy(data)
    i = 0
    T = 1e9
    while i < T:
        for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            field = roll(field, dir)

        field_t = tuple(tuple(row) for row in field)
        if field_t in seen:
            dur = i - seen[field_t]
            amount = (T-i)//dur
            i += amount * dur
        else:
            seen[field_t] = i
        i += 1

    print(calc_load(field))


if __name__ == "__main__":
    part1()
    part2()
