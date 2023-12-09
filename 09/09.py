with open("09/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))
data = [[int(y) for y in x.split()] for x in data]


def get_diffs(l):
    return [l[i+1]-x for i, x in enumerate(l) if i+1 < len(l)]


def extrapolate_forwards(seqs):
    seqs = list(reversed(seqs))[1:]
    value = 0
    for seq in seqs:
        value = seq[-1]+value
    return value


def extrapolate_backwards(seqs):
    seqs = list(reversed(seqs))[1:]
    value = 0
    for seq in seqs:
        value = seq[0] - value
    return value


nexts = []
prevs = []
for seq in data:
    cur_seq = seq
    seqs = [cur_seq]
    while any(cur_seq):
        cur_seq = get_diffs(cur_seq)
        seqs.append(cur_seq)

    next = extrapolate_forwards(seqs)
    prev = extrapolate_backwards(seqs)
    prevs.append(prev)
    nexts.append(next)

part1 = sum(nexts)
part2 = sum(prevs)
print("Part 1:", part1)
print("Part 2:", part2)
