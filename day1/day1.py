def day1Part1(lines):
    for line in lines:
        index = 0
        for x in range(index, len(lines)):
            result = line + lines[x]
            if result == 2020:
                return (line * lines[x])

def day1Part2(lines):
    for line in lines:
        index = 0
        for x in range(index, len(lines)):
            for y in range(index+1, len(lines)):
                result = line + lines[x] + lines[y]
                if result == 2020:
                    return (line * lines[x] * lines[y])

def main(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(int(line))

    file.close()

    print("Part 1: ", day1Part1(lines))
    print("Part 2: ", day1Part2(lines))

print("Advent of Code: Day 1")
print("Caleb Morales - clbmrls14")
main("input.txt")
