
## part 1

file = open('../puzzle_inputs/day02.txt','r',encoding="utf-8")

def compare(x,y):
    if x == 'A':
        if y == 'X': return 3
        elif y == 'Y': return 6
        elif y == 'Z': return 0
    if x == 'B':
        if y == 'X': return 0
        elif y == 'Y': return 3
        elif y == 'Z': return 6
    if x == 'C':
        if y == 'X': return 6
        elif y == 'Y': return 0
        elif y == 'Z': return 3 

## key
## A = X = 1 = Rock
## B = Y = 2 = Paper
## C = Z = 3 = Scissors
## 0 = lost
## 3 = tie
## 6 = win
total = 0

for line in file:
    temp = line.split()
    if temp[1] == 'X': total = total + (1 + compare(temp[0],temp[1]))
    elif temp[1] == 'Y': total = total + (2 + compare(temp[0],temp[1]))
    elif temp[1] == 'Z': total = total + (3 + compare(temp[0],temp[1]))

print(total)

## part 2

file.close()
file = open('../puzzle_inputs/day02.txt','r',encoding="utf-8")

valueMatrix = {
    "A X\n":3,
    "A Y\n":4,
    "A Z\n":8,

    "B X\n":1,
    "B Y\n":5,
    "B Z\n":9,

    "C X\n":2,
    "C Y\n":6,
    "C Z\n":7,

    "A Z":8
    }

total = 0
for line in file:
    total = total + valueMatrix[line]
print(total)
