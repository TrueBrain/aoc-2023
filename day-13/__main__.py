
with open("day-13/input") as fp:
    lines = fp.readlines()


def find_mirror_line(grid, smudges, offset=0):
    for left in range(len(grid) - 1):
        right = len(grid) - 1

        # Walk inwards, see if the rest of the rows are identical.
        difference = 0
        while left < right:
            difference += sum([1 for a, b in zip(grid[left], grid[right]) if a != b])

            left += 1
            right -= 1

        if left > right and difference == smudges:
            if offset:
                return offset - left
            else:
                return left

    return 0


def find_mirror(grid, smudges):
    rows = grid
    cols = ["".join([row[i] for row in rows]) for i in range(len(rows[0]))]

    r = find_mirror_line(rows, smudges) or find_mirror_line(rows[::-1], smudges, len(rows))
    c = find_mirror_line(cols, smudges) or find_mirror_line(cols[::-1], smudges, len(cols))

    return r, c


def analyze_grid(grid, answer, smudges):
    r, c = find_mirror(grid, smudges)

    answer[0] += r
    answer[1] += c

def analyze_all(smudges):
    total = [0, 0]
    grid = []
    for line in lines:
        if line.strip() == "":
            analyze_grid(grid, total, smudges)
            grid = []
            continue

        grid.append(list(line.strip()))

    analyze_grid(grid, total, smudges)
    return total[0] * 100 + total[1]

print(f"Part 1: {analyze_all(0)}")
print(f"Part 2: {analyze_all(1)}")
