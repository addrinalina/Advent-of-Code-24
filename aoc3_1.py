#https://adventofcode.com/2024/day/3

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input3.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

result = 0

for line in x:
    matches = re.findall(pattern, line)

    for pair in matches:
        print(f"multiply {pair[0]}*{pair[1]}")
        result += int(pair[0])*int(pair[1])
    print(matches)
    
print(f"Result = {result}")