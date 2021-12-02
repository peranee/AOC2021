import re
f = open("input.txt", "r")
hor = 0
depth = 0
for x in f:
    words = x.split(" ")
    if "f" in words[0]:
        hor = hor + int(words[1])
    elif "u" in words[0]:
        depth = depth - int(words[1])
    else:
        depth = depth + int(words[1])
print(hor)
print(depth)
res = hor * depth
print(res)
fi = open("input.txt", "r")
hor = 0
depth = 0
aim = 0
for x in fi:
    words = x.split(" ")
    if "f" in words[0]:
        hor = hor + int(words[1])
        depth = depth + (aim * int(words[1]))
    elif "u" in words[0]:
        aim = aim - int(words[1])
    else:
        aim = aim + int(words[1])
print(hor)
print(depth)
res = hor * depth
print(res)