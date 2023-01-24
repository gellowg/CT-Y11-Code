myList = [88, 66, 44, 22, 33, 99, 11, 77, 55]
abc = 999
index = 0
length = len (myList)

while (index < length):
    if (myList[index] < abc):
        abc = myList[index]
    index = index + 1

print (abc)

