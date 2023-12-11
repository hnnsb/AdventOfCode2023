import itertools
import numpy as np

with open("11/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))
data = [list(x) for x in data]
universe = np.array(data)

empty_rows = [i for i,row in enumerate(universe) if '#' not in row]
empty_cols = [j for j in range(len(universe[0,:])) if '#' not in universe[:,j]]


galaxies = np.where(universe == "#")
galaxies = list(zip(galaxies[0],galaxies[1]))

def l1_norm(a,b):
    return sum(abs(a[i]-b[i]) for i in range(2))

for space in [1,1000000]:
    distances= []
    for a,b in itertools.combinations(galaxies, 2):
        d = l1_norm(a,b)
        for i in empty_rows:
            assert a!=b
            if a[0] < i < b[0] or b[0] < i < a[0]:
                d+=space-1
                
        for j in empty_cols:
            if a[1] < j < b[1] or b[1] < j < a[1]:
                d+=space-1
                
        distances.append(d)

    print(sum(distances))