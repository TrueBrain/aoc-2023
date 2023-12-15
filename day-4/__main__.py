from collections import defaultdict

with open("day-4/input") as fp:
    lines = fp.readlines()

cards = defaultdict(lambda: 1)

total = 0
total_cards = 0
for cardno, line in enumerate(lines):
    card, _, line = line.strip().partition(":")
    raw_winning, _, raw_ours = line.strip().partition("|")

    total_cards += cards[cardno]

    winning = set()
    for number in raw_winning.strip().split(" "):
        if number.strip() == "":
            continue
        number = int(number.strip())

        winning.add(number)

    matches = 0
    for number in raw_ours.strip().split(" "):
        if number.strip() == "":
            continue
        number = int(number.strip())

        if number in winning:
            matches += 1

    if matches > 0:
        total += 2 ** (matches - 1)

        for i in range(matches):
            cards[cardno + i + 1] += cards[cardno]

print(f"Part 1: {total}")
print(f"Part 1: {total_cards}")
