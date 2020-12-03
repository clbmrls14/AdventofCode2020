def day2Part1(lines):
    validPasswords = 0
    for line in lines:
        x = line.split()

        minMax = x[0].split('-')
        minimum = int(minMax[0])
        maximum = int(minMax[1])

        character = x[1]
        character = character[:-1]

        password = x[2]

        numOccurences = password.count(character)
        if (numOccurences >= minimum) and (numOccurences <= maximum):
            validPasswords += 1

    return validPasswords

def day2Part2(lines):
    validPasswords = 0
    for line in lines:
        x = line.split()

        locations = x[0].split('-')
        first = int(locations[0])
        second = int(locations[1])

        character = x[1]
        character = character[:-1]

        password = x[2]

        if ((password[first-1] is character) and (password[second-1] is not character)) or ((password[first-1] is not character) and (password[second-1] is character)):
            validPasswords += 1

    return validPasswords


def main(inputFile):
    file = open(inputFile)

    lines = []
    for line in file:
        lines.append(line)

    file.close()

    # print("Part 1:", day2Part1(lines), "valid passwords")
    print("Part 2:", day2Part2(lines), "valid passwords")

print("Advent of Code: Day 1")
print("Caleb Morales - clbmrls14")
main("input/input.txt")