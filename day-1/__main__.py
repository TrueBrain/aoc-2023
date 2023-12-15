

with open("day-1/input") as f:
    lines = f.readlines()

total = 0
part2 = True

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in lines:
    first = None
    last = None

    if part2:
        # Go from left to right; if you find a numeric, stop.
        # If you find a word that represents a digit, replace it with the digit, and stop.
        for pos in range(len(line)):
            if line[pos].isnumeric():
                break

            for word, digit in digits.items():
                if line[pos:].startswith(word):
                    line = line[:pos] + str(digit) + line[pos + len(word) :]
                    break
            else:
                continue

            break

        # Go from right to left; if you find a numeric, stop.
        # If you find a word that represents a digit, replace it with the digit, and stop.
        for pos in range(len(line) - 1, -1, -1):
            if line[pos].isnumeric():
                break

            for word, digit in digits.items():
                if line[pos:].startswith(word):
                    line = line[:pos] + str(digit) + line[pos + len(word) :]
                    break
            else:
                continue

            break

    for c in line:
        if not c.isnumeric():
            continue

        last = int(c)

        if first is None:
            first = int(c)

    number = first * 10 + last
    total += number

print(total)
