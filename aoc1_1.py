#https://adventofcode.com/2024/day/1

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input1.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
#print(x)

leftlist = []
rightlist = []

for line in x:
    line = line.split()
    leftlist.append(int(line[0]))
    rightlist.append(int(line[1]))

leftlist.sort()
rightlist.sort()

print("left", leftlist)
print("right", rightlist)

resta = []

for i, digit in enumerate(leftlist):
    resta.append(abs(rightlist[i]-leftlist[i]))
print('Resta', sum(resta))

