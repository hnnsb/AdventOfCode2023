import sys

sys.setrecursionlimit(int(1e9))

with open("./18/input.txt", "r") as file:
    data = file.readlines()
data = [x.strip().split() for x in data]
data = [tuple([x[0],int(x[1]), x[2]]) for x in data]
dir2coor = {"U":(-1,0), "R":(0,1), "D":(1,0), "L":(0,-1)}

trench = {(0,0)}

r,c = 0,0
for dir, length, color in data:
    dr,dc = dir2coor[dir]
    for i in range(length):
        r, c = r+dr, c+dc
        trench.add((r,c))       


def fill(pos):
    r,c = pos
    for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
        rr,cc = r+dr,c+dc
        if (rr,cc) not in trench:
            trench.add((rr,cc))
            fill((rr,cc))

fill((1,1))
print("Part 1:", len(trench))



print("Part 2")
num2dir = [(0,1),(1,0),(0,-1),(-1,0)]
path = [(0,0)]
r,c = 0,0
edges = 0
for _, _, color in data:
    length, dir =int(color[2:-2], base=16), int(color[-2])
    dr,dc = num2dir[dir]

    r, c = r+dr*length, c+dc*length
    edges+= length
    path.append((r,c))
        
path.append(path[0])
res = 0
for i,a in enumerate(path[:-1]):
    x_1,y_1 = a
    x_2,y_2 = path[i+1]
    res += x_1*y_2-y_1*x_2
    
print(int((abs(res)+edges)/2+1)) #+1 for the start