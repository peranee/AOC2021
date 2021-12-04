def distrOne(list):
    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    for x in list:
        j = 0
        while j < 12:
            if x[j] == "1":
                one[j] = one[j] + 1
            j = j + 1
    return one
def distrZero(list):
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    for x in list:
        j = 0
        while j < 12:
            if x[j] == "0":
                zero[j] = zero[j] + 1
            j = j + 1
    return zero

with open("input.txt", "r") as f:
    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    list1 = []
    list2 = []
    for x in f:
        list1.append(x)
        list2.append(x)
        count = 0
        while count < 12:
            if x[count] == "1":
                one[count] = one[count] + 1
            else:
                zero[count] = zero[count] + 1
            count = count + 1
    gamma = ""
    epsilon = ""
    i = 0
    while i < len(one):
        if one[i] < zero[i]:
            gamma = gamma + str(0)
            #gamma.append(0)
            epsilon = epsilon + str(1)
        else:
            gamma = gamma + str(1)
            epsilon = epsilon + str(0)
        i = i + 1
    print(gamma)
    print(epsilon)
    print(int(gamma))
    print (int(gamma, 2) * int(epsilon, 2))
    print(len(list1))
    print(len(list2))
    print(one)
    print(zero)
    j = 0
    while j < 12 and len(list1) > 1:
        if one[j] < zero[j]:
            list1 = list(filter(lambda x: x[j] == "0", list1))
        else:
            list1 = list(filter(lambda x: x[j] == "1", list1))
        j = j + 1
        one = distrOne(list1)
        zero = distrZero(list1)
    j = 0
    while j < 12 and len(list2) > 1:
        if one[j] < zero[j]:
            list2 = list(filter(lambda x: x[j] == "1", list2))
        else:
            list2 = list(filter(lambda x: x[j] == "0", list2))
        j = j + 1
        one = distrOne(list2)
        zero = distrZero(list2)
    print(list1)
    print(list2)
    print(int(list1[0], 2))
    print(int(list2[0], 2))
    print(int(list1[0], 2) * int(list2[0], 2))
    


    