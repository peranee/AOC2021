import re
points = []
collision = []
with open("input.txt", "r") as f:
    for x in f:
        y = x.split(" ")
        first = y[0].split(",")
        second = y[2].split(",")
        #print(first)
        #print(second)
        x1 = int(first[0])
        y1 = int(first[1])
        x2 = int(second[0])
        y2 = int(second[1])
        if x1 == x2:
            i = min(y1, y2)
            while i <= max(y1, y2):
                if [x1, i] in points:
                    collision.append([x1, i])
                else:
                    points.append([x1, i])
                i = i + 1
        elif y1 == y2:
            i = min(x1, x2)
            while i <= max(x1, x2):
                if [i, y1] in points:
                    collision.append([i, y1])
                else:
                    points.append([i, y1])
                i = i + 1
        elif (abs(y1-y2)/abs(x1 - x2)) == 1:
            if x1 < x2:
                if y1 < y2:
                    i = x1
                    j = y1
                    while i <= x2 and j <= y2:
                        if [i, j] in points:
                            collision.append([i, j])
                        else:
                            points.append([i,j])
                        i = i + 1
                        j = j + 1
                # x1 < x2 and y2 < y1
                else:
                    i = x1
                    j = y1
                    while i <= x2 and j >= y2:
                        if [i, j] in points:
                            collision.append([i,j])
                        else:
                            points.append([i,j])
                        i = i + 1
                        j = j - 1
            #x2 < x1
            else:
                if y1 < y2:
                    i = x2
                    j = y2
                    while i <= x1 and j >= y1:
                        if [i, j] in points:
                            collision.append([i, j])
                        else:
                            points.append([i, j])
                        i = i + 1
                        j = j - 1
                else:
                    i = x1
                    j = y1
                    while i >= x2 and j >= y2:
                        if [i, j] in points:
                            collision.append([i, j])
                        else:
                            points.append([i, j])
                        i = i - 1
                        j = j - 1
#collision = list(set(collision))
res = []
[res.append(x) for x in collision if x not in res]
print(len(res))