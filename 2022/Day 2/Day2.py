with open("input.txt") as file:                 #Format must be line 1: A, B or C line 2: X, Y or Z and so on
    data = list(map(str, file.readlines()))     #Just replace space wit \n
#print(data)
def task1():
    punkte = 0
    for i in range(len(data)):
        if data[i] != "":
            if data[i] == "A\n":
                if data[i + 1] == "X\n":
                    punkte += 1
                    punkte += 3
                if data[i + 1] == "Y\n":
                    punkte += 2
                    punkte += 6
                if data[i + 1] == "Z\n":
                    punkte += 3
                    punkte += 0
            elif data[i] == "B\n":
                if data[i + 1] == "X\n":
                    punkte += 1
                    punkte += 0
                if data[i + 1] == "Y\n":
                    punkte += 2
                    punkte += 3
                if data[i + 1] == "Z\n":
                    punkte += 3
                    punkte += 6
            elif data[i] == "C\n":
                if data[i + 1] == "X\n":
                    punkte += 1
                    punkte += 6
                if data[i + 1] == "Y\n":
                    punkte += 2
                    punkte += 0
                if data[i + 1] == "Z" or data[i + 1] == "Z\n":
                    punkte += 3
                    punkte += 3
    print("Solution for task 1 is: "+str(punkte))
                
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

    