def getGroupEntries(lines):
    entry = ""
    entries = []
    for line in lines:
        if line:
            entry += line + " "
        else:
            entries.append(entry)
            entry = ""
    entries.append(entry)
    return entries

def removeDuplicates(score):
    responses = []
    for character in score:
        if character not in responses:
            responses.append(character)
    if ' ' in responses:
        responses.remove(' ')
    return responses

def day6Part1(lines):
    scores = getGroupEntries(lines)
    numAnswers = 0
    for score in scores:
        answers = removeDuplicates(score)
        numAnswers = numAnswers + len(answers)
    return numAnswers

def getConsensus(groupScores):
    groupSize = len(groupScores)
    if groupSize is 1:
        return [char for char in groupScores[0]]
    consensus = []
    scoresString = ('').join(groupScores)
    for char in groupScores[0]:
        if scoresString.count(char) is groupSize:
            consensus.append(char)
    return consensus

def day6Part2(lines):
    scores = getGroupEntries(lines)
    numAnswers = 0
    for score in scores:
        consensus = getConsensus(score.split())
        numAnswers = numAnswers + len(consensus)
    return numAnswers


def main(inputFile):
    file = open(inputFile)
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)
    file.close()

    print("Part 1:", day6Part1(lines), "is your answer")
    print("Part 2:", day6Part2(lines), "is your answer")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/input.txt")