with open("C:\Users\niels\OneDrive\Dokumente\GitHub\Advent-of-Code\2021\Day 1\liste.txt") as file:
    data = list(map(int, file.readlines()))

data

a = 0

for i in range(len(data)):
    if i < (len(data) - 1):
        if data[i + 1] > data[i]:
            a += 1
    else:
        break

print(a)