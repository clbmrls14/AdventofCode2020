def day10Part1(jolts):
    chargers = [int(i) for i in jolts]
    chargers.sort()
    highest_charger = 0
    one_jolt = 0
    three_jolt = 1
    for charger in chargers:
        if charger <= highest_charger + 3:
            diff = highest_charger - charger
            highest_charger = charger
            if abs(diff) == 1:
                one_jolt = one_jolt + 1
            if abs(diff) == 3:
                three_jolt = three_jolt + 1

    return one_jolt * three_jolt

def main(inputFile):
    file = open(inputFile)
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    print("Part 1:", day10Part1(lines), "is your answer")
    # print("Part 2:", day10Part2(lines, bag), "is your answer")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/input.txt")