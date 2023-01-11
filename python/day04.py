file = open('../puzzle_inputs/day01.txt','r',encoding="utf-8")

for line in file:
   pair = line.split(",")
   pair1 = pair[0].split("-")
   pair2 = pair[1].split("-")
   le1 = pair1[0]
   le2 = pair1[1]
   re1 = pair2[0]
   re2 = pair2[1]
   print(le1,le2,re1,re2)
