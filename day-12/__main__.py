import functools

part2 = False

with open("day-12/input") as fp:
    lines = fp.readlines()

@functools.cache
def calculate_arrangements(springs, markers, current=0):
    # End of the string.
    if not springs:
        assert(current == 0)
        # If there are any markers left, this is an invalid arrangement; otherwise, it's valid.
        return 0 if markers else 1

    b1 = 0
    b2 = 0

    if springs[0] in "#?":
        if not markers or current == markers[0]:
            # Active group that will now grow too large. This is not a valid arrangement.
            b1 = 0
        else:
            b1 = calculate_arrangements(springs[1:], markers, current + 1)

    if springs[0] in ".?":
        if current == 0:
            # No group active.
            b2 = calculate_arrangements(springs[1:], markers, 0)
        elif current != markers[0]:
            # We cannot end a group if it doesn't match the marker. This is not a valid arrangement.
            b2 = 0
        else:
            # We can end a group here.
            b2 = calculate_arrangements(springs[1:], markers[1:], 0)

    return b1 + b2

part1 = 0
part2 = 0
debug = {}
for i, line in enumerate(lines):
    raw_springs, _, raw_markers = line.strip().partition(" ")
    markers = tuple([int(marker) for marker in raw_markers.split(",")])

    print(i, raw_springs, markers)

    first = calculate_arrangements(raw_springs + ".", markers)
    second = calculate_arrangements("?".join([raw_springs] * 5) + ".", markers * 5)

    part1 += first
    part2 += second

    print("-----", i, raw_springs, raw_markers, first, second)
    debug[i] = first

print(f"Part 1: {part1}")
print(f"Part 1: {part2}")
