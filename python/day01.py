
## Solves part one of the day 1 problem. Opens the file with the calories 

file = open('../puzzle_inputs/day01.txt','r',encoding="utf-8")
elves = []
elf = []
totals = []
for line in file:
    if line != '\n' :
        elf.append(int(line))
    else:
        elves.append(elf)
        elf = []

for elf in elves:
    totals.append(sum(elf))

## Solves part two.

totals.sort(reverse=True)
print(totals[0:3])
print(sum(totals[0:3]))
