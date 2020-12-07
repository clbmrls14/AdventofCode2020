import re

class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = int(byr)
        self.iyr = int(iyr)
        self.eyr = int(eyr)
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
    
    def isValidHeight(self):
        if "cm" in self.hgt:
            if 150 <= int(self.hgt.replace('cm', '')) <= 193:
                return True
        elif "in" in self.hgt:
            if 59 <= int(self.hgt.replace('in', '')) <= 76:
                return True
        else:
            return False

    def isValid(self):
        validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if (1920 <= self.byr <= 2002
            and 2010 <= self.iyr <= 2020
            and 2020 <= self.eyr <= 2030
            and self.isValidHeight()
            and re.match(r"^#[a-f0-9]{6}", self.hcl)
            and self.ecl in validEyeColors
            and re.match(r"^[0-9]{9}", self.pid)):
            return True
        else:
            return False

def buildPassport(entry):
    params = {}
    for item in entry.split():
        [field, value] = item.split(':')
        params[field] = value
    return Passport(**params)

def validFields(entry):
    if ("byr:" in entry) and ("iyr:" in entry) and ("eyr:" in entry) and ("hgt:" in entry) and ("hcl:" in entry) and ("ecl:" in entry) and ("pid:" in entry):
        return True 
    else:
        return False

def getEntries(lines):
    entry = ""
    entries = []
    for line in lines:
        if line:
            entry += line + " "
        else:
            if validFields(entry):
                entries.append(entry)
            entry = ""
    return entries

def day4Part1(lines):
    return len(getEntries(lines)) + 1

def day4Part2(lines):
    entries = getEntries(lines)
    passports = [buildPassport(entry) for entry in entries]
    validPassports = [passport for passport in passports if passport.isValid()]
    return len(validPassports)

def main(inputFile):
    file = open(inputFile)
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)
    file.close()

    print("Part 1:", day4Part1(lines), "valid passports")
    print("Part 2:", day4Part2(lines), "valid passports")

print("Advent of Code: Day 3")
print("Caleb Morales - clbmrls14")
main("input/input.txt")