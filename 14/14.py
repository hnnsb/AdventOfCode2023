from collections import Counter
import copy
from functools import cache
from typing import Literal


with open("./14/test.txt", "r") as file:
    data = file.read()
data = data.split("\n")
data = [[c for c in x]for x in data]

def roll_NS(field, dir:Literal["N","S"]):
    if dir =="S":
        field = field[::-1]
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] != 'O':
                continue
            
            dr = 1
            moved = False
            while r - dr >= 0 and field[r - dr][c] == '.':
                dr += 1
                moved = True
            if moved:
                field[r][c] = '.'
                field[r-dr+1][c] = 'O'
    return field[::-1] if dir == "S" else field

def roll_EW(field, dir:Literal["E", "W"]):
    if dir =="E":
        field = [row[::-1] for row in field]
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] != 'O':
                continue
            
            dc = 1
            moved = False
            while c - dc >= 0 and field[r][c-dc] == '.':
                dc += 1
                moved = True
            if moved:
                field[r][c] = '.'
                field[r][c-dc+1] = 'O'
    return [row[::-1] for row in field] if dir == "E" else field

 
def calc_load(field):
    res = 0   
    for i, row in enumerate(field):
        rocks = Counter(row)['O']
        res += (len(field)-i)*rocks
    return res


rolled = roll_NS(copy.deepcopy(data), "N")
print(calc_load(rolled))

positions_in_cycle = []
field = copy.deepcopy(data)
prev = copy.deepcopy(field)
for i in range(100):
        if i%1000 ==0:
            print(i, i/1_000_000_000)
        field = roll_NS(field, "N")
        field = roll_EW(field, "W")
        field = roll_NS(field, "S")
        field = roll_EW(field, "E")

        # print(i, calc_load(field))
        # continue

        positions = {(r,c) for r,row in enumerate(field) for c,col in enumerate(row) if col == "O"}
        if positions in positions_in_cycle:
            print(i)
            print(i+1_000_000_000%i)
            break
        else:
            positions_in_cycle.append(positions)
