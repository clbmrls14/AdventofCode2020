


def main(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(line)

    file.close()

    # print("Part 1:", day3Part1(lines), "valid passwords")
    # print("Part 2:", day3Part2(lines), "valid passwords")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/sampleInput.txt")