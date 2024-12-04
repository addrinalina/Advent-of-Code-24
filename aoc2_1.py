#https://adventofcode.com/2024/day/2

with open("C:\\Users\\adrir\\Documents\\GitHub\\Advent-of-Code-24\\input2.txt") as f:
    lines = f.readlines()
    x = [line[:-1] for line in lines[:-1]] + [lines[-1]]
# print(x)

cont = 0
list = []

for line in x:
    list = line.split()
    list = [int(num) for num in list]
    # Descendente
    if list[0] > list[1]:
        i = 0
        flag = False
        while flag == False and i < len(list)-1:
            if list[i] - list[i+1] > 3 or list[i] - list[i+1] <= 0:
                flag = True
                # print("La linea",list,"es UNSAFE en", i)
            else:
                i += 1
        if i == len(list) - 1:
            cont += 1
            # print("La linea",list,"es safe")
    # Ascendente
    else:
        i = 0
        flag = False
        while flag == False and i < len(list)-1:
            if list[i+1] - list[i] > 3 or list[i+1] - list[i] <= 0:
                flag = True
                # print("La linea",list,"es UNSAFE en", i)
            else:
                i += 1
        if i == len(list) - 1:
            cont += 1
            # print("La linea",list,"es safe")
print("The total of safe lines is ", cont)
        







