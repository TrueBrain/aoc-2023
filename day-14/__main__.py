import copy

with open("day-14/input") as fp:
    lines = fp.readlines()

def rotate_counterclock(grid):
    return [[row[len(grid[0]) - i - 1] for row in grid] for i in range(len(grid[0]))]

def roll_rocks(grid):
    for row in grid:
        rocks = 0
        for l, r in enumerate(row):
            if r == "#":
                rocks = l + 1

            if r == "O":
                row[l] = row[rocks]
                row[rocks] = "O"
                rocks += 1

def calculate_load(grid):
    load = 0
    for i, row in enumerate(grid):
        load += row.count("O") * (len(grid) - i)

    return load

def do_cycle(grid):
    # North
    grid = rotate_counterclock(grid)
    roll_rocks(grid)
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)

    # West
    roll_rocks(grid)

    # South
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)
    roll_rocks(grid)
    grid = rotate_counterclock(grid)

    # East
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)
    roll_rocks(grid)
    grid = rotate_counterclock(grid)
    grid = rotate_counterclock(grid)

    return grid

grid = []
for line in lines:
    grid.append(list(line.strip()))

grid = rotate_counterclock(grid)
roll_rocks(grid)
grid = rotate_counterclock(grid)
grid = rotate_counterclock(grid)
grid = rotate_counterclock(grid)

print(f"Part 1: {calculate_load(grid)}")

# Find the moment repetition starts.
seen = {}
for i in range(1000):
    grid = do_cycle(grid)

    sgrid = "".join(["".join(row) for row in grid])
    if sgrid in seen:
        cycle = i - seen[sgrid]
        print(f"Repetition detected after {cycle}!")
        break
    seen[sgrid] = i

goal_cycle = 1000000000 - i - 1
# As this is repetition, doing these cycles doesn't change the outcome.
remaining_cycle = goal_cycle - goal_cycle // cycle * cycle
# Only run the cycles we still have to, ignoring the parts that causes repetition.
for i in range(remaining_cycle):
    grid = do_cycle(grid)

print(f"Part 2: {calculate_load(grid)}")
