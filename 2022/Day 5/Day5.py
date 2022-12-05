with open("input.txt") as file:
    data = file.read().splitlines()
this = []
to = []
quantity = []
stacks = []
temp = []
for i in range(1, 36, 4):
        l = []
        for el in data[:8]:
            if el[i] != " ":
                l.append(el[i])
        stacks.append(l)

for i in range(len(stacks)):
    stacks[i].reverse()
    
del data[0:10]

for i in range(len(data)):
    e1, e2 = data[i].split("from")
    e1 = e1.replace("move ", "")
    e1 = int(e1)
    f1, f2 = e2.split("to")
    f1 = f1.replace(" ", "")
    f2 = f2.replace(" ", "")
    f1 = int(f1)
    f2 = int(f2)
    quantity.append(e1)
    this.append(f1)
    to.append(f2)

def transfer9000(a, b):
    stacks[b].append(stacks[a][-1])
    stacks[a].pop()
    
def transfer9001(a, b):
    temp.append(stacks[a][-1])
    stacks[a].pop()
    for n in range(len(temp)):
        stacks[b].append(temp[-1])
        temp.pop()

def CrateMover9000():
    for i in range(len(quantity)):
        for e in range(int(quantity[i])):
            transfer9000(int(this[i])-1, int(to[i])-1)


def CrateMover9001():
    for i in range(len(quantity)):
        for e in range(int(quantity[i])):
            temp.append(stacks[int(this[i])-1][-1])
            stacks[int(this[i])-1].pop()
        for n in range(len(temp)):
            stacks[int(to[i])-1].append(temp[-1])
            temp.pop()

CrateMover9001()

for i in range(len(stacks)):
    print(stacks[i][-1])