with open("input.txt") as f:
    data = list(map(str, f.read().splitlines())) 

result1 = 0
result2 = 0

for i in range(len(data)):
    first, second = data[i].split(",")
    e1, f1 = first.split("-")
    e2, f2 = second.split("-")
    if e1 >= e2 and f1 <= f2 or e1 <= e2 and f1 >= f2: #Part 1
        result1 += 1
    if int(e1) in range(int(e2), int(f2)+1, 1) or int(f1) in range(int(e2), int(f2)+1, 1) or int(e2) in range(int(e1), int(f1)+1, 1) or int(f2) in range(int(e1), int(f1)+1, 1):
        result2 += 1