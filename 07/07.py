from collections import Counter
import functools


with open("07/input.txt") as file:
    data = file.readlines()
data = list(map(lambda x: x.strip(), data))
data = [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]

card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_order2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def find_hand1(s: str):
    hand = Counter(s)
    c = sorted(hand.values(), reverse=True)
    if c[0] >= 4:  # Five or Four of a kind
        return c[0]+1
    elif c[0] == 3 and c[1] == 2:  # Full house
        return 4
    elif c[0] == 3:  # Three of a kind
        return 3
    elif c[0] == 2 and c[1] == 2:  # Two Pair
        return 2
    elif c[0] == 2:  # Pair
        return 1
    else:
        return 0


def find_hand2(s: str):
    hand = Counter(s)
    j = hand["J"]
    del hand["J"]
    c = sorted(hand.values(), reverse=True)

    if j == 5:
        return j+1
    if c[0]+j >= 4:  # Five or Four of a kind
        return c[0]+j+1
    elif c[0]+j == 3 and c[1] == 2:  # Full House
        return 4
    elif c[0]+j == 3:
        return 3
    elif c[0] == 2 and c[1] == 2:
        return 2
    elif c[0]+j == 2:
        return 1
    else:
        return 0


def sort_hand(find_func, card_order, x, y):
    # If it returns a positive number: x > y
    # If it returns 0: x == y
    # If it returns a negative number: x < y
    value_x = find_func(x[0])
    value_y = find_func(y[0])

    if value_x != value_y:
        return value_x - value_y
    for c1, c2 in zip(x[0], y[0]):
        x1 = card_order.index(c1)
        x2 = card_order.index(c2)
        if x1 == x2:
            continue
        return x1-x2


ranks = sorted(data, key=functools.cmp_to_key(
    functools.partial(sort_hand, find_hand1, card_order)))
res1 = sum([x[1]*(idx+1) for idx, x in enumerate(ranks)])
print(res1)

ranks = sorted(data, key=functools.cmp_to_key(
    functools.partial(sort_hand, find_hand2, card_order2)))
res2 = sum([x[1]*(idx+1) for idx, x in enumerate(ranks)])
print(res2)
