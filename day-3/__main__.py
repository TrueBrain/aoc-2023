
part2 = True

lines = []
with open("day-3/input") as fp:
    for line in fp:
        lines.append(line.strip())

width = len(lines[0])
height = len(lines)

gears = {}

# Create a mask of all places that are adjacent to a symbol.
mask = [[False for _ in range(width + 2)] for _ in range(height + 2)]
for y in range(height):
    for x in range(width):
        if lines[y][x].isnumeric() or lines[y][x] == ".":
            continue

        mx = x + 1
        my = y + 1

        gear = True
        if lines[y][x] == "*":
            gear = (mx, my)

        mask[my - 1][mx - 1] = gear
        mask[my - 1][mx] = gear
        mask[my - 1][mx + 1] = gear
        mask[my][mx - 1] = gear
        mask[my][mx] = gear
        mask[my][mx + 1] = gear
        mask[my + 1][mx - 1] = gear
        mask[my + 1][mx] = gear
        mask[my + 1][mx + 1] = gear

        if gear is not True:
            gears[gear] = []

adjacent = False
number = 0
total = 0
for y in range(height):
    for x in range(width):
        if lines[y][x].isnumeric():
            adjacent = adjacent or mask[y + 1][x + 1]
            number = number * 10 + int(lines[y][x])
        elif number != 0 or adjacent:
            if adjacent:
                total += number
                if adjacent is not True:
                    gears[adjacent].append(number)
            adjacent = False
            number = 0

    if number != 0 or adjacent:
        if adjacent:
            total += number
            if adjacent is not True:
                gears[adjacent].append(number)
        adjacent = False
        number = 0

ratio = 0
for gear in gears:
    if len(gears[gear]) != 2:
        continue

    ratio += gears[gear][0] * gears[gear][1]

print(f"Part 1: {total}")
print(f"Part 2: {ratio}")
