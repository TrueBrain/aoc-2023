
with open("day-5/input") as fp:
    lines = fp.readlines()

def map_items(mapping, items):
    new_items = []

    for (isource, ilength) in items:
        iend = isource + ilength - 1

        for source, dest, length in mapping:
            send = source + length - 1
            diff = dest - source

            if isource >= source and iend <= send:
                new_items.append((isource + diff, ilength))
                break

            if source < isource < send:
                new_items.append((isource + diff, source - isource + length))
                isource = source + length
                ilength -= source - isource + length
                continue

            if source < iend < send:
                new_items.append((dest, isource + ilength - source))
                ilength -= source - isource
                continue

        else:
            new_items.append((isource, ilength))

    return new_items


def run_mapping(mappings, items):
    for mapping in mappings:
        items = map_items(mapping, items)
    return items

mappings = []

mapping = []
for line in lines[1:]:
    line = line.strip()

    if line == "":
        continue

    if line.endswith(" map:"):
        mappings.append(mapping)
        mapping = []
        continue

    dest, source, length = line.split(" ")
    mapping.append((int(source), int(dest), int(length)))
mappings.append(mapping)

raw_items = [int(item) for item in lines[0].split(":")[1].strip().split(" ")]

lowest = 2**32
items = run_mapping(mappings, [(item, 1) for item in raw_items])
for item in items:
    lowest = min(lowest, item[0])
print(f"Part 1: {lowest}")

lowest = 2**32
for i in range(0, len(raw_items), 2):
    items = run_mapping(mappings, [(raw_items[i], raw_items[i+1])])
    for item in items:
        lowest = min(lowest, item[0])

print(f"Part 2: {lowest}")
