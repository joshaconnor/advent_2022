
## part 1

file = open('./puzzle_inputs/day03.txt','r',encoding="utf-8")

def score(letter):
    values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return values.find(letter)+1

summation = 0
for line in file:
    length = len(line)
    firstCompartment = line[:int(length/2)]
    secondCompartment = line[int(length/2):]
    common = []
    for letter in firstCompartment:
        if letter in secondCompartment:
            common.append(letter)
    summation = summation + score(common[0])

print(summation)

## part 2

file.close()
file = open('./puzzle_inputs/day03.txt','r',encoding="utf-8")
summation = 0

def compareStrings(elf1,elf2,elf3):
    for letter in elf1:
        if (letter in elf2) and (letter in elf3):
            return letter

i = 0
firstElves = []
secondElves = []
thirdElves = []
for line in file:
    if i == 3:
        i = 0
    if i == 0:
        firstElves.append(line[:-1])
    elif i == 1:
        secondElves.append(line[:-1])
    elif i == 2:
        thirdElves.append(line[:-1])
    i=i+1

for elf1 in firstElves:
    lineNum = firstElves.index(elf1)
    elf2 = secondElves[lineNum]
    elf3 = thirdElves[lineNum]
    summation = summation + score(compareStrings(elf1,elf2,elf3))

print(summation)
