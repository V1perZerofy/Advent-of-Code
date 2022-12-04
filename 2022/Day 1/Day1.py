with open("input.txt") as file:
    data = list(map(int, file.readlines()))
file.close()
calories = 0
inv = []
for i in range(len(data)):
    if data[i] != 0:
        calories += data[i]
    else:
        inv.append(calories)
        calories = 0
inv.sort(reverse = True | False)
print("The biggest is: " + str(inv[0]))
print("The sum of the three biggest is: " + str(inv[0] + inv[1] + inv[2]))