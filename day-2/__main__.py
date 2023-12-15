
with open("day-2/input") as fp:
    lines = fp.readlines()

total = 0
power = 0

for line in lines:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    game, _, raw_reveals = line.strip().partition(":")
    game = int(game.strip()[5:])

    max_colors = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }

    raw_reveals = raw_reveals.strip().split(";")
    for raw_reveal in raw_reveals:
        raw_colors = raw_reveal.strip().split(",")
        for raw_color in raw_colors:
            count, _, color = raw_color.strip().partition(" ")
            count = int(count)

            if max_colors[color] < count:
                max_colors[color] = count

    if max_colors["blue"] <= 14 and max_colors["red"] <= 12 and max_colors["green"] <= 13:
        total += game

    power += max_colors["blue"] * max_colors["red"] * max_colors["green"]

print(f"Part 1: {total}")
print(f"Part 2: {power}")
