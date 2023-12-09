import re


with open("05/input.txt") as file:
    lines = file.read().splitlines()

data = [] 
sub = []
for x in lines:
    if x == "":
        data.append(sub)
        sub = []
    else:
        sub.append(x)
data.append(sub)
seeds = list(map(int, data[0][0].split(" ")[1:]))
seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = [{},{},{},{},{},{},{}]
for map_data, map_ in zip(data[1:], maps):
    for range_ in map_data[1:]:
        goal, start, length = map(int, range_.split(" "))     
        # range: [start, start + length)
        map_[(start, start + length)] = goal
     
   
locations = []
for seed in seeds:
    val = seed 
    for map_ in maps:
        for key in map_.keys():
            start, end = key
            if val in range(start, end):
                val = map_[key] + val - start
                break
    locations.append(val)

print("Part 1:", min(locations))


locations = []
for idx, (seed_range_start, seed_range_end) in enumerate(seed_ranges):
    print(idx/len(seed_ranges), f"{idx}/{len(seed_ranges)}")
    # Takes too long need to calculate range by range
    for seed in range(seed_range_start, seed_range_end):
        print((seed-seed_range_start)/(seed_range_end-seed_range_start))
        val = seed 
        for map_ in maps:
            for key in map_.keys():
                start, end = key
                if val in range(start, end):
                    val = map_[key] + val - start
                    break
        locations.append(val)

print("Part 2:", min(locations))
            