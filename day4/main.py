import re
def chunks (lst):
    for i in range(0, len(lst), 5):
        yield lst[i:i + 5]
def checkCol(fields):
    i = 0
    while i < 5:
        if all(x[i] == 1 for x in fields):
            return i
        i = i + 1
    return 5

def playOne(lst, numbers):
    temp = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0], [0,0,0,0,0]]
    steps = 0
    for x in numbers:
        steps = steps + 1
        i = 0
        while i < len(list(lst)):
            j = 0
            while j < len(list(lst)):
                if x == lst[i][j]:
                    temp[i][j] = 1
                j = j + 1
            i = i + 1
        if [1,1,1,1,1] in temp or (checkCol(temp) != 5):
            toret = []
            toret.append(steps)
            finalSum = 0
            i = 0
            while i < len(temp):
                j = 0
                while j < len(temp):
                    if temp[i][j] != 1:
                        finalSum = finalSum + lst[i][j]
                    j = j + 1
                i = i + 1
            toret.append(finalSum * x)
            return toret
def play(bingo, numbers):
    fin = []
    for x in bingo:
        fin.append(playOne(x, numbers))
    return fin
input = []
bingo = []
numbers = []
with open("input.txt", "r") as f:
    for x in f:
        if "," in x:
            numbers = x.split(",")
        else:
            input.append(x)
input = list(filter(lambda x: x != "\n", input))
num = []
for x in numbers:
    num.append(int(x))
for x in input:
    line = []
    y = x.split(" ")
    for j in y:
        if j != "":
            line.append(int(j))
    bingo.append(line)
time = []
#[lst[i:i + n] for i in range(0, len(lst), n)]
gen = chunks(bingo)
res = play(gen, num)
#print(res)
high = 0
low = len(num)
for x in res:
    if x[0] > high:
        high = x[0]
    if x[0] < low:
        low = x[0]
print(high)
print(low)
for x in res:
    if x[0] == high:
        print("last board score")
        print(x[1])
    if x[0] == low:
        print("first board score")
        print(x[1])
#print(num)