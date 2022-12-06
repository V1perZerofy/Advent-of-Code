with open("input.txt") as file:
    data = file.read().splitlines()
    
points = 0
points2 = 0

for i in range(len(data)):
    enemy, we = data[i].split(" ")
    draw, win = 3, 6
    enemy, we = enemy.replace("A", "1",), we.replace("X", "1")
    enemy, we = enemy.replace("B", "2"), we.replace("Y", "2")
    enemy, we = enemy.replace("C", "3"), we.replace("Z", "3")
    enemy, we = int(enemy), int(we)
    if enemy == we:
        points += draw
        points += we
    elif we == 3 and enemy == 1:
        points += we
    elif we == 3 and enemy == 2:
        points += win
        points += we
    elif we == 2 and enemy == 3:
        points += we
    elif we == 2 and enemy == 1:
        points += win
        points += we
    elif we == 1 and enemy == 2:
        points += we
    elif we == 1 and enemy == 3:
        points += win
        points += we

for i in range(len(data)):
    enemy, we = data[i].split(" ")
    draw, win = 3, 6
    enemy, we = enemy.replace("A", "1",), we.replace("X", "Loss")
    enemy, we = enemy.replace("B", "2"), we.replace("Y", "Draw")
    enemy, we = enemy.replace("C", "3"), we.replace("Z", "Win")
    enemy = int(enemy)
    if we == "Loss" and enemy == 1:
        points2 += 3
    elif we == "Loss" and enemy == 2:
        points2 += 1
    elif we == "Loss" and enemy == 3:
        points2 += 2
    elif we == "Draw" and enemy == 1:
        points2 += draw
        points2 += 1
    elif we == "Draw" and enemy == 2:
        points2 += draw
        points2 += 2
    elif we == "Draw" and enemy == 3:
        points2 += draw
        points2 += 3
    elif we == "Win" and enemy == 1:
        points2 += win
        points2 += 2
    elif we == "Win" and enemy == 2:
        points2 += win
        points2 += 3
    elif we == "Win" and enemy == 3:
        points2 += win
        points2 += 1
    
print("The solution for part 1 is: " + str(points))
print("The solution for part 2 is: " + str(points2))