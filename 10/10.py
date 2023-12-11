with open("10/input.txt") as file:
    maze = file.readlines()
maze = list(map(lambda x: x.strip(), maze))

for i,row in enumerate(maze):
    maze[i] = "." + row + "."
    
maze.insert(0, "."*len(maze[0]))
maze.append("."*len(maze[0]))

maze = [list(row) for row in maze]

for r,row in enumerate(maze):
    for c, cell in enumerate(row):
        if cell == "S":
            start = (r,c)
  
dir2compass = {(-1,0):"N",(0,-1):"W", (1,0):"S",(0,1):"E"}  
        
type2connection = {
    # | is a vertical pipe connecting north and south.
    "|":{"N":["|","7","F","S"],"E":[],               "S":["|","L","J","S"],"W":[]},
    # - is a horizontal pipe connecting east and west.
    "-":{"N":[],               "E":["-","7","J","S"],"S":[],               "W":["-","L","F","S"]},
    # L is a 90-degree bend connecting north and east.
    "L":{"N":["|","7","F","S"],"E":["-","7","J","S"],"S":[],               "W":[]},
    # J is a 90-degree bend connecting north and west.
    "J":{"N":["|","7","F","S"],"E":[],               "S":[],               "W":["-","L","F","S"]},
    # 7 is a 90-degree bend connecting south and west.
    "7":{"N":[],               "E":[],               "S":["|","L","J","S"],"W":["-","L","F","S"]},
    # F is a 90-degree bend connecting south and east.
    "F":{"N":[],               "E":["-","7","J","S"],"S":["|","L","J","S"],"W":[]},
    # . is ground; there is no pipe in this tile.
    ".":{"N":[],               "E":[],               "S":[],               "W":[]},
    "S":{"N":["|","7","F"],    "E":["-","7","J"],    "S":["|","L","J"],    "W":["-","L","F"]}
}

connections = {# N,E,S,W
    "S":[1,1,1,1],
    # | is a vertical pipe connecting north and south.
    "|":[1,0,1,0],
    # - is a horizontal pipe connecting east and west.
    "-":[0,1,0,1],
    # L is a 90-degree bend connecting north and east.
    "L":[1,1,0,0],
    # J is a 90-degree bend connecting north and west.
    "J":[1,0,0,1],
    # 7 is a 90-degree bend connecting south and west.
    "7":[0,0,1,1],
    # F is a 90-degree bend connecting south and east.
    "F":[0,1,1,0],
    # . is ground; there is no pipe in this tile.
    ".":[0,0,0,0],
}
del connections

def is_connected(a,b, dir):
    r1, c1 = a
    r2, c2 = b
    type_a = maze[r1][c1]
    type_b = maze[r2][c2]
    if type_b in type2connection[type_a][dir]:
        return True
    return False
    

prev = start
count = 0
visited = {start}
path = [start]
run = True
while run:
    for dr,dc in dir2compass.keys():
        next = (prev[0]+dr,prev[1]+dc)
        if next in visited:
            continue
        if next not in visited and is_connected(prev, next, dir2compass[(dr,dc)]):
            visited.add(next)
            path.append(next)
            prev = next
            count += 1
            break
    else:
        run = False
        
print((count+1)/2)

maze2=[[" " for _ in row] for row in maze]
for r,c in path:
    maze2[r][c] = maze[r][c]
    
    