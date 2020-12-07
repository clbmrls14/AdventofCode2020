def day7Part1(lines, bag):
    containers = []
    new_bags = []
    for line in lines:
        if (bag in line) and (line not in containers):
            containers.append(line)
            new_bags.append(' '.join(line.split()[:2]))
    for new_bag in new_bags:
        for line in lines:
            if (new_bag in line) and (line not in containers):
                containers.append(line)
                new_bags.append(' '.join(line.split()[:2]))
    new_bags.remove(bag)
    print(str(new_bags))
    return len(containers)

def day7Part2(lines, bag):
    containers = []
    inner_bags = []
    for line in lines:
        if line.startswith(bag):
            containers.append(line)
            inner_bags.append(' '.join(line.split()[5 : 7]))
            inner_bags.append(' '.join(line.split()[9 : 11]))
    for inner_bag in inner_bags:
        for line in lines:
            if line.startswith(inner_bag):
                if "no other" not in line:
                    containers.append(line)
                    inner_bags.append(' '.join(line.split()[5 : 7]))
                    inner_bags.append(' '.join(line.split()[9 : 11]))
    numbers = []
    for container in containers:
        numbers.append([int(word) for word in container.split() if word.isdigit()])
    flat_numbers = [num for sublist in numbers for num in sublist]

    print(str(containers))
    return sum(flat_numbers)



def main(inputFile):
    file = open(inputFile)
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    bag = "shiny gold"

    # print("Part 1:", day7Part1(lines, bag), "is your answer")
    print("Part 2:", day7Part2(lines, bag), "is your answer")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/sample_input.txt")