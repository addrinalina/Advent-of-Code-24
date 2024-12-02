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

print("left", leftlist)
print("right", rightlist)

similarity = []

for digit in leftlist:
    times = rightlist.count(digit)
    similarity.append(abs(digit*times))
print('Similarity', similarity, sum(similarity))