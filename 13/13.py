import functools


with open("./13/input.txt", "r") as file:
    data = file.read()
data = data.split("\n\n")
data = [x.split() for x in data]

rows = []
cols = []
rows2 = []
cols2 = []


def check_rows(pattern):
    index_sets = []
    for row in pattern:
        indexes = set()
        for c in range(1, len(row)):
            left, right = row[:c], row[c:]
            left = left[::-1]
            mirror = True
            for dc in range(min(len(left), len(right))):
                if left[dc] != right[dc]:
                    mirror = False
                    break
            if mirror:
                indexes.add(c)
        index_sets.append(indexes)

    same = functools.reduce(lambda x, y: x.intersection(y), index_sets)
    if len(same) > 0:
        return same.pop()
    else:
        return 0


def check_rows_2(pattern):
    Rows = len(pattern)
    Cols = len(pattern[0])
    for c in range(Cols-1):
        badness = 0
        for dc in range(Cols):
            left = c-dc
            right = c+1+dc
            if 0 <= left < right < Cols:
                for r in range(Rows):
                    if pattern[r][left] != pattern[r][right]:
                        badness += 1
        if badness == 1:
            return c+1


def transpose(pattern):
    return list(zip(*pattern))


def rotate(pattern):
    reversed = [x[::-1] for x in pattern]
    return transpose(reversed)


for pattern in data:
    rotated_pattern = rotate(pattern)

    row = check_rows(pattern)
    col = check_rows(rotated_pattern)
    cols.append(row)
    rows.append(col)

    row2 = check_rows_2(pattern)
    col2 = check_rows_2(rotated_pattern)
    if row2:
        cols2.append(row2)
    if col2:
        rows2.append(col2)

print(sum(cols)+100*sum(rows))

print(sum(cols2)+100*sum(rows2))
