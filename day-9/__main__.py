
with open("day-9/input") as fp:
    lines = fp.readlines()

def diff_array(numbers):
    return [numbers[n + 1] - numbers[n] for n in range(0, len(numbers) - 1)]


total_next = 0
total_prev = 0
for line in lines:
    diffs = {
        0: [int(v) for v in line.strip().split(" ")],
    }

    i = 1
    while True:
        diffs[i] = diff_array(diffs[i - 1])
        if all([d == 0 for d in diffs[i]]):
            break
        i += 1

    for i in range(i, 0, -1):
        diffs[i - 1].append(diffs[i - 1][-1] + diffs[i][-1])
        diffs[i - 1].insert(0, diffs[i - 1][0] - diffs[i][0])

    total_next += diffs[0][-1]
    total_prev += diffs[0][0]

print(f"Part 1: {total_next}")
print(f"Part 2: {total_prev}")
