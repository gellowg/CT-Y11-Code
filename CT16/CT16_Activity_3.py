butter = 0
flour = 0
sugar = 0
eggs = 0

butter = int (input ("Enter grams of butter: "))
flour = int (input ("Enter grams of flour: "))
sugar = int (input ("Enter grams of sugar: "))
eggs = int (input ("Enter number of eggs: "))

if (butter < 250):
    print ("Buy butter")
elif ((eggs < 3) or (eggs > 4)):
    print ("Check eggs")
elif ((sugar < 200) and (flour < 200)):
    print ("Buy dry goods")
elif (((sugar > 225) or (flour > 250)) and (butter > 300)):
    print ("Make a bigger cake")
else:
    print ("Start baking!")

