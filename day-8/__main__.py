part2 = True

with open("day-8/input") as fp:
    lines = fp.readlines()

route = lines[0].strip()

pathing = {}
for line in lines[2:]:
    node, _, paths = line.strip().partition("=")
    node = node.strip()

    left, _, right = paths.strip().partition(",")
    left = left[1:].strip()
    right = right[:-1].strip()

    pathing[node] = (left, right)

if not part2:
    nodes = ["AAA"]
else:
    nodes = [node for node in pathing.keys() if node[-1] == "A"]

# After some analysis, it turns out every start-node takes exactly a multiplier
# of the length of the route to get to the end node, and the multiplier is always
# a prime number. Which means that the only time they all are at an end node, is
# the multiplier of all prime numbers.

cycles = []

total = 1
for node in nodes:
    index = 0
    while node[-1] != "Z":
        if route[index % len(route)] == "L":
            node = pathing[node][0]
        else:
            node = pathing[node][1]

        index += 1

    total *= index // len(route)

print(total * len(route))
