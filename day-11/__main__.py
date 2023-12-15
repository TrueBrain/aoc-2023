
lines = []
with open("day-11/input") as fp:
    for line in fp.readlines():
        lines.append(line.strip())

expansion_y = []
expansion_x = []

for row in lines:
    e = 1 if "#" not in row else 0
    expansion_y.append((expansion_y[-1] if len(expansion_y) else 0) + e)

for x in range(len(lines[0])):
    col = [r[x] for r in lines]
    e = 1 if "#" not in col else 0
    expansion_x.append((expansion_x[-1] if len(expansion_x) else 0) + e)

def calculate_distance(expansion):
    expansion -= 1  # Minus one, as we already have a row/col in the input.

    galaxies = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                galaxies.append((x + expansion_x[x] * expansion, y + expansion_y[y] * expansion))

    total = 0
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i + 1 :]:
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return total

print(f"Part 1: {calculate_distance(2)}")
print(f"Part 2: {calculate_distance(1000000)}")
