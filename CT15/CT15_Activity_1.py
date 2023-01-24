myList = [10, 20, 30, 40, 50]
total = 0
position = 0

position = len (myList) - 1

while (position >= 0):
    print (myList[position])
    total = total + myList[position]
    position = position - 1

print (total)

