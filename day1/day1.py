def day1Part1(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(int(line))

    file.close()

    for line in lines:
        index = 0
        for x in range(index, len(lines)):
            result = line + lines[x]
            if result == 2020:
                return (line * lines[x])

def day1Part2(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(int(line))

    file.close()

    for line in lines:
        index = 0
        for x in range(index, len(lines)):
            for y in range(index+1, len(lines)):
                result = line + lines[x] + lines[y]
                if result == 2020:
                    print(result)
                    return (line * lines[x] * lines[y])

print("Advent of Code: Day 1")
print("Caleb Morales - clbmrls14")

print("Part 1: ", day1Part1("input.txt"))
print("Part 2: ", day1Part2("input.txt"))