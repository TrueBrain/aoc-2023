
part2 = True

with open("day-6/input") as fp:
    lines = fp.readlines()

if not part2:
    times = [int(time.strip()) for time in lines[0].strip().split(":")[1].split(" ") if time.strip() != ""]
    distances = [int(distance.strip()) for distance in lines[1].strip().split(":")[1].split(" ") if distance.strip() != ""]
else:
    times = [int(lines[0].strip().split(":")[1].replace(" ", ""))]
    distances = [int(lines[1].strip().split(":")[1].replace(" ", ""))]

total = 1
for i, distance in enumerate(distances):
    ways = 0

    for t in range(times[i]):
        new_d = t * (times[i] - t)
        if new_d > distance:
            ways += 1

    total *= ways

print(f"Part 1: {total}")
