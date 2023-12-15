from collections import defaultdict


with open("./15/input.txt", "r") as file:
    data = file.read()
data = data.split(",")


def hash(s):
    res = 0
    for c in s:
        ascii = ord(c)
        res += ascii
        res *= 17
        res %= 256
        
    return res
        
res = 0
for s in data:
    assert "\n" not in s
    res += hash(s)
print("Part1:", res)

boxes = defaultdict(list)
for s in data:
    if s[-1] == "-": # Remove lens if exists
        label = s[:-1]
        box = hash(label)
        for i,lens in enumerate(boxes[box]):
            if label == lens[0]:
                boxes[box].pop(i)
    else: # Append or swap lens
        label,focal = s.split("=")
        box = hash(label)
        replaced = False
        for i,lens in enumerate(boxes[box]):
            if label == lens[0]:
                boxes[box][i] = (label, focal)
                replaced = True
        if not replaced:
            boxes[box].append((label, focal))

ans = 0
for k,v in boxes.items():
    for j, lens in enumerate(v):
        ans += (k+1)*(j+1)*int(lens[-1])     

print("Part2:", ans)
