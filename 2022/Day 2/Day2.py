with open("input.txt") as file:                 #Format must be line 1: A, B or C line 2: X, Y or Z and so on
    data = file.read().splitlines()    #Just replace space wit \n
#print(data)
def task1():
    points = 0

    for i in range(len(data)):
        enemy, we = data[i].split(" ")
        draw, win = 3, 6
        enemy, we = enemy.replace("A", "1"), we.replace("X", "1")
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
        print("Solution for task 1 is: "+str(points))
                
def task2():
    punkte = 0
    verloren = 0
    gewonnen = 6
    unentschieden = 3
    rock = "A\n" 
    paper = "B\n"
    scissors = "C\n"
    for i in range(len(data)):
        if data[i] != "":
            if data[i] == rock:
                if data[i + 1] == "X\n":
                    punkte += verloren
                    punkte += 3
                if data[i + 1] == "Y\n":
                    punkte += unentschieden
                    punkte += 1
                if data[i + 1] == "Z\n":
                    punkte += gewonnen
                    punkte += 2
            elif data[i] == paper:
                if data[i + 1] == "X\n":
                    punkte += verloren
                    punkte += 1
                if data[i + 1] == "Y\n":
                    punkte += unentschieden
                    punkte += 2
                if data[i + 1] == "Z\n":
                    punkte += gewonnen
                    punkte += 3
            elif data[i] == scissors:
                if data[i + 1] == "X\n":
                    punkte += verloren
                    punkte += 2
                if data[i + 1] == "Y\n":
                    punkte += unentschieden
                    punkte += 3
                if data[i + 1] == "Z" or data[i + 1] == "Z\n":
                    punkte += gewonnen
                    punkte += 1
    print("Solution for task 2 is: "+str(punkte))

task1()
task2()

    