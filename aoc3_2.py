#https://adventofcode.com/2024/day/3

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input3.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

import re

pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"

result = 0
valid_mul_expressions = []
last_valid_keyword = "do"

for line in x:
    tokens = re.findall(pattern, line)
    print("Tokens", tokens)

    for token in tokens:
        print(token)
        if token[0] == "do()":
            last_valid_keyword = "do"
        elif token[0] == "don't()":
            last_valid_keyword = "don't"
        elif token[0].startswith("mul") and last_valid_keyword == "do":
            valid_mul_expressions.append(token[0])
            print(f"Multiplying {token[1]} * {token[2]}")
            result += int(token[1])*int(token[2])
            


print(f"Result = {result}")