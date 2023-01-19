id = ""
num = 0
name = ""

num = int (input ("Enter a number: "))
name = input ("Enter a name: ")

if ((num > 0) or (num <= 99)):
    if (len (name) > 0):
        id = name + str (num)
        print(id)
else:
    print ("Invalid number")