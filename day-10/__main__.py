
with open("day-10/input") as fp:
    lines = fp.readlines()

width = len(lines[0].strip())
height = len(lines)

def find_start():
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "S":
                return (x, y)

# The shape of each tile, in a 3x3 matrix.
# This indicates the parts that are solid, and cannot be flooded.
tiles = {
    "-": [
        (0, 1),
        (1, 1),
        (2, 1),
    ],
    "|": [
        (1, 0),
        (1, 1),
        (1, 2),
    ],
    "7": [
        (0, 1),
        (1, 1),
        (1, 2),
    ],
    "J": [
        (1, 0),
        (1, 1),
        (0, 1),
    ],
    "L": [
        (1, 0),
        (1, 1),
        (2, 1),
    ],
    "F": [
        (2, 1),
        (1, 1),
        (1, 2),
    ],
}

def update_matrix(x, y, tile):
    for dx, dy in tiles[tile]:
        matrix[y * 3 + dy][x * 3 + dx] = 1

def follow(x, y, last):
    lx, ly = last

    update_matrix(x, y, lines[y][x])

    if lines[y][x] == "-":
        if x > lx:
            return (x + 1, y)
        return (x - 1, y)
    if lines[y][x] == "|":
        if y > ly:
            return (x, y + 1)
        return (x, y - 1)
    if lines[y][x] == "7":
        if x > lx:
            return (x, y + 1)
        return (x - 1, y)
    if lines[y][x] == "J":
        if x > lx:
            return (x, y - 1)
        return (x - 1, y)
    if lines[y][x] == "L":
        if x < lx:
            return (x, y - 1)
        return (x + 1, y)
    if lines[y][x] == "F":
        if x < lx:
            return (x, y + 1)
        return (x + 1, y)

    raise Exception("Failed to follow path")

(start_x, start_y) = find_start()
last = (start_x, start_y)

# The matrix creates a 3x3 per tile, which is used for flooding.
matrix = [[0 for x in range(width * 3)] for y in range(height * 3)]

right = False
left = False
top = False
bottom = False

if lines[start_y][start_x + 1] in ("-", "7", "J"):
    right = True
    x, y = (start_x + 1, start_y)
if lines[start_y][start_x - 1] in ("-", "L", "F"):
    left = True
    x, y = (start_x - 1, start_y)
if lines[start_y + 1][start_x] in ("|", "L", "J"):
    bottom = True
    x, y = (start_x, start_y + 1)
if lines[start_y - 1][start_x] in ("|", "7", "F"):
    top = True
    x, y = (start_x, start_y - 1)

if right and top:
    update_matrix(start_x, start_y, "L")
elif right and bottom:
    update_matrix(start_x, start_y, "F")
elif left and top:
    update_matrix(start_x, start_y, "J")
elif left and bottom:
    update_matrix(start_x, start_y, "7")
elif left and right:
    update_matrix(start_x, start_y, "-")
elif top and bottom:
    update_matrix(start_x, start_y, "|")
else:
    raise Exception("Failed to find start tile")

steps = 1
while True:
    nx, ny = follow(x, y, last)
    last = (x, y)
    (x, y) = (nx, ny)

    steps += 1

    if (x, y) == (start_x, start_y):
        break

print(f"Part 1: {steps // 2}")

flooding = set()

def flood(x, y):
    if x > 0 and matrix[y][x - 1] == 0:
        matrix[y][x - 1] = 2
        flooding.add((x - 1, y))

    if x < width * 3 - 1 and matrix[y][x + 1] == 0:
        matrix[y][x + 1] = 2
        flooding.add((x + 1, y))

    if y > 0 and matrix[y - 1][x] == 0:
        matrix[y - 1][x] = 2
        flooding.add((x, y - 1))

    if y < height * 3 - 1 and matrix[y + 1][x] == 0:
        matrix[y + 1][x] = 2
        flooding.add((x, y + 1))

# Flood from the borders.
for y in range(height * 3):
    if matrix[y][0] == 0:
        flooding.add((0, y))
    if matrix[y][width * 3 - 1] == 0:
        flooding.add((width * 3 - 1, y))
for x in range(width * 3):
    if matrix[0][x] == 0:
        flooding.add((x, 0))
    if matrix[height * 3 - 1][x] == 0:
        flooding.add((x, height * 3 - 1))

# Keep on flooding as long as we have something to flood.
while flooding:
    x, y = flooding.pop()
    matrix[y][x] = 2
    flood(x, y)

# Find out what FULL tiles (so a 3x3) are not flooded; those are internal tiles.
closed = 0
for y in range(0, height * 3, 3):
    for x in range(0, width * 3, 3):
        if matrix[y][x] == 0 and matrix[y + 1][x] == 0 and matrix[y + 2][x] == 0 and matrix[y][x + 1] == 0 and matrix[y + 1][x + 1] == 0 and matrix[y + 2][x + 1] == 0 and matrix[y][x + 2] == 0 and matrix[y + 1][x + 2] == 0 and matrix[y + 2][x + 2] == 0:
            closed += 1

print(f"Part 2: {closed}")
