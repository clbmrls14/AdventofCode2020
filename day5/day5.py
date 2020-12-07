def getSeatId(ticket):
    lower = 0
    upper = 128
    for element in range(7):
        half = (upper - lower) / 2
        if ticket[element] == 'F':
            upper = upper - half
        else:
            lower = lower + half
        row = lower
    lower = 0
    upper = 8
    for element in range(7, 10):
        half = (upper - lower) / 2
        if ticket[element] == 'R':
            lower = lower + half
        else:
            upper = upper - half
        column = upper - 1
    seatID = row * 8 + column
    return seatID

def day5Part1(lines):
    seatIDs = []
    for line in lines:
        seatIDs.append(getSeatId(line))
    return max(seatIDs)

def day5Part2(lines):
    seatIDs = []
    for line in lines:
        seatIDs.append(getSeatId(line))
    iterator = min(seatIDs)
    for seat in sorted(seatIDs):
        if seat != iterator:
            return seat - 1
        iterator = iterator + 1
    return "uh oh"

def main(inputFile):
    file = open(inputFile)
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)
    file.close()

    print("Part 1:", day5Part1(lines), "is the highest seat ID")
    print("Part 2:", day5Part2(lines), "is your seat ID")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/input.txt")