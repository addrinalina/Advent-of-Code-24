#https://adventofcode.com/2024/day/4

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input4.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
print(x)

import re, numpy
count = 0

xrev = [line[::-1] for line in x]

print(f"xrev {xrev}")

x2 = [["" for _ in range(len(x[0]))] for _ in range(len(x))]
x3 = [["" for _ in range(2*len(x[0]))] for _ in range(2*len(x))]
x4 = [["" for _ in range(2*len(x[0]))] for _ in range(2*len(x))]

for i in range(len(x)):
    for j in range(len(x[0])):
        x2[j][i] = x[i][j]
    
    if i == 0:
        for j in range(len(x[0])):    
            for k in range(len(x)-j):
                # print(f"i={i} j={j} k={k}, {x[i+k][j+k]} va a ser el x3[{i+j},{i+k}]")
                x3[i+j][i+k] = x[i+k][j+k]
                x4[i+j][i+k] = xrev[i+k][j+k]
    else:
        for k in range(len(x)-i):
            # print(f"i={i} k={k}, {x[i+k][k]} va a ser el x3[{i+len(x)},{i+k}]")
            x3[i+len(x)][i+k] = x[i+k][k]
            x4[i+len(x)][i+k] = xrev[i+k][k]

#ME FALTAN LAS DIAGONALES DE ABAJO A ARRIBA

x2 = ["".join(row) for row in x2]
x3 = ["".join(row) for row in x3]
x4 = ["".join(row) for row in x4]

print(f"X2 es {x2}")
print(f"X3 es {x3}")
print(f"X4 es {x4}")

for i in range(len(x)):
    matches1 = x[i].count("XMAS")
    matches2 = x[i][::-1].count("XMAS")
    matches3 = x2[i].count("XMAS")
    matches4 = x2[i][::-1].count("XMAS")
    matches5 = x3[i].count("XMAS") + x3[i+len(x)].count("XMAS")
    matches6 = x3[i][::-1].count("XMAS") + x3[i+len(x)][::-1].count("XMAS")
    matches7 = x4[i][::-1].count("XMAS") + x4[i+len(x)][::-1].count("XMAS")
    matches8 = x4[i].count("XMAS") + x4[i+len(x)].count("XMAS")
    count += matches1 + matches2 + matches3 + matches4 + matches5 + matches6 + matches7 + matches8
    print(f"{i} Found {matches1} normally written, {matches2} backwards, {matches3} downwards, {matches4} upwards, {matches5} diagonally LU, {matches6} diagonally RD, {matches7} diagonally LD, {matches8} diagonally RU")

print(f"Total {count} matches")