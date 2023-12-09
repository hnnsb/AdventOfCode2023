import re

# Time:        45     97     72     95
# Distance:   305   1062   1110   1695

races1 = [(7,9), (15,40), (30, 200)]
races1 = [(45,305), (97,1062), (72, 1110), (95,1695)]

race2 = (71530, 940200)
race2 = (45977295, 305106211101695)

res = 1
for race in races1:
    length, high = race
    hold = []
    for speed in range(length+1):
        score = speed * (length-speed)
        if score > high:
            hold.append(speed)
    res *= len(hold)

print(res)

res=0
length, high = race2
for speed in range(length+1):
    score = speed*(length-speed)
    if score > high:
        res+=1

print(res)