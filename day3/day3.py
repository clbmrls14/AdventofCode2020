def findTrees(lines, right, down):
    indent = 0
    totalTrees = 0
    skip = down
    for line in lines:
        if skip is not down:
            skip += 1
        else:
            line = line.rstrip('\n')
            if line[indent] == '#':
                totalTrees += 1
            indent += right
            if indent >= len(line):
                indent = indent - len(line)
            skip = 1
    return totalTrees

def day3Part1(lines):
    totalTrees = findTrees(lines, 3, 1)
    return totalTrees

def day3Part2(lines):
    a = findTrees(lines, 1, 1)
    b = findTrees(lines, 3, 1)
    c = findTrees(lines, 5, 1)
    d = findTrees(lines, 7, 1)
    e = findTrees(lines, 1, 2)
    return a*b*c*d*e



def main(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(line)

    file.close()

    print("Part 1:", day3Part1(lines), "total trees")
    print("Part 2:", day3Part2(lines), "is the answer")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/input.txt")