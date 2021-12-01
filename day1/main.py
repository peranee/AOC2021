list = []
f = open("input.txt", "r")
temp = 0
amount = -1
for x in f:
    if int(x) > temp:
        amount = amount + 1
    temp = int(x)
print(amount)
fi = open("input.txt", "r")
threeSum = 0
prevSum = 0
count = 0
number = 0
for x in fi:
    list.append(int(x))
threeSum = int(list[0]) + int(list[1]) + int(list[2])
while (count + 3) < len(list):
    prevSum = threeSum
    threeSum = threeSum - list[count]
    threeSum = threeSum + list[count + 3]
    if threeSum > prevSum:
        number = number + 1
    count = count + 1
print(number)