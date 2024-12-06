#https://adventofcode.com/2024/day/4

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input4.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

import re, numpy
count = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        if x[i][j]=="A" and (i>=1 and j>=1 and (i+1)<len(x) and (j+1)<len(x[0])):
            if (x[i-1][j-1]=="M" and x[i+1][j+1]=="S") and ((x[i-1][j+1]=="M" and x[i+1][j-1]=="S") or (x[i-1][j+1]=="S" and x[i+1][j-1]=="M")):
                print(f"X-MAS en x[{i},{j}]")
                count += 1
            elif (x[i+1][j-1]=="M" and x[i-1][j+1]=="S") and ((x[i-1][j-1]=="M" and x[i+1][j+1]=="S") or (x[i-1][j-1]=="S" and x[i+1][j+1]=="M")):
                print(f"X-MAS en x[{i},{j}]")
                count += 1
            elif (x[i+1][j+1]=="M" and x[i-1][j-1]=="S") and ((x[i-1][j+1]=="M" and x[i+1][j-1]=="S") or (x[i-1][j+1]=="S" and x[i+1][j-1]=="M")):
                print(f"X-MAS en x[{i},{j}]")
                count += 1
            elif (x[i-1][j+1]=="M" and x[i+1][j-1]=="S") and ((x[i+1][j+1]=="M" and x[i-1][j-1]=="S") or (x[i+1][j+1]=="S" and x[i-1][j-1]=="M")):
                print(f"X-MAS en x[{i},{j}]")
                count += 1

print(f"Count = {count}")
