#https://adventofcode.com/2024/day/5

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input5.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

rules = []
updates = []

for line in x:
    if "|" in line:
        rules.append([x for x in line.split("|")])
    elif "," in line:
        updates.append([x for x in line.split(",")])
# print(rules)
# print(updates)

result = 0

for printing in updates:
    valid = True
    for i in range(len(printing)):
        for rule in rules:
            if printing[i] == rule[0]:
                for j in range(0,i):
                    if printing[j] == rule[1]:
                        valid = False
                        print(f" -- {printing} no cumple la regla {rule}")
                        break
            if valid == False:
                break
        if valid == False:
            break
    if valid:
        mid = int(printing[int((len(printing)-1)/2)])
        print(f"{printing} es válido, y su número en medio es {mid}")
        result += mid
print(f"Resultado = {result}")
