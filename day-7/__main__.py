from collections import defaultdict

part2 = True

with open("day-7/input") as fp:
    lines = fp.readlines()

CARD_RANK = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

if part2:
    CARD_RANK["J"] = 1

def score_hand(hand):
    shand = defaultdict(lambda: 0)
    for h in hand:
        shand[h] += 1

    js = shand["J"] if part2 else 0
    if part2 and js:
        del shand["J"]

    score = 0
    if (5 - js) in shand.values() or js == 5:  # Five of a kind
        score |= 7 << 24
    elif (4 - js) in shand.values():  # Four of a kind
        score |= 6 << 24
    elif js == 1 and list(shand.values()).count(2) == 2:  # Full house with Joker
        score |= 5 << 24
    elif 3 in shand.values() and 2 in shand.values():  # Full house
        score |= 5 << 24
    elif (3 - js) in shand.values():  # Three of a kind
        score |= 3 << 24
    elif list(shand.values()).count(2) == 2:  # Two pairs
        score |= 2 << 24
    elif (2 - js) in shand.values():  # One pair
        score |= 1 << 24

    score |= CARD_RANK[hand[0]] << 16
    score |= CARD_RANK[hand[1]] << 12
    score |= CARD_RANK[hand[2]] << 8
    score |= CARD_RANK[hand[3]] << 4
    score |= CARD_RANK[hand[4]]

    return score

hands = {}
for line in lines:
    hand, _, bid = line.strip().partition(" ")

    hands[hand] = int(bid)

rank = 1
total = 0
for hand in sorted(hands.items(), key=lambda x: score_hand(x[0])):
    total += hand[1] * rank
    rank += 1

print(total)
