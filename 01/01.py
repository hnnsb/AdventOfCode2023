import re

with open("01/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))
data = [re.findall(r"\d", x) for x in data]
data = [x[0]+x[-1] for x in data]

print(sum(map(int, data)))

with open("01/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))

digit_strings = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r",
                 "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

for idx, line in enumerate(data):
    current = line
    for key in digit_strings.keys():
        current = current.replace(key, digit_strings[key])
    data[idx] = current

data = [re.findall(r"\d", x) for x in data]
data = [x[0]+x[-1] for x in data]
print(sum(map(int, data)))
