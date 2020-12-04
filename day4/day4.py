def day4Part1(lines):
    for line in lines:
        line = line.rstrip('\n')
        print(line)
    return "?"

def main(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(line)

    file.close()

    print("Part 1:", day4Part1(lines), "valid passports")
    # print("Part 2:", day4Part2(lines), "is the answer")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/sample_input.txt")